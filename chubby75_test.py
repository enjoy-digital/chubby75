#!/usr/bin/env python3

from fractions import Fraction

from migen import *
from migen.genlib.resetsync import AsyncResetSynchronizer

from litex.soc.integration.soc_core import *
from litex.soc.integration.builder import *
from litex.soc.cores.clock import period_ns

from liteeth.common import *
from gateware.s6rgmii import LiteEthPHYRGMII
from liteeth.core import LiteEthUDPIPCore

import chubby75_platform


class _CRG(Module):
    def __init__(self, platform, sys_clk_freq):
        self.clock_domains.cd_sys = ClockDomain()

        self.reset = Signal()

        f0 = 25*1000000
        clk25 = platform.request("clk25")
        clk25a = Signal()
        self.specials += Instance("IBUFG", i_I=clk25, o_O=clk25a)
        clk25b = Signal()
        self.specials += Instance("BUFIO2", p_DIVIDE=1,
                                  p_DIVIDE_BYPASS="TRUE", p_I_INVERT="FALSE",
                                  i_I=clk25a, o_DIVCLK=clk25b)
        f = Fraction(int(sys_clk_freq), int(f0))
        n, m = f.denominator, f.numerator
        assert f0/n*m == sys_clk_freq
        p = 8
        pll_lckd = Signal()
        pll_fb = Signal()
        pll_sys = Signal()
        self.specials.pll = [
            Instance("PLL_ADV",
                p_SIM_DEVICE="SPARTAN6",
                p_BANDWIDTH="OPTIMIZED", p_COMPENSATION="INTERNAL",
                p_REF_JITTER=.01, p_CLK_FEEDBACK="CLKFBOUT",
                i_DADDR=0, i_DCLK=0, i_DEN=0, i_DI=0, i_DWE=0, i_RST=0, i_REL=0,
                p_DIVCLK_DIVIDE=1, p_CLKFBOUT_MULT=m*p//n, p_CLKFBOUT_PHASE=0.,
                i_CLKIN1=clk25b, i_CLKIN2=0, i_CLKINSEL=1,
                p_CLKIN1_PERIOD=1e9/f0, p_CLKIN2_PERIOD=0.,
                i_CLKFBIN=pll_fb, o_CLKFBOUT=pll_fb, o_LOCKED=pll_lckd,
                o_CLKOUT0=pll_sys, p_CLKOUT0_DUTY_CYCLE=.5,
                p_CLKOUT0_PHASE=0., p_CLKOUT0_DIVIDE=p//1),
            Instance("BUFG", i_I=pll_sys, o_O=self.cd_sys.clk)
        ]
        reset = self.reset
        self.clock_domains.cd_por = ClockDomain()
        por = Signal(max=1 << 11, reset=(1 << 11) - 1)
        self.sync.por += If(por != 0, por.eq(por - 1))
        self.comb += self.cd_por.clk.eq(self.cd_sys.clk)
        self.specials += AsyncResetSynchronizer(self.cd_por, reset)
        self.specials += AsyncResetSynchronizer(self.cd_sys, ~pll_lckd | (por > 0))
        platform.add_period_constraint(self.cd_sys.clk, period_ns(sys_clk_freq))


class EthernetTestSoC(SoCCore):
    csr_map = {
        "ethphy":  11,
        "ethcore": 12
    }
    csr_map.update(SoCCore.csr_map)
    def __init__(self, platform, mac_address=0x10e2d5000000, ip_address="192.168.1.50"):
        sys_clk_freq = int(150e6)
        SoCCore.__init__(self, platform, sys_clk_freq, cpu_type=None, with_uart=False)

        # crg
        self.submodules.crg = _CRG(platform, sys_clk_freq)

        # ethernet
        self.submodules.ethphy = LiteEthPHYRGMII(platform.request("eth_clocks"),
                                            platform.request("eth"))
        self.submodules.ethcore = LiteEthUDPIPCore(self.ethphy,
                                                   mac_address,
                                                   convert_ip(ip_address),
                                                   sys_clk_freq,
                                                   with_icmp=True)
        self.ethphy.crg.cd_eth_rx.clk.attr.add("keep")
        self.ethphy.crg.cd_eth_tx.clk.attr.add("keep")
        platform.add_period_constraint(self.ethphy.crg.cd_eth_rx.clk, period_ns(125e6))
        platform.add_period_constraint(self.ethphy.crg.cd_eth_tx.clk, period_ns(125e6))
        platform.add_false_path_constraints(
            self.crg.cd_sys.clk,
            self.ethphy.crg.cd_eth_rx.clk)
        platform.add_false_path_constraints(
            self.crg.cd_sys.clk,
            self.ethphy.crg.cd_eth_tx.clk)
        platform.add_source("gateware/rgmii_if.vhd")


def main():
    platform = chubby75_platform.Platform()
    soc = EthernetTestSoC(platform)
    builder = Builder(soc, output_dir="build")
    builder.build()

if __name__ == "__main__":
    main()

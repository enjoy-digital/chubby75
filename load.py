#!/usr/bin/env python3

from litex.build.openocd import OpenOCD
prog = OpenOCD("openocd.cfg")
prog.load_bitstream("build/gateware/top.bit")

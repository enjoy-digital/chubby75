HUB75E "hat" hardware
=====================

Layout/numbering
----------------

The board consists of 10 connectors (marked J1-J10) and 6 74HC245TS buffers (marked U1-U6).

J600/J601 connectors are numbered as per RV901T markings. J601 is the RV901T connector that mates with JP1, J600 is the RV901T connect that makes with JP2.

HUB75E connectors
----------------

```
  _________
 |  R1 G1  |
 |  B1 GND |
 |  R2 G2  |
  | B2 E   |
  |  A B   |
 |   C D   |
 | CLK STB |
 |  OE GND |
  ---------
```

74HC245 buffers
----------------

`DIR` on all buffers is strapped to `VCC`.

U1

| Ch. | A-side   | B-side          |
|---|------------|-----------------|
| 0 | J601.44    | J1.CLK          |
| 1 | J601.44    | J2.CLK          |
| 2 | J601.44    | J3.CLK          |
| 3 | J601.44    | J4.CLK          |
| 4 | J601.44    | J5.CLK          |
| 5 | J601.43    | J1.STB, J2.STB  |
| 6 | J601.43    | J3.STB, J4.STB  |
| 7 | J601.43    | J5.STB, J6.STB  |

U2

| Ch. | A-side   | B-side          |
|---|------------|-----------------|
| 0 | J601.43    | J7.STB, J8.STB  |
| 1 | J601.43    | J9.STB, J10.STB |
| 2 | J601.42    | J1.A, J2.A      |
| 3 | J601.42    | J3.A, J4.A      |
| 4 | J601.42    | J5.A, J6.A      |
| 5 | J601.42    | J7.A, J8.A      |
| 6 | J601.42    | J9.A, J10.A     |
| 7 | J601.41    | J1.B, J2.B      |


U3

| Ch. | A-side   | B-side        |
|---|------------|---------------|
| 0 | J601.41    | J3.B, J4.B    |
| 1 | J601.41    | J5.B, J6.B    |
| 2 | J601.41    | J7.B, J8.B    |
| 3 | J601.41    | J9.B, J10.B   |
| 4 | J601.40    | J1.C, J2.C    |
| 5 | J601.40    | J3.C, J4.C    |
| 6 | J601.40    | J5.C, J6.C    |
| 7 | J601.40    | J7.C, J8.C    |

U4

| Ch. | A-side   | B-side        |
|---|------------|---------------|
| 0 | J601.40    | J10.C, J9.C   |
| 1 | J601.39    | J1.D, J2.D    |
| 2 | J601.39    | J3.D, J4.D    |
| 3 | J601.39    | J5.D, J6.D    |
| 4 | J601.39    | J7.D, J8.D    |
| 5 | J601.39    | J9.D, J10.D   |
| 6 | J600.44    | J9.CLK        |
| 7 | J600.44    | J10.CLK       |

U5

| Ch. | A-side   | B-side        |
|---|------------|---------------|
| 0 | J600.45    | J1.OE, J2.OE  | 
| 1 | J600.45    | J3.OE, J4.OE  | 
| 2 | J600.45    | J5.OE, J6.OE  | 
| 3 | J600.45    | J7.OE, J8.OE  | 
| 4 | J600.45    | J9.OE, J10.OE | 
| 5 | J600.44    | J6.CLK        |
| 6 | J600.44    | J7.CLK        |
| 7 | J600.44    | J8.CLK        |

U6

| Ch. | A-side   | B-side               |
|---|------------|----------------------|
| 0 | J600.6     | J10.E, J9.E (via R3) |
| 1 | J600.6     | J8.E, J7.E (via R4)  |
| 2 | J600.6     | J6.E, J5.E (via R5)  |
| 3 | J600.6     | J4.E, J3.E (via R6)  |
| 4 | J600.6     | J2.E, J1.E (via R7)  |
| 5 | NC         | NC                   |
| 6 | NC         | NC                   |
| 7 | NC         | NC                   |


Final pinout
------------

| Signal          | J600/J601 pin                      | FPGA Pin |
|-----------------|------------------------------------|----------|
| HUB75.*.OE      | J600.45 (via U5)                   | C11      |
| HUB75.*.STB     | J601.43 (via U1, U2)               | A14      |
| HUB75.*.CLK     | J601.44 (via U1), J600.44 (via U4) | B14      |
| HUB75.*.A       | J601.42 (via U2)                   | C13      |
| HUB75.*.B       | J601.41 (via U2, U3)               | A13      |
| HUB75.*.C       | J601.40 (via U3, U4)               | B12      |
| HUB75.*.D       | J601.39 (via U4)                   | A12      |
| HUB75.*.E       | J600.6 (via U6 and resistors)      | A11      |
| HUB75.J1.RD1    | J601.38                            | B6       |
| HUB75.J1.GD1    | J601.37                            | C6       |
| HUB75.J1.BD1    | J601.36                            | C7       |
| HUB75.J1.RD2    | J601.35                            | C8       |
| HUB75.J1.GD2    | J601.34                            | C9       |
| HUB75.J1.BD2    | J601.33                            | E6       |
| HUB75.J2.RD1    | J601.32                            | D6       |
| HUB75.J2.GD1    | J601.31                            | E7       |
| HUB75.J2.BD1    | J601.30                            | E8       |
| HUB75.J2.RD2    | J601.29                            | D8       |
| HUB75.J2.GD2    | J601.28                            | F9       |
| HUB75.J2.BD2    | J601.27                            | D9       |
| HUB75.J3.RD1    | J601.26                            | E10      |
| HUB75.J3.GD1    | J601.25                            | D11      |
| HUB75.J3.BD1    | J601.24                            | D12      |
| HUB75.J3.RD2    | J601.23                            | E11      |
| HUB75.J3.GD2    | J601.22                            | B10      |
| HUB75.J3.BD2    | J601.21                            | A10      |
| HUB75.J4.RD1    | J601.20                            | A9       |
| HUB75.J4.GD1    | J601.19                            | B8       |
| HUB75.J4.BD1    | J601.18                            | A8       |
| HUB75.J4.RD2    | J601.17                            | A7       |
| HUB75.J4.GD2    | J601.16                            | A6       |
| HUB75.J4.BD2    | J601.15                            | A5       |
| HUB75.J5.RD1    | J601.14                            | A3       |
| HUB75.J5.GD1    | J601.13                            | A2       |
| HUB75.J5.BD1    | J601.12                            | B2       |
| HUB75.J5.RD2    | J601.11                            | A4       |
| HUB75.J5.GD2    | J601.10                            | D5       |
| HUB75.J5.BD2    | J601.9                             | B3       |
| HUB75.J6.RD1    | J600.38                            | T5       |
| HUB75.J6.GD1    | J600.37                            | R5       |
| HUB75.J6.BD1    | J600.36                            | T6       |
| HUB75.J6.RD2    | J600.35                            | T7       |
| HUB75.J6.GD2    | J600.34                            | R7       |
| HUB75.J6.BD2    | J600.33                            | T8       |
| HUB75.J7.RD1    | J600.32                            | R9       |
| HUB75.J7.GD1    | J600.31                            | R9       |
| HUB75.J7.BD1    | J600.30                            | T11      |
| HUB75.J7.RD2    | J600.29                            | P11      |
| HUB75.J7.GD2    | J600.28                            | N9       |
| HUB75.J7.BD2    | J600.27                            | L10      |
| HUB75.J8.RD1    | J600.26                            | M10      |
| HUB75.J8.GD1    | J600.25                            | M11      |
| HUB75.J8.BD1    | J600.24                            | N11      |
| HUB75.J8.RD2    | J600.23                            | M12      |
| HUB75.J8.GD2    | J600.22                            | N8       |
| HUB75.J8.BD2    | J600.21                            | P7       |
| HUB75.J9.RD1    | J600.20                            | L8       |
| HUB75.J9.GD1    | J600.19                            | L7       |
| HUB75.J9.BD1    | J600.18                            | M6       |
| HUB75.J9.RD2    | J600.17                            | N6       |
| HUB75.J9.GD2    | J600.16                            | M7       |
| HUB75.J9.BD2    | J600.15                            | P6       |
| HUB75.J10.RD1   | J600.14                            | P5       |
| HUB75.J10.GD1   | J600.13                            | T4       |
| HUB75.J10.BD1   | J600.12                            | K6       |
| HUB75.J10.RD2   | J600.11                            | M5       |
| HUB75.J10.GD2   | J600.10                            | L5       |
| HUB75.J10.BD2   | J600.9                             | M4       |

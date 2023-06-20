# Build Instructions


## Rogowski Coil
The rogowski coil assembly consists of the wound coil, the 3D printed housing, and a small PCB which connects the rogowski coil to a U.FL connector and holds the termination resistor.

This rogowski coil design involved winding countless coils and trying over 20 types of heatshrink to find a design with good electrical performance, an outer diameter less than 1.7mm so the coil can fit between the leads of a TO-220 package, and is mechanically robust to bending and abrasion.
The integrator design is tuned to the properties of the rogowski coil described here.
If the coil size is changed or different materials are used the coil sensitivity will be different and the integrator may not be able to be adjusted for a nominal gain of 0.1V/A or a flat pulse response.

When winding the coil it is of utmost importance that the winding are uniform with no gaps or overlaps.
A constant winding tension is important as the tension causes shrinkage of the PTFE tube and a non-uniform cross section degrades the rejection of external magnetic fields.

As a general summary of the coil winding and assembly, the coil is wound on a PTFE tube.
The starting wire is secured by a small hole in the tube and passed through the center of the tube such that the start and end wires are at the same end.
UV cure epoxy is used to temporally secure the coil end after winding and the coil is protected with FEP heatshrink.
Additional heat shrink is used to strain relief the coil and and the coaxial cable that connects the rogowski coil to the integrator.


| <img src="img/coil_assembly.jpg" width="600"/> | 
|:--:| 
| *Rogowski coil assembly before top case is installed* |

### 3D prints
1x of `coil_retainer_bottom.stl` and `coil_retainer_top.stl`
Printed in SLS nylon.
Test parts were printed out of 3201PA-F Nylon through JLCPCB.

### PCB
Coil terminator board populated with 680 ohm 1206 resistor and U.FL connector

### Parts
* 1.3x shrink ratio FEP for 18 Wire Gage, McMaster-Carr P/N 8703K114
* 2.5mm diameter 2x shrink ratio Polyolefin heat shrink, Digikey P/N HST-04-WT-4
* 0.6mm ID x 1mm OD PTFE tubing, [Amazon](https://www.amazon.com/gp/product/B07F5X51F5/)
* 36AWG MW 35-C magnet wire, Remington Industries P/N 36S200P
* 450mm 1.37mm coax cable, U.FL to U.FL, Digikey P/N 732-636201100450-ND
* 4x M1.6x6 flat head self tapping screw McMaster-Carr P/N 95893A162
* double sided adhesive tape, 3M 9495LE or similar
* UV cure epoxy, Loctite 3494 or similar
* 1/16"-004 O-Ring, McMaster-Carr P/N 9452K12

### Build Instructions

#### Bare Coil
1. Cut 1mm OD PTFE tube to 90mm length, cut hole big enough to pass 36 AWG wire 2mm from one end.
2. Thread 36 AWG magnet wire through the hole and have the wire exit the opposite end of the PFTE tube.
3. With the end of the magnet wire secured, wind a coil around the tube, winding should extend to the bottom 4mm of the tube. Use constant tension and ensure there are no gaps, overlaps, or kinks. This process can be easier by using a think stainless steel wire as a mandrel to hold the tube.
4. Secure the end of the winding with a small dab of UV cure epoxy. Cut the coil ends to 5mm length
5. Cut 100mm of the FEP heatshrink and heatshrink the coil with hot air at 250C. Start from the coil end and ensure the heat shrink starts flush with the PFET tube. After heating, trim the heatshink to be flush with the far end of the PTFE tube.
6. Cut 10mm of the Polyolefin heat shrink and apply to the wire end of the coil. Make sure that the heat shrink is flush with the existing heatshrink and coil end, it should not overhang. Process with 250C hot air. 
7. Strip the last 2mm of the wires of enamel and tin with solder.

#### Coil Assembly
1. Cut 50mm of the Polyolefin heat shrink and apply to both ends of the coax cable. The heat shrink should be flush with the neck of the U.FL connector. Process with 250C hot air.
2. Secure the coil terminator PCB to the inside of the bottom coil retainer housing with adhesive tape. The board edge should be flush with the wall where the rogowski coil is connected.
3. Solder the rogowski coil leads to the pads on the coil terminator board. Minimize any exposed loops. 
4. Connect the coaxial cable to the U.FL connector on the coil terminator board.
5. Place an O-ring in the O-ring retaining grove.
6. Make sure that the end of the rogowski coil is flush with the inner wall. Cover with the top coil retainer housing, compress the housing halves together and secure with M1.6x6 self tapping screws. Use gentle tightening force to ensure screw holes do not strip out. 



## Integrator 
The final assembly is the integrator PCBA and the rogowski coil.
The project is contained in an off the shelf project box and uses PCB based front and rear panels.
The integrator PCBA was optimized for assembly with the JLCPCB PCBA service, but component availability varies.
The KiCad project contains both a BOM with LCSC part numbers and a BOM with western part numbers stocked at Digikey. 

| <img src="img/amplifier_open.jpg" width="600"/> | 
|:--:| 
| *Complete current probe with top case open* |

### PCBs
* Integrator PCBA
* Front panel PCB
* Rear Panel PCB

### Parts

* \#4-1/4" thread cutting screws, McMaster-Carr P/N 94629A150
* M6X1.0 Cable gland, Generic, [Aliexpress example](https://www.aliexpress.us/item/3256803804996455.html)
* M6X1.0 thin hex nut, McMaster-Carr P/N 90710A038
* ABS Project Enclosure, Digikey P/N 377-1651-ND
* Ferrite EMI suppression bead, Digikey P/N 1934-1323-ND
* 5mm LED light pipe, Digikey P/N 492-1531-ND

#### Assembly
1. Attach the M6 cable gland to the front panel PCB with the M6 nut and tighten. Press fit the LED light pipe into the front panel.
2. Slide the rear panel over the SMA and USB connectors of the integrator PCB and slide the integrator PCBA and panel PCBs into the project box.
3. Secure integrator PCBA to the project box with the \#4-1/4" screws.
4. Thread the coaxial cable of the rogowski coil assembly through the cable gland. 
5. Slide the ferrite bead over the side of the coaxial cable that is inside the project box.
6. Connect the U.FL connector of the rogowski coil assembly to the U.FL connector of the integrator PCBA. Adjust the cable length such that the cable is not under tension and then tighten the cable gland.
7. Secure the ferrite bead to the integrator PCBA with adhesive or zip-tie. 
8. After calibration, install the top of the project box. 

#### Calibration
With a 100KHz square wave current source adjust the gain and compensation trimmer resistors such that the pulse response is flat and the probe gain is the nominal 0.1V/A.
The compensation trimmer adjusts the rising edge of the waveform and also impacts the gain and should be adjusted first.

A function generator driving a 10 turn coil and a 1 ohm shunt resistor to provide a reference signal should provide a sufficient signal for calibration.
When multiple loops of the same wire pass through the sensing coil the measured current is the current flowing through the wire times the number of turns. 


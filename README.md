# SPAM-LIKELY

![Double](Double.jpg)
## Story

The Spam-Likely Split Keyboard Rev0 was designed as my first attempt at building a keyboard. In response to Ben Vallack (Later referred to as "Tom" in other areas of my writing and memory) and his youtube video entitled [“The REAL Ergonomic Keyboard Endgame!” - How To Design & Make A Totally Custom Keyboard](https://www.youtube.com/watch?v=UKfeJrRIcxw), I created a rough document with the design goals below. The project started with the [ergogen project](https://github.com/ergogen/ergogen), and quickly lead into using ki-cad and other new tools

In particular, I'm looking to have something that I can build and itterate on, and I want to be able to make modifications to, and use this as a tool to further learn how to use new modules over raw IO, SPI, UART, and I2C.

I chose the KB2040 for this board when I learned about the two peripheral interfaces I can activate over either SPI, UART, or I2C. This gives me sufficiant options to learn how different plugable modules might work, and the horsepower behind it seems underutilized for my purposes. 

In reviewing other designs, I knew that I didn't want to use a traditional diode matrix for the following reasons.
- diodes tend to be at or near the point of keystrike
- diodes are directional; they're electronic valves, so if I solder this by hand especially at night, there's a larger chance of creating new problems, and higher risk of failure on first time bootup
- the matrix takes up too many pins, and does not give enough space for experimentation
- the traditional grid-style matrix circuit design **did not bring me joy**

In this I started seeking alternatives. At one point I was at one point set on using the PCA9506 I2C GPIO expander, as referenced by Zach Freedman in his [Mirage project](https://github.com/ZackFreedman/MiRage). The lack of availaibility of the PCA9506, which includes built-in pull-up resistors, and the high cost of failure (and parts) lead me to search for alternatives again. A general IO expander over SPI seemed like the best bet, and I looked into Adafruit's MCP23017 expander board as a solution. These boards were at a shortage at the time, and I went back to discord boards to complain. 

Designer [Deshipu](https://github.com/deshipu) lead me to the idea of using shift registers as an alternative. The libraries were included by default with the keypad library in circuitpython, and wouldn't require that I use extra peripheral "slots" to drive the board. I found the specific model 74HC597E, which was availible from multiple manufacturers, could be driven by 3.3v or 5v, and was cheap. Allong with some network resistors, I started on the breadboard using the following design schematic referenced from [Nuts and Volts; November 2010](https://www.nutsvolts.com/magazine/article/november2010_smileysworkshop).	 ![75HC579-SCHEMATIC](https://www.nutsvolts.com/uploads/wygwam/NV_1110_Pardue_Figure-8---Parallel-In-Serial-Out-Schematic.jpg)

In addition to the features specified, other options were added including a 5 way switch for naviation, a thumbstick, and an I2C breakout header. These may change in future revisions.

## Design goals
- Split Keyboard
- Ergonomic -- This fits to my hand
- All keys can be reached from neutral position
- No need for diodes
- Board is flipable -- one board can be used for left or right hand
- ~Use IO Expanders for additional Modules (PCA9505)~
- Use Shift Registers for standard IO
- Microcontroller is socketed
- Firmware can be updated without flashing the board
- Break out all unused pins

### Keys:
- Low Profile Keys 
- Choc V1
- linear
- light touch keys

### Display Hardware:
- Not limited by board
- TFT display
- OLED Display

### Design Options:
- Sockets for IO Expanders
- Wireless Conversion available
- Modular, to allow new components using the same standard onto the board
- PS2 Output
- Onboard Storage / SD Card via add-on
- Case to house the board
- Tenting options

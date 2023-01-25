# Micropython-ESPNOW-IOT-button-example
Example code for my 3D printed Big Iot button using a Lolin 32 C3 Pico.

The reciever code was writen for the Lolin S2 Mini, you may have to change pin numbers to make my example work on your microcontrollers. Also, you will have to fill in your own devices' MAC addresses in the codes

In this example, I used the reset button (PINS EN and GND wired to a button) to make the Lolin 32 C3 Pico execute code and then go to sleep. This option is the easiest and doesn't require any software or hardware resistors. Be aware that although economical, this option limits you on fuctionality as it prevents you form adding a long press or double click function to the button. For those more advanced functions, I'd suggest you to go lookup micropython's documentation on deepsleep for ESP32 and wakeup on Ext0. 


Big thanks to @glenn20 for creating the Micropython ESPNow library and helping me with this code.

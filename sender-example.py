import esp32
import machine
import time
import espnow
import network
import neopixel

np = neopixel.NeoPixel(machine.Pin(7),1) #neopixel Pin
bat = machine.ADC(machine.Pin(3)) #Battery voltage pin

#Colour labels for the neopixel
green = (220, 0, 0)
yellow = (150, 220, 10)
orange = (50 , 220, 0)
red = (0, 220, 0)
blue = (0, 0, 220)
clear = (0,0,0)

def np_blink(colour, interval, nb): #neopixel blink function
  for i in range(nb):
    np[0] = colour
    np.write()
    time.sleep(interval)
    np[0] = clear
    np.write()
    time.sleep(interval)

def wifi_off():
  e.active(False)
  sta.active(False)

def gotosleep(): #Sleep routine that will prevent you if battery is low
  level = bat.read()
  if level > 2500:
    wifi_off()
    machine.deepsleep()
  else:
    wifi_off()
    np_blink(orange, 0.3, 20)
    machine.deepsleep()

# Turning on wifi for espnow
sta = network.WLAN(network.STA_IF)
sta.active(True)

# Registering peer(s)
e = espnow.ESPNow()
e.active(True)
peer = b'\x00\x00\x00\x00\x00\x00' # Put the reciever's mac address here
e.add_peer(peer)

# Sending message that button has been pressed
e.send(b'press')
host, msg = e.irecv(5000)

if msg:
  if msg == b'pressed':
    np_blink(green, 0.1, 4)
    gotosleep()
else:
  np_blink(yellow, 0.3, 5)
  v = 0
  while v < 3 and msg == None:
    e.send(b'press')
    host, msg = e.irecv(5000)
    np_blink(yellow, 0.3, 3)
    v = v+1
  if msg:
    np_blink(green, 0.1, 4)
    gotosleep()
  else:
    np_blink(red, 0.3, 5)
    print('timeout error!!!!')
    gotosleep()






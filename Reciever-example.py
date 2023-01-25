import espnow
import network
import time
import machine


led = machine.Pin(15, machine.Pin.OUT) #board's internal LED
led.value(0) # Making sure it's closed by default

def led_blink(interval, nb): #internal led blink function
  for i in range(nb):
    led.value(1)
    time.sleep(interval)
    led.value(0)
    time.sleep(interval)

def msg_get(e): # function calledback when a message is sent
  host, msg = e.irecv()
  if msg == b'press':
    e.send(peer, b'pressed')
    led_blink(0.3,10)
  elif msg is not None:
    led_blink(1, 30)

# Wifi needs to be on in order to use ESPNow
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

e = espnow.ESPNow()
e.active(True)
peer = b"\x00\x00\x00\x00\x00\x0"  # Insert the sender's MAC address here
e.add_peer(peer)

while True:
  msg_get(e)


import time
import sys
from PN532 import PN532



def callbackPN532(tag, msg):
    print('Found tag: {}, msg: {}'.format(tag, msg))


# device uart, aid for android, callback
pn532 = PN532('tty:S0', 'A0000001020304', callbackPN532)

while True:
    listen = pn532.listen()
    if not listen:
        print("Waiting..")
        break

pn532.close()

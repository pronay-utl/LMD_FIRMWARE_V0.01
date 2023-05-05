from gpiozero import LED,MotionSensor
from gpiozero import Buzzer
from time import sleep
import requests
from PN532 import PN532
import json
import signal


#**************** NFC Callback ******************
def callbackPN532(tag, msg):
    print('Found tag: {}, msg: {}'.format(tag, msg))
    if msg :
        # msg["doorbell_id"]="100003"
        # msg["stream_url"]="https://oceloid-woodpecker-8595.dataplicity.io/stream.mp4"
        sleep(1)
        buzzer.off()
        pn532.close()
        r = requests.post(url, data=msg, headers=headers)
        print(r.json().get('message'))
        # red.off
        # stop_video()
    buzzer.off()
    red.off

#**************** NFC Initilize ******************
# Do not change the aid A0000001020304
# pn532 = PN532('tty:S0', 'A0000001020304', callbackPN532)
pn532 = PN532('tty:S0', 'A0000001020304', callbackPN532)

#**************** Sensors Initilize ******************
red = LED(18)
pir = MotionSensor(4)
buzzer = Buzzer(17)
url = 'https://kni6zyml9b.execute-api.us-east-1.amazonaws.com/DEV/web/doorbell/unsigned/bell-to-bell-cloud'
# Adding empty header as parameters are being sent in payload
headers = {
    "Content-Type":"application/json",
    "x-api-key":"caFG0mX4gjaLJGOWfTRLwVAyFPTqgt66uGfgtDd3"
}

#***************** Initiate pi Camera **************************
# camera=PiCamera()
#***************** Program Start **************************
print("Device is now running !!")
while True:
    if pir.motion_detected:
        print("Motion Detected")
        sleep(4)
        red.on
        buzzer.on()
        print(KeyboardInterrupt)
        # capture_video()
        print("Please tap your device to continue !")
        listen = pn532.listen()
    if buzzer.is_active:
        buzzer.off()
    sleep(2)
    

 
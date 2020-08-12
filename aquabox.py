#!/usr/bin/env python3

import sys, getopt
import RPi.GPIO as GPIO

def main(argv):
   relay_number = ''
   relay_state = ''
   try:
       opts, args = getopt.getopt(argv,"hdr:s:",["help","relay=", "state="])
   except getopt.GetoptError:
      help() 
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         help()
         sys.exit()
      elif opt in ("-r", "--relay"):
         relay_number = arg
      elif opt in ("-s", "--state"):
         relay_state = arg

   print( 'relay is: ', relay_number )
   print( 'state wanted is: ', relay_state )

   if relay_number != '' and relay_state != '':
       relay(relay_number, relay_state)
   else:
       help()

def help():
    print('aquabox.py -r <relay_number> -s <on|off>')

def relay(relay_number, relay_state):
    GPIO.setwarnings(False)

    relay_pin = ''

    if relay_number == str(1):
        relay_pin = 2
    else: 
        relay_pin = 3

    print( 'relay number is: ', relay_number )
    print( 'relay pin is: ', relay_pin )

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(relay_pin, GPIO.OUT)

    if relay_state == 'on':
        GPIO.output(relay_pin, GPIO.LOW)
    else:
        GPIO.output(relay_pin, GPIO.HIGH)
    #GPIO.cleanup()
    

if __name__ == "__main__":
   main(sys.argv[1:])

# src: https://tutorials-raspberrypi.com/raspberry-pi-control-relay-switch-via-gpio/

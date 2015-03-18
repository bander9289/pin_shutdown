def __main__():
  import RPi.GPIO as GPIO
  import time
  import os
  
  SHUTDOWN_GPIO = 18
  
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(SHUTDOWN_GPIO, GPIO.IN)
  
  while True:
      # block until a triggered to shutdown
      GPIO.wait_for_edge(SHUTDOWN_GPIO, GPIO.FALLING)
      
      # shutdown now! (about to lose power)
      if(GPIO.input(SHUTDOWN_GPIO) == False):
      	print "Shutdown pin event! Shutdown in ~20 seconds ...."
          os.system("sync")
  	time.sleep(20)
  
      	if(GPIO.input(SHUTDOWN_GPIO) == False):
              os.system("sync; poweroff")
              break;
  
  	print "Canceling shutdown since ignition is back on"

if __name__ == '__main__':
  __main__()

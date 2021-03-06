# Import required Python libraries
import RPi.GPIO as GPIO
import time
import smtplib
 
#GMAIL mail setup
TO = 'yourmail@gmail.com'
SUBJECT = 'PIR'
TEXT = 'Motion is detected'

#GMAIL user setup
gmail_sender = 'mymail@gmail.com'
gmail_passwd = 'mypwd'

#GMAIL stuff to login
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo
server.login(gmail_sender, gmail_passwd)

#GMAIL Message
BODY = '\r\n'.join([
       'TO: %s' % TO,
       'From: %s' % gmail_sender ,
       'Subject: %s' % SUBJECT ,
       '',
       TEXT
       ])

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
 
# Define GPIO to use on Pi
GPIO_PIR = 7
 
print "PIR Module Test (CTRL-C to exit)"
 
# Set pin as input
GPIO.setup(GPIO_PIR,GPIO.IN)      # Echo
 
Current_State  = 0
Previous_State = 0
 
try:
 
  print "Waiting for PIR to settle ..."
 
  # Loop until PIR output is 0
  while GPIO.input(GPIO_PIR)==1:
    Current_State  = 0
 
  print "  Ready"
 
  # Loop until users quits with CTRL-C
  while True :
 
    # Read PIR state
    Current_State = GPIO.input(GPIO_PIR)
 
    if Current_State==1 and Previous_State==0:
      # PIR is triggered
      print "  Motion detected!"
      #Send mail
      server.sendmail(gmail_sender, [TO], BODY)
      # Record previous state
      Previous_State=1
    elif Current_State==0 and Previous_State==1:
      # PIR has returned to ready state
      print "  Ready"
      Previous_State=0
 
    # Wait for 10 milliseconds
    time.sleep(0.01)
 
except KeyboardInterrupt:
  print "  Quit"
  # Reset GPIO settings
  GPIO.cleanup()
  server.quit()

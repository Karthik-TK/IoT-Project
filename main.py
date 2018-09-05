import sheetupdate
import serial
import spidev
import RPi.GPIO as GPIO
import I2C_LCD
import datetime
import os , time
import sys
import urllib2
from random import randint
from time import sleep
myAPI = "WZ88J29X01ELBIQK" 

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()
GPIO.setup(29, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.output(29,1)
GPIO.output(31,0)
GPIO.output(35,0)
mylcd = I2C_LCD.lcd()

port = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=1)

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000
 
# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data
 
# Function to convert data to voltage level,
# rounded to specified number of decimal places.
def ConvertVolts(data,places):
  volts = (data * 5.0) / float(1023)
  volts = round(volts,places)
  #print len(str(decimal.Decimal(volts))) 
  return volts
 
# Define sensor channels
PIR_channel = 0
GAS_SENSOR_channel  = 1
IR1_channel = 2
IR2_channel = 3
IR3_channel = 4
TEMP_channel = 5

def message():
    port.write('AT'+'\r')
    print "AT"
    rcv = port.read(10)
    print rcv
    time.sleep(1)

    port.write('ATE0'+'\r')      # Disable the Echo
    print "DISABLED ECHO"
    rcv = port.read(10)
    print rcv
    time.sleep(1)

    port.write('AT+CMGF=1'+'\r')  # Select Message format as Text mode
    print"MESSAGE ENABLED"
    cv = port.read(10)
    print rcv
    time.sleep(1)

    port.write('AT+CNMI=2,1,0,0,0'+'\r')   # New SMS Message Indications
    print "MESSAGE INDICATION"
    rcv = port.read(10)
    print rcv
    time.sleep(1)

# Sending a message to a particular Number

    port.write('AT+CMGS="1234567890"'+'\r')
    print "SENDING TO 1234567890"
    rcv = port.read(10)
    print rcv 
    time.sleep(1)

    port.write("EMERGENCY\r")  # Message
    print "MESSAGE SENT"
    rcv = port.read(10)
    print rcv 

    port.write("\x1A") # Enable to send SMS
    for i in range(10):
        rcv = port.read(10)
        print rcv
    print "COMPLETED"

global count

def testsheet():
        count=0
        baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI
	'''spreadsheetId = '1VeFwfXykn7ifa-i8ewEojLRDiZkREXNaLRRZMV2huEE'
	rangeName = 'A1:F'
	values = {'values':[['Time','PIR','GAS', 'IR1','IR2','IR3',TEMPERATURE],]}'''
	#mylcd.lcd_display_string("SENSOR DATA",1)
	#sheetupdate.update_authenticate(spreadsheetId, rangeName, values)
        delay = 1
	try:
            while True:
                for i in range(2,999):
                    
                    
                    
 # Read the PIR sensor data
                    PIR_level = ReadChannel(PIR_channel)
                    PIR_volts = ConvertVolts(PIR_level,2)
                #mylcd.lcd_display_string(PIR_volts,1)
                
# Read the GAS sensor data              
                    GAS_level = ReadChannel(GAS_SENSOR_channel)
                    GAS_volts = ConvertVolts(GAS_level,2)
                #mylcd.lcd_display_string(GAS_volts,1)
                
# Read the IR sensor data
                    IR1_level = ReadChannel(IR1_channel)
                    IR1_volts = ConvertVolts(IR1_level,2)
                #mylcd.lcd_display_string(IR_volts,1)
                    
                    IR2_level = ReadChannel(IR2_channel)
                    IR2_volts = ConvertVolts(IR2_level,2)
                    
                    IR3_level = ReadChannel(IR3_channel)
                    IR3_volts = ConvertVolts(IR3_level,2)
                    
                    TEMP_level = ReadChannel(TEMP_channel)
                    TEMP_volts = ConvertVolts(TEMP_level,2)
                    TEMP_deg = (TEMP_level*0.488)-55
 
                    '''myTS = '{:%H:%M:%S}'.format(datetime.datetime.now())
                    values = {'values':[[myTS, PIR_volts,GAS_volts,IR1_volts,IR2_volts,IR3_volts,TEMP_deg],]}
                    rangeName = 'A'+ str(i) + ':F'
            
                    sheetupdate.update_sheet(spreadsheetId, rangeName, values)'''

 
  # Print out results.
 
                    print "----------------------------------------------------"

                    mylcd.lcd_display_string("PIR VALUE       ",1) 
                    print("PIR : {} ({}V)".format(PIR_level,PIR_volts))
                    mylcd.lcd_display_string(str(PIR_volts),2)
                    time.sleep(delay)
 
                    mylcd.lcd_display_string("GAS VALUE      ",1) 
                    print("GAS SENSOR : {} ({}V)".format(GAS_level,GAS_volts))
                    mylcd.lcd_display_string(str(GAS_volts),2)
                    time.sleep(delay)
 
                    mylcd.lcd_display_string("IR1 VALUE      ",1) 
                    print("IR1 : {} ({}V)".format(IR1_level,IR1_volts))
                    mylcd.lcd_display_string(str(IR1_volts),2)
                    
                    mylcd.lcd_display_string("IR2 VALUE      ",1) 
                    print("IR2 : {} ({}V)".format(IR2_level,IR2_volts))
                    mylcd.lcd_display_string(str(IR2_volts),2)
                    
                    mylcd.lcd_display_string("IR3 VALUE      ",1) 
                    print("IR3 : {} ({}V)".format(IR3_level,IR3_volts))
                    mylcd.lcd_display_string(str(IR3_volts),2)
                    
                    mylcd.lcd_display_string("TEMPERATURE VALUE      ",1) 
                    print("TEMPERATURE : {} ({}V)".format(TEMP_deg,TEMP_volts))
                    mylcd.lcd_display_string(str(TEMP_deg),2)
                    
                    
            
                    f = urllib2.urlopen(baseURL + 
                               "&field1=%s&field2=%s&field3=%s&field4=%s&field5=%s&field6=%s"
                                        % (PIR_volts,GAS_volts,IR1_volts,IR2_volts,IR3_volts,TEMP_deg))  
                    #print f.read() 
                    f.close()
  # Wait before repeating loop
                    #time.sleep(delay)
                    if((PIR_volts >=4.0)):
                        print "PIR SENSOR crossed threshold"
                        GPIO.output(33,1)
                        mylcd.lcd_display_string("LIGHT ON          ",1)
##                        message()
                    else:
                        GPIO.output(33,0)
                    
                    if((GAS_volts >=3.0)):
                        print "GAS SENSOR crossed threshold"
                        mylcd.lcd_display_string("TOXIC GAS LEVEL   ",1)
##                        message()
                        
                    if((TEMP_volts >=3.0)):
                        print "TEMPERATURE SENSOR crossed threshold"
                        GPIO.OUTPUT(35,1)
                        mylcd.lcd_display_string("HIGH TEMPERATURE  ",1)
##                        message()
                    else:
                        GPIO.output(35,0)
                        

    

 
                    if(IR1_volts <=4.0):
                        
                        print "IR1 SENSOR crossed threshold"
                        GPIO.output(29,0)
                        GPIO.output(31,1)
                        mylcd.lcd_display_string("SLOT 1 OCCUPIED",2)
                        time.sleep(2)
                        mylcd.lcd_display_string("               ",2)
##                        message()
                        
                    else:
                        GPIO.output(29,1)
                        GPIO.output(31,0)
                        
                    if(IR2_volts <=4.0):
                        
                        print "IR2 SENSOR crossed threshold"
                        GPIO.output(29,0)
                        GPIO.output(31,1)
                        mylcd.lcd_display_string("SLOT 2 OCCUPIED",2)
                        time.sleep(2)
                        mylcd.lcd_display_string("               ",2)
##                        message()
                        
                    else:
                        GPIO.output(29,1)
                        GPIO.output(31,0)
                        
                    if(IR3_volts <=4.0):
                        
                        print "IR3 SENSOR crossed threshold"
                        GPIO.output(29,0)
                        GPIO.output(31,1)
                        mylcd.lcd_display_string("SLOT 3 OCCUPIED",2)
                        time.sleep(2)
                        mylcd.lcd_display_string("               ",2)
##                        message()
                        
                    else:
                        GPIO.output(29,1)
                        GPIO.output(31,0)    
                    
                    
                    time.sleep(1)
                       
                    
        	
	except KeyboardInterrupt:
            pass
 
 
if __name__ == '__main__':
	testsheet()

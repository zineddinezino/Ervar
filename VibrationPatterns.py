import pickle
from gpiozero import InputDevice, OutputDevice, PWMOutputDevice


# define the motors
M1 = PWMOutputDevice(13)
M2 = PWMOutputDevice(13)
M3 = PWMOutputDevice(13)
M4 = PWMOutputDevice(13)
M5 = PWMOutputDevice(13)
M6 = PWMOutputDevice(13)

def motor(id):
	M = None
	if(id == 1):
		M = M1
	elif(id == 2):
		M = M2
	elif(id == 3):
		M = M3
	elif(id == 4):
		M = M4
	elif(id == 5):
		M = M5
	elif(id == 6):
		M = M6
	return M

def turn_on_motor_one_by_one(id,duration):
	if(id == 1):
		M1.value = 0.5
		sleep(duration)
		M1.value = 0
	elif(id == 2):
		M2.value = 0.5
		sleep(duration)
		M2.value = 0
	elif(id == 3):
		M3.value = 0.5
		sleep(duration)
		M3.value = 0
	elif(id == 4):
		M4.value = 0.5
		sleep(duration)
		M4.value = 0
	elif(id == 5):
		M5.value = 0.5
		sleep(duration)
		M5.value = 0
	elif(id == 6):
		M6.value = 0.5
		sleep(duration)
		M6.value = 0

def turn_on_motors(ids,duration):
	M = None
	for i in ids:
		M = motor(i)
		M.value = 0.5

	sleep(duration)

	for i in ids:
		M = motor(i)
		M.value = 0

def search_pattern_by_name(name):
	inputFile = 'sound_patterns.data'
	fd = open(inputFile, 'rb')
	sound_patterns = pickle.load(fd)
	pattern_parameters = sound_patterns[name]
	return pattern_parameters

# {'name': ['pattern', 'type', 'frequency', 'session_duration']}
def run_pattern(pattern_parameters):

	pattern = [int(x) for x in str(pattern_parameters[0])]
	pattern_type = pattern_parameters[1]
	frequency = pattern_parameters[2]
	session_duration = pattern_parameters[3]
 
    if(pattern_type == 'parallel'):
    	while frequency >0:
    		turn_on_motors(pattern,session_duration)
    		frequency = frequency - 1
    elif(pattern_type == 'sequence' && pattern == [3,6,2,5,1,4]):
    	for i in pattern:
    		ids = [i, i+1] # the motors are running 2 by 2
    		turn_on_motors(ids,session_duration)
    		i = i + 2
    elif(pattern_type == 'sequence'):
    	for i in pattern:
    		turn_on_motor_one_by_one(i,session_duration)
    		
	
























































'''from bluedot.btcomm import BluetoothServer
from signal import pause
import RPi.GPIO as GPIO     # Import Library to access GPIO PIN
import time                 # To access delay function
GPIO.setwarnings(False)     # To avoid same PIN use warning
GPIO.setmode(GPIO.BOARD)    # Consider complete raspberry-pi board
LED_PIN_1 = 7                 # Define PIN for LED
LED_PIN_2 = 11                 # Define PIN for LED
IR_PIN = 13                 # Define PIN for IR Sensor
GPIO.setup(LED_PIN_1,GPIO.OUT)   # Set pin function as output
GPIO.setup(LED_PIN_2,GPIO.OUT)   # Set pin function as output
GPIO.setup(IR_PIN,GPIO.IN,pull_up_down=GPIO.PUD_UP)   # Set pin function as input
GPIO.output(LED_PIN_2,GPIO.HIGH)  #LED OFF
GPIO.output(LED_PIN_1,GPIO.HIGH)  #LED OFF
def data_received(data):
    print(data)
    if(data == "led1_ON"):
        GPIO.output(LED_PIN_1,GPIO.LOW)  #LED ON
    elif(data == "led1_OFF"):
        GPIO.output(LED_PIN_1,GPIO.HIGH)  #LED OFF
    elif(data == "led2_ON"):
        GPIO.output(LED_PIN_2,GPIO.LOW)  #LED ON
    elif(data == "led2_OFF"):
        GPIO.output(LED_PIN_2,GPIO.HIGH)  #LED OFF
    else:
        GPIO.output(LED_PIN_2,GPIO.HIGH)  #LED OFF
        GPIO.output(LED_PIN_1,GPIO.HIGH)  #LED OFF
        
s = BluetoothServer(data_received)  #Received data from bluetooth
while(1) :       
    if GPIO.input(IR_PIN) == GPIO.LOW:
        s.send("Obstacle Detected\n")
    else:
        s.send("Obstacle Does Not Detected\n")
pause()



################################### MQTT ################################
from time import sleep
import os,sys
import RPi.GPIO as GPIO
import paho.mqtt.client as paho
from six.moves.urllib.parse import urlparse
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
LED_PIN=11  #define LED pin
GPIO.setup(LED_PIN,GPIO.OUT)   # Set pin function as output

def on_connect(self, mosq, obj, rc):
        self.subscribe("led", 0)
    
def on_message(mosq, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    if(msg.payload == "on"):    
        print "LED on"      
        GPIO.output(LED_PIN,GPIO.HIGH)  #LED ON
    else:    
        print "LED off"
        GPIO.output(LED_PIN,GPIO.LOW)   # LED OFF

def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))

    
def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))



mqttc = paho.Client()                        # object declaration
# Assign event callbacks
mqttc.on_message = on_message                          # called as callback
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe


#url_str = os.environ.get('CLOUDMQTT_URL', 'tcp://broker.emqx.io:1883')                  # pass broker addr e.g. "tcp://iot.eclipse.org"
#url_str = os.environ.get('CLOUDMQTT_URL', 'tcp://broker.hivemq.com:1883')
url_str = os.environ.get('CLOUDMQTT_URL', 'tcp://broker.emqx.io:1883') 
url = urlparse.urlparse(url_str)
mqttc.connect(url.hostname, url.port)

rc = 0
while True:
    while rc == 0:
        import time   
        rc = mqttc.loop()
        #time.sleep(0.5)
    print("rc: " + str(rc))'''
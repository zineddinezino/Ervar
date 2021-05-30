from scipy.io.wavfile import write
from keras.utils import to_categorical
from tensorflow import keras
import sounddevice as sd
import numpy as np
from gpiozero import InputDevice, OutputDevice, PWMOutputDevice
from time import sleep, time
# Audio Real Time from the microphone
import pandas as pd
import librosa
#import noisereduce as nr
#from keras.models import load_model
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
import os
import pyaudio

from bluedot.btcomm import BluetoothServer

# MQTT
import paho.mqtt.client as paho
from six.moves.urllib.parse import urlparse
# end

# variable declaration for the model
num_rows = 40
num_columns = 174
num_channels = 1
max_pad_len = 174

import numpy as np

max_pad_len = 174

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 22050
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"
duration = 3

M1 = PWMOutputDevice(13)
Path_file = "/home/pi/Downloads/sounds for model testing purpose/siren.wav"
def extract_features(file_name):
    try:
        audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast')
        mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
        pad_width = max_pad_len - mfccs.shape[1]
        mfccs = np.pad(mfccs, pad_width=((0, 0), (0, pad_width)), mode='constant')

    except Exception as e:
        print("Error encountered while parsing file: ", file_name)
        return None

    return mfccs


def print_prediction(file_name):
    prediction_feature = extract_features(file_name)
    prediction_feature = prediction_feature.reshape(1, num_rows, num_columns, num_channels)
    
    predicted_vector = model.predict_classes(prediction_feature)
    predicted_class = le.inverse_transform(predicted_vector)
    return predicted_class[0]

        
def vibration_mapper(predicted_class):

    if(predicted_class == 'siren'):
        M1.value = 0.5
        sleep(2)
        M1.value = 0


def record_sound(indata, outdata, frames, time, status):
    fs = 22050  # Sample rate
    seconds = 3  # Duration of recording
    volume_norm = np.linalg.norm(indata)*10
    #print (int(volume_norm))
    if(int(volume_norm) >= 130):
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
        sd.wait()  # Wait until recording is finished
        write('output.wav', fs, myrecording)  # Save as WAV file
        predicted_class = print_prediction('output.wav')
        vibration_mapper(predicted_class)





featuresdf = pd.read_csv('/home/pi/Downloads/featuresdf.csv')
# Convert features and corresponding classification labels into numpy arrays

y = np.array(featuresdf.class_label.tolist())

# Encode the classification labels
le = LabelEncoder()
yy = to_categorical(le.fit_transform(y))


model = keras.models.load_model('/home/pi/Downloads/weights.best.basic_cnn.hdf5')
#print_prediction('WAV006.wav')

##################################################################### Main code(the app will start listing for sounds to record, if the mode is on) ###########################
'''
mode_indoor = True #this type of varibales should be listing alwayse to the incoming queries from the Flutter application

while(mode_indoor):
    sd.get_stream()
    with sd.Stream(callback=record_sound):
        sd.sleep(duration * 1000)'''
##################################################################### Main code ends ###########################    



# Record only relevent sounds
# Print out realtime audio volume as ascii bars







############################

#sd.get_stream()
#with sd.Stream(callback=print_sound):
#    sd.sleep(duration * 1000)

# MQTT
def on_connect(self, mosq, obj, rc):
    self.subscribe("sound", 0)

def on_message(mosq, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    if(msg.payload == b'siren'):
        print("Siren on")
        vibration_mapper('siren')
        
    elif(msg.payload == b'off'):
        break

def on_publish(mosq, obj, mid):
    print("mid: " +str(mid))

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))
    
mqttc = paho.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

url_str = os.environ.get('CLOUDMQTT_URL', 'tcp://broker.emqx.io:1883')
url = urlparse(url_str)
mqttc.connect(url.hostname, url.port)

rc = 0
while True:
    while rc == 0:
        rc = mqttc.loop()
    print("rc: " +str(rc))
# end


'''print("hello")
def data_received(data):
    print(data)
    if(data == "siren"):
        vibration_mapper(data)

#s = BluetoothServer(data_received)
print("hello")'''
#s.send("Done")
#predicted_class = print_prediction(Path_file)
#vibration_mapper(predicted_class)
############################################################################### Testing purpse only #############################################
# Loop predictions entre the file path or q to exit
'''while(True):
    
    path=input("Entre the path file or q to exit: ")
    if(path != 'q'):
        predicted_class = print_prediction(path)
        vibration_mapper(predicted_class)
    else:
        break'''
############################################################################### Testing purpse only #############################################


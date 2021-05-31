from scipy.io.wavfile import write
from keras.utils import to_categorical
from tensorflow import keras

import numpy as np
import vibrationPatterns
# Audio Real Time from the microphone
import pandas as pd
import librosa
#import noisereduce as nr
#from keras.models import load_model
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
import os
import pyaudio

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






class _Sound_Recognition_Service:
    featuresdf = None
    y = None
    le = None
    yy = None
    model = None


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
            pattern_parameters = VibrationPatterns.search_pattern_by_name(predicted_class)
            VibrationPatterns.run_pattern(pattern_parameters)





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





############################################################################### Testing purpse only #############################################
# Loop predictions entre the file path or q to exit
'''while(True):
    
    path=input("Entre the path file or q to exit: ")
    if(path != 'q'):
        print_prediction(path)
    else:
        break'''
############################################################################### Testing purpse only #############################################


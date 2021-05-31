import pickle

# {'name': ['pattern', 'type', 'frequency', 'session_duration']}
sound_patterns = {'siren': [1346, "parallel", 3, 2000],
             'car_horn': [14, "parallel", 1, 2000],
             'car_passing': [362514, "sequence", 1, 1000], # 1s for each 2 motors
             'baby_cry': [2536, "parallel", 1, 2000],
             'door_bell': [4, "parallel", 1, 2000],
             'phone_ring': [1, "parallel", 1, 2000],
             'smoke_alarm': [123456, "parallel", 1, 2000],
             'alarm_clock': [45, "parallel", 3, 2000],
		 'dog_bark': [1346, "parallel", 3, 2000],
             'drilling': [1346, "parallel", 3, 2000],
             'jackhammer': [1346, "parallel", 3, 2000],
             'air_conditioner': [1346, "parallel", 3, 2000],
             'children_playing': [1346, "parallel", 3, 2000],
             }


outputFile = 'sound_patterns.data'
fw = open(outputFile, 'wb')
pickle.dump(sound_patterns, fw)
fw.close()
import soundrecognitionController
import sounddevice as sd

if __name__ == "__main__":
    srs = soundrecognitionController()
    srs.featuresdf = pd.read_csv('featuresdf.csv')
	# Convert features and corresponding classification labels into numpy arrays
	srs.y = np.array(featuresdf.class_label.tolist())
	# Encode the classification labels
	srs.le = LabelEncoder()
	srs.yy = to_categorical(le.fit_transform(y))
	srs.model = keras.models.load_model('weights.best.basic_cnn.hdf5')

	sd.get_stream()
    with sd.Stream(callback=srs.record_sound):
        sd.sleep(duration * 1000)
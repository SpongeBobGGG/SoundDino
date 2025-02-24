import sounddevice as sd
import numpy as np
import librosa
from sklearn.linear_model import LogisticRegression
from joblib import dump, load
import threading
import time
import keyboard

def extract_features(audio, sample_rate):
    mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    mfccs_processed = np.mean(mfccs.T, axis=0)
    return mfccs_processed

model = LogisticRegression()
model = load('soundModel.joblib')

duration = 1/5  
sample_rate = 22050

laststat = 'background'
# Initialize keyboard controller from pynput

def press_key(key, duration=None):
    """Function to handle key press in a separate thread."""
    keyboard.press(key)
    if duration:
        time.sleep(duration)  # Hold the key for the specified duration
        keyboard.release(key)
    else:
        keyboard.release(key)

def callback(indata, frames, time, status):
    # Check for any errors during the audio capture
    if status:
        print("Error:", status)
    
    # Convert the incoming audio data to a 1D numpy array
    audio = indata[:, 0]
    
    # Extract features for the prediction model
    features = extract_features(audio, sample_rate)
    
    # Predict the command based on extracted features
    prediction = model.predict([features])
    print("Prediction result:", prediction)
    global laststat
    # Actions based on the prediction
    if prediction[0] == "up":
        if laststat == 'up' :
          threading.Thread(target=press_key, args=("up",)).start()
        laststat = 'up'

    elif prediction[0] == "down":
        if laststat == 'down' :
          threading.Thread(target=press_key, args=("down", 0.5)).start()
        laststat = 'down'

    else:
        laststat = 'background'

# Continuously record audio and process it in the callback
with sd.InputStream(callback=callback, dtype='float32', channels=1, samplerate=sample_rate, blocksize=int(sample_rate * duration), device=0):
    print("Starting real-time listening...")
    while True:
        time.sleep(0.2)  # Keep the main thread alive, allowing Ctrl+C to exit

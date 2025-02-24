import librosa
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from joblib import dump, load
from sklearn.metrics import accuracy_score
import os

# MFCC
def extract_features(file_path):
    audio, sample_rate = librosa.load(file_path, res_type='kaiser_fast')
    mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    mfccs_processed = np.mean(mfccs.T, axis=0)
    return mfccs_processed

def prepare_datasets(audio_dir):
    features = []
    labels = []
    for folder in os.listdir(audio_dir):
        label = folder
        folder_path = os.path.join(audio_dir, folder)
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            data = extract_features(file_path)
            features.append(data)
            labels.append(label)

    print(labels)
    return features, labels

audio_directory = 'samples'
features, labels = prepare_datasets(audio_directory)
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(features_train, labels_train)

predictions = model.predict(features_test)
accuracy = accuracy_score(labels_test, predictions)
print(f'Model Accuracy: {accuracy:.2f}')

model_filename = 'soundModel.joblib'
dump(model, model_filename)

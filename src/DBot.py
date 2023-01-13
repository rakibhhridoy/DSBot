import pyaudio
from vosk import Model, KaldiRecognizer

model_file = r"/home/RHHLab/vosk-model-en-us-0.22"
channels = 1
rate = 16000
framesPerBuffer = 8192

model = Model(model_file)
recognizer = KaldiRecognizer(model, rate)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, rate= rate, channels= channels, frames_per_buffer= framesPerBuffer, input=True)
stream.start_stream()


while True:
    data = stream.read(4096)
    if recognizer.AcceptWaveform(data):
        text = recognizer.Result()
        print(text[14:-3])
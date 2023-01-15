import pyaudio
from vosk import Model, KaldiRecognizer
from collections import OrderedDict

model_file = r"/home/RHHLab/voskModels/vosk-model-en-us-0.22"
model_file_s = r"/home/RHHLab/voskModels/vosk-model-small-en-us-0.15"
model_file_lg = r"/home/RHHLab/voskModels/vosk-model-en-us-0.22-lgraph"
channels = 1
rate = 16000
framesPerBuffer = 8192



def listening():
    model = Model(model_file_lg)
    recognizer = KaldiRecognizer(model, rate)

    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, rate= rate, channels= channels, frames_per_buffer= framesPerBuffer, input=True)
    stream.start_stream()


    while True:
        data = stream.read(4096)
        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()
            strip_duplicates(text[14:-3])
            
            
def strip_duplicates(text):
    
#    text = OrderedDict().fromkeys(text.split())
#    text = ' '.join(text)

    if text.startswith("the") or text.endswith("the"):
        if text.startswith("the"):
            text = text.removeprefix("the")
        else:
            text = text.removesuffix("the")
    
        
    print(text)
    
        
    
listening()
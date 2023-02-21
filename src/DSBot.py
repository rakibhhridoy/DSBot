import pyaudio
from vosk import Model, KaldiRecognizer
from collections import OrderedDict
from createf import creating, deleting
from apps import Command

model_file = r"/home/RHHLab/voskModels/vosk-model-en-us-0.22"
model_file_s = r"/home/RHHLab/voskModels/vosk-model-small-en-us-0.15"
model_file_lg = r"/home/RHHLab/voskModels/vosk-model-en-us-0.22-lgraph"


class Bot:
    def __init__(self, model_file):
        
        self._channel = 1
        self._rate = 16000
        self._framesPerBuffer = 8192
        self._voice = None
        self._audiolist = None
        
        self._model = Model(model_file)
        self._recognizer = KaldiRecognizer(self._model, self._rate)


        self._directory = ["folder", "directory"]
        self._file = "file"
        self._deletion = ["delete", "remove", "exclude"]
        self._creation = ["create", "add", "include"]


    def listening(self):

        mic = pyaudio.PyAudio()
        stream = mic.open(format=pyaudio.paInt16, rate= self._rate, channels= self._channel, frames_per_buffer= self._framesPerBuffer, input=True)
        stream.start_stream()


        while True:
            data = stream.read(4096)
            if self._recognizer.AcceptWaveform(data):
                self._voice = self._recognizer.Result()
                self._voice = self.strip_the(self._voice[14:-3])
                print(self._voice)
                self._audiolist = self._voice.split(" ")
                folderorfile = self._audiolist.pop()
            
                if bool(set(self._audiolist).intersection(self._creation)):
                    creating(self._audiolist, folderorfile, self._directory,self._file)
                if bool(set(self._audiolist).intersection(self._deletion)):
                    deleting(self._audiolist, folderorfile, self._directory, self._file)
                
                Command.apps_open()
                
    def strip_the(self, text):
        if text.startswith("the") or text.endswith("the"):
            if text.startswith("the"):
                text = text.removeprefix("the")
            else:
                text = text.removesuffix("the")
        return text
    


bot = Bot(model_file_lg)
bot.listening()

    

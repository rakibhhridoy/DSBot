import os
from DSBot import Bot


class Command(Bot):
    def __init__(self):
        self._applist = self.appList("files/applist.txt")

    def appList(self, file):
        with open(file) as f:
            name_list = [line.rstrip() for line in f]
        return name_list
        

    def match(self, str1, str2):
        pass

    def apps_open(self):
        def jupyter(self):
            if "notebook" in self._voice:
                os.system("jupyter-notebook")
            
            elif "lab" in self._voice:
                os.system("jupyter-lab")

        def anaconda(self):
            if "anaconda" in self._voice:
                os.system("anaconda-navigator")
            elif "spyder" in self._voice:
                os.system("spyder")

        def youtube(self):
            if "youtube" in self._voice:
                os.system("/opt/brave.com/brave/brave-browser --profile-directory=Default --app-id=agimnkijcaahngcdmfeangaknmldooml")
        
        jupyter()
        anaconda()
        youtube()


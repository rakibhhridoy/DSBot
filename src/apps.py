import os

def jupyter():
    if "notebook" in value:
        os.system("jupyter-notebook")
    
    elif "lab" in value:
        os.system("jupyter-lab")

def anaconda():
    if "anaconda" in value:
        os.system("anaconda-navigator")
    elif "spyder" in value:
        os.system("spyder")

def youtube():
    if len(value) < 14:
        os.system("/opt/brave.com/brave/brave-browser --profile-directory=Default --app-id=agimnkijcaahngcdmfeangaknmldooml")
    


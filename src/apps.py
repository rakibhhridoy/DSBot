import os
#from DSBot import Bot


def appList(file):
    with open(file) as f:
        name_list = [line.rstrip() for line in f]
    print(name_list)
        


def match(str1, str2):
    pass

appList("files/applist.txt")

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
    


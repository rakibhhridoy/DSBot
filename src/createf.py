import os

def creating(audio):
    directory = ["folder", "directory"]
    file = "file"
    audiolist = audio.split(" ")
    folderorfile = audiolist.pop()

    if directory in audio:
        os.system("mkdir {}".format(folderorfile))

    elif file in audio:
        os.system("touch {}".format(folderorfile))
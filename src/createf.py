import os

def creating(audio, folderorfile, directory, file):
    
    
    if audio in directory:
        print("Creating directory {}".format(folderorfile))
        os.system("mkdir {}".format(folderorfile))
        print("Success!, {} directory created!".format(folderorfile))

    elif file in audio:
        print("Creating file {}".format(folderorfile))
        os.system("touch {}".format(folderorfile))
        print("Success!, {} file created!".format(folderorfile))


def deleting(audio, folderorfile, directory, file):
    
    if audio in directory:
        os.system("rm -r {}".format(folderorfile))
        print("Success!, {} directory deleted!".format(folderorfile))
        
    elif file in audio:
        os.system("rm -r {}".format(folderorfile))
        print("Success!, {} file deleted!".format(folderorfile))
        
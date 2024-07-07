import datetime

def GetNewName(pathToFolder: str, extension: str):

    now = datetime.datetime.now()

    strCurrentDate = now.strftime('%m-%d-%Y_%H-%M-%S')
     
    return pathToFolder + "/" + strCurrentDate + "." + extension
import datetime

def CreateNewNameFile(pathToFolder: str, prefix: str, extension: str):

    now = datetime.datetime.now()

    strCurrentDate = now.strftime('%m-%d-%Y_%H-%M-%S')
     
    return pathToFolder + "/" + prefix + "_" + strCurrentDate + "." + extension
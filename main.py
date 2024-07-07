from src.name_creator import *
from src.video_recorder import *

nameFile = GetNewName("video", "avi")
VideoRecord(24.0, (1920, 1080) , nameFile)

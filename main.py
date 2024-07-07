from src.name_creator import *
from src.video_recorder import *
from src.crop_video import *

nameFile = GetNewName("video", "avi")
VideoRecord(24.0, (1920, 1080) , nameFile)

resultFile = "video/result.avi"
CropVideo(nameFile, resultFile, 800, 1200)

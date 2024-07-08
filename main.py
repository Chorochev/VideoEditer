from src.name_creator import *
from src.video_recorder import *
from src.crop_video import *
from src.slow_down_video import *
import src.arguments as commands

commands.init()

if(commands.args.record):   
    #nameFile = GetNewName("video", "avi")
    nameFile = "video/" + commands.args.inFile + ".avi"
    VideoRecord(24.0, (1920, 1080) , nameFile)

if(commands.args.crop):
    outFile = "video/" + commands.args.outFile + ".avi"
    resultFile = "video/" + commands.args.inFile + ".avi"
    x1 = commands.args.x
    y1 = commands.args.y
    xRatio = commands.args.wd
    yRatio = commands.args.ht
    CropVideo(outFile, resultFile, x1, y1, x1 + xRatio, y1 + yRatio)

if(commands.args.slowDown):    
    outFile = "video/" + commands.args.outFile + ".avi"
    resultFile = "video/" + commands.args.inFile + ".avi"
    speedRatio = commands.args.speedRatio
    SlowDownVideo(outFile, resultFile, speedRatio)

import src.arguments as commands
from src.name_creator import GetNewName
from src.video_recorder import VideoRecord
from src.crop_video import CropVideo
from src.slow_down_video import SlowDownVideo
from src.title_screen import AddTitle
from src.fade_effect import AddFadeEffect
from src.subclip import SubClip
from src.join_videoclips import JoinVideClips

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

if(commands.args.addTitle):
    caption = commands.args.caption
    outFile = "video/" + commands.args.outFile + ".avi"
    resultFile = "video/" + commands.args.inFile + ".avi"
    AddTitle(caption, outFile, resultFile)

if(commands.args.addFade):    
    outFile = "video/" + commands.args.outFile + ".avi"
    resultFile = "video/" + commands.args.inFile + ".avi"
    duration = commands.args.duration
    AddFadeEffect(outFile, resultFile, duration)

if(commands.args.subClip):
    outFile = "video/" + commands.args.outFile + ".avi"
    resultFile = "video/" + commands.args.inFile + ".avi"
    start = commands.args.start
    end = commands.args.end
    SubClip(outFile, resultFile, start, end)

if(commands.args.joinClips):
    name = commands.args.name
    count = commands.args.count
    resultFile = "video/" + commands.args.inFile + ".avi"    
    JoinVideClips(name, count, resultFile)

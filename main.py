import src.arguments as commands
from src.video_recorder import VideoRecord
from src.crop_video import CropVideo
from src.slow_down_video import SlowDownVideo
from src.title_screen import AddTitle
from src.fade_effect import AddFadeEffect
from src.subclip import SubClip
from src.join_videoclips import JoinVideClips
from src.change_speed import ChangeSpeedVideo

commands.init()

outFile = commands.GetOutFileName()
resultFile = commands.GetInFileName()

if(commands.args.record):      
    nameFile = commands.GetNameRecordFile("record")
    fps = commands.args.fps
    widthSCR = commands.args.widthSCR
    heightSCR = commands.args.heightSCR
    VideoRecord(fps, (widthSCR, heightSCR) , nameFile)

if(commands.args.crop):  
    x1 = commands.args.x
    y1 = commands.args.y
    xRatio = commands.args.wd
    yRatio = commands.args.ht
    CropVideo(outFile, resultFile, x1, y1, x1 + xRatio, y1 + yRatio)

if(commands.args.slowDown):        
    speedRatio = commands.args.speedRatio
    SlowDownVideo(outFile, resultFile, speedRatio)

if(commands.args.addTitle):
    caption = commands.args.caption   
    AddTitle(caption, outFile, resultFile)

if(commands.args.addFade): 
    duration = commands.args.duration
    AddFadeEffect(outFile, resultFile, duration)

if(commands.args.subClip):    
    start = commands.args.start
    end = commands.args.end
    SubClip(outFile, resultFile, start, end)

if(commands.args.joinClips):
    name = commands.args.name
    count = commands.args.count    
    JoinVideClips(name, count, resultFile)

if not (commands.args.speed is None):
    speed = commands.args.speed
    ChangeSpeedVideo(outFile, resultFile, 0.5)

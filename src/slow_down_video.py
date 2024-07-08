from moviepy.editor import VideoFileClip
import moviepy.video.fx.all as vfx

def SlowDownVideo(fromfileName: str,
                  toFileName: str,
                  speedRatio: any):
   
    clip = VideoFileClip(fromfileName)  
    clip = clip.set_fps(clip.fps * speedRatio)
    modifiedClip = clip.fx(vfx.speedx, speedRatio)    
    modifiedClip.write_videofile(toFileName, fps=24, threads=1, codec="libx264")
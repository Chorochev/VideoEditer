import moviepy.editor as mpy

def ChangeSpeedVideo(fromfileName: str, 
              toFileName: str,
              speed: any):

    clip = mpy.VideoFileClip(fromfileName)
       
    clip.speedx(speed).write_videofile(toFileName, fps=24, threads=1, codec="libx264")

import moviepy.editor as mpy
from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"})


def AddFadeEffect(fromfileName: str, 
                  toFileName: str,
                  duration: any):

    # Get clip
    clip = mpy.VideoFileClip(fromfileName).fadein(duration).fadeout(duration)
    
    clip.write_videofile(toFileName, fps=24, threads=1, codec="libx264")
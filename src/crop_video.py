import moviepy.editor as mpy
from moviepy.video.fx.all import crop

def CropVideo(fromfileName: str, 
              toFileName: str,
              _x1: any,
              _y1: any,
              _x2: any,
              _y2: any):

    clip = mpy.VideoFileClip(fromfileName)
    #(w, h) = clip.size
    # cropped_clip = crop(clip, width=320, height=320, x_center=w/2, y_center=h/2)
    cropped_clip = crop(clip, x1=_x1, y1=_y1, x2=_x2, y2=_y2)
    cropped_clip.write_videofile(toFileName, fps=24, threads=1, codec="libx264")

import moviepy.editor as mpy
from moviepy.video.fx.all import crop

def CropVideo(fromfileName: str, 
              toFileName: str,
              width: any,
              height: any):

    clip = mpy.VideoFileClip(fromfileName)
    #(w, h) = clip.size
    # cropped_clip = crop(clip, width=320, height=320, x_center=w/2, y_center=h/2)
    cropped_clip = crop(clip, x1=0, y1=0, x2=width, y2=height)
    cropped_clip.write_videofile(toFileName, fps=10, threads=1, codec="libx264")

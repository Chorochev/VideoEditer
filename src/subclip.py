import moviepy.editor as mpy
 
def SubClip(fromfileName: str, 
            toFileName: str,
            start: any,
            end: any):
   
    clip = mpy.VideoFileClip(fromfileName)
 
    clip = clip.subclip(start, end)
 
    clip.write_videofile(toFileName, fps=24, threads=1, codec="libx264")
    
import moviepy.editor as mpy
from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"})

def AddTitle(caption: str,
             fromfileName: str, 
             toFileName: str):

    # Get clip
    clip = mpy.VideoFileClip(fromfileName)

    edited_right = clip.subclip(0, 2.5)
    edited_right = mpy.vfx.fadein(edited_right, duration=2.5)

    # MAKE THE TITLE SCREEN
    titleStr = "SQL\nEXAMPLES\n\n\n" + caption

    txt_title = (mpy.TextClip(titleStr, fontsize=46,
                 font="Arrow", color="white") #, bg_color="black")
                 .margin(top=15, opacity=0)
                 .set_position(("center","top")))

    title = (mpy.CompositeVideoClip([edited_right, txt_title])
            .set_duration(2.5).fadein(.5).fadeout(.5))   

    # MAKE THE CREDITS SCREEN
    txt_credits = "Thanks\nfor\nwatching"
    credits = (mpy.TextClip(txt_credits, color='white',
                font="Arrow", fontsize=46, kerning=-2,
                interline=-1, bg_color='black', size=title.size)
                .set_duration(3)
                .fadein(.5)
                .fadeout(.5))
    
    # ASSEMBLE EVERYTHING, WRITE TO FILE
    final = mpy.concatenate_videoclips([title, clip, credits])
    final.write_videofile(toFileName, fps=24, threads=1, codec="libx264")
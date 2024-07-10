import moviepy.editor as mpy

def JoinVideClips(name: str,
                  count: int,
                  toFileName: str):
    
    clips = []

    for n in range(1, count+1):
        fileName = "video/" + name + str(n) + ".avi"
        clip = mpy.VideoFileClip(fileName)
        clips.append(clip)

    concat_clip = mpy.concatenate_videoclips(clips, method="compose")
    concat_clip.write_videofile(toFileName, fps=24, threads=1, codec="libx264")

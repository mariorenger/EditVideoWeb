#from tinkerer import *
from moviepy.editor import *

# clip1 = VideoFileClip("/home/trannguyenhan/Videos/untitled.mp4")
# clip2 = VideoFileClip("/home/trannguyenhan/Videos/dichvucong.mp4")

# desc : function is merge multi video 
# clips: array
# path : string
def mix(clips, path):
    final_video = concatenate_videoclips(clips)
    final_video.write_videofile(path)

# desc : function is mirror one video
# clip: VideoFileClip
# path : string
def mirror(clip, path):
    final_video = clip.fx(vfx.mirror_x)
    final_video.write_videofile(path)


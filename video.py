from moviepy.editor import *

class Video: 
    def __init__(self, starttime, endtime, path_video):
        self.starttime = starttime
        self.endtime = endtime
        
        # fix after: instead try catch with other methods
        try: 
            self.video = VideoFileClip(path_video)
        except ValueError: 
            self.video = None

    # create video from Video object
    # with start time is startime param
    # end time is endtime param
    def finish_video(self): 
        if self.video: 
            result = self.video.subclip(self.starttime, self.endtime)
            return result
        
        return None
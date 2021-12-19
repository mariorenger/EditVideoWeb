from moviepy.editor import *
from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": "/usr/local/bin/convert"})

class Video: 
    def __init__(self, starttime, endtime, path_video, volume, tracks):
        self.starttime = starttime
        self.endtime = endtime
        self.volume = volume
        self.tracks = tracks

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
            result = self.video.subclip(self.starttime, self.endtime).volumex(self.volume / 50)
        
            # subs = []

            # add track for video
            # if self.tracks: 
            #     for track in self.tracks: 
            #         endTime = track['endTime']
            #         startTime = track['startTime']
            #         text = str(track['text'])
                    
            #         textClip = TextClip(text, fontsize=30, color='red').set_position('bottom', 'center').set_duration(endTime-startTime)
            #         # result = CompositeVideoClip([result, textClip])
                
            return result
        
        return None
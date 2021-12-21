from moviepy.editor import *
from models.track import Track

class Video: 
    def __init__(self, starttime, endtime, path_video, volume, tracks):
        self._starttime = starttime
        self._endtime = endtime
        self._volume = volume
        self._tracks = []

        for item in tracks: 
            starttime = item['startTime']
            endtime = item['endTime']
            duration = endtime - starttime
            text = str(item['text'])

            track = Track(starttime, duration, text)
            self._tracks.append(track)

        # fix after: instead try catch with other methods
        try: 
            self._video = VideoFileClip(path_video)
        except ValueError: 
            self._video = None

    # create video from Video object
    # with start time is startime param
    # end time is endtime param
    def finish_video(self): 
        if self._video: 
            result = self._video.subclip(self._starttime, self._endtime).volumex(self._volume / 50)
            
            subs = []
            # add track for video
            if len(self._tracks) != 0: 
                for track in self._tracks: 
                    starttime = track.get_starttime()
                    duration = track.get_duration()
                    text = str(track.get_text())
                    
                    # text_clip = TextClip(text, fontsize=30, color='red').set_position('bottom', 'center').set_duration(duration)
                    # result = CompositeVideoClip([result, text_clip])
                    print(starttime)
                    print(duration)
                    print(text)
                
            return result
        
        return None
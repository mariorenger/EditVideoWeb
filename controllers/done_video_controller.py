from models.video import *
import helper_video

class DoneVideoController: 
    def __init__(self, data, volume):
        self._data = data
        self._volume = volume

    def get(self):
        print(self._data)
        videopys = []
        for item in self._data: 
            st = float(item['startTime'])
            et = float(item['endTime'])
            path = item['pathVideo'].replace("http://127.0.0.1:5000/", "") # remove protocol and get relative path of video
            tracks = item['track']
			
            video = Video(st, et, path, self._volume, tracks)
            videopy = video.finish_video()
            videopys.append(videopy)
		
        helper_video.mix(videopys, 'static/resources/result.mp4')

        return "True"

    def post(self):
        return self.get()
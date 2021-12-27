class Track:
    def __init__(self,starttime, duration, text):
        self._starttime = starttime
        self._duration = duration
        self._text = text
    
    def get_starttime(self):
        return self._starttime

    def get_duration(self):
        return self._duration

    def get_text(self):
        return self._text
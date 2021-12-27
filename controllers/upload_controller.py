import os
import helper

class UploadController: 
    def __init__(self, file, path):
        self._file = file
        self._path = path

    def get(self): 
        helper.create_new_folder(self._path)
        saved = os.path.join(self._path, self._file.filename)
        self._file.save(saved)

        return "True"
    
    def post(self):
        return self.get()

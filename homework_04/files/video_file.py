import datetime
from files.base_file import BaseFile

class VideoFile(BaseFile):
    def __init__(self, name: str, size: int, date: datetime.datetime, owner: str, duration: int, resolution: str):
        super().__init__(name, size, date, owner)
        self.duration = duration
        self.resolution = resolution
    
    def __str__(self):
        
        return f"{super().__str__()}, duration: {self.duration} seconds, resolution: {self.resolution})"
    
    def __repr__(self):
        return f"Video{super.__repr__()}, duration={self.duration} sec, resolution={self.resolution})"
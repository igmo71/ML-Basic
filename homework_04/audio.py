import datetime
from base import BaseFile

class AudioFile(BaseFile):
    def __init__(self, name: str, size: int, date: datetime.datetime, owner: str, duration: int):
        super().__init__(name, size, date, owner)
        self.duration = duration
    
    def __str__(self):
        return f"{super().__str__()}, duration: {self.duration} seconds)"
    
    def __repr__(self):
        return f"Audio{super.__repr__()}, duration={self.duration} sec)"
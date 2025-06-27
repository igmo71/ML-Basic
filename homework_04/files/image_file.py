import datetime
from files.base_file import BaseFile

class ImageFile(BaseFile):
    def __init__(self, name: str, size: int, date: datetime.datetime, owner: str, dimensions: str):
        super().__init__(name, size, date, owner)
        self.dimensions = dimensions
    
    def __str__(self):
        return f"{super().__str__()}, dimensions: {self.dimensions})"
    
    def __repr__(self):
        return f"Image{super.__repr__()}, dimensions={self.dimensions})"
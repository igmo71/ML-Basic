import datetime

class BaseFile:
    def __init__(self, name: str, size: int, date: datetime.datetime, owner: str):
        self.name = name
        self.size = size
        self.date = date
        self.owner = owner
    
    def __str__(self):
        return f"{self.name} ({self.size} bytes, {self.date}, owned by {self.owner})"
    
    def __repr__(self):
        return f"File(name={self.name}, size={self.size}, date={self.date}, owner={self.owner})"
    
    def __eq__(self, other):
        if not isinstance(other, BaseFile):
            return NotImplemented
        return self.name == other.name and self.size == other.size and self.date == other.date and self.owner == other.owner
    
    def __lt__(self, other):
        if not isinstance(other, BaseFile):
            return NotImplemented
        return self.size < other.size
    
    def create(self):
        # Simulate file creation
        print(f"Creating file: {self.name}")
        return self
    
    def delete(self):
        # Simulate file deletion
        print(f"Deleting file: {self.name}")
        return self
    
    def move(self, new_location: str):
        # Simulate file moving
        print(f"Moving file {self.name} to {new_location}")
        return self
    
    def copy(self, new_location: str):
        # Simulate file copying
        print(f"Copying file {self.name} to {new_location}")
        return self
    
    def rename(self, new_name: str):
        # Simulate file renaming
        print(f"Renaming file {self.name} to {new_name}")
        self.name = new_name
        return self
    
    def open(self):
        # Simulate file opening
        print(f"Opening file: {self.name}")
        return self
    
    def close(self):
        # Simulate file closing
        print(f"Closing file: {self.name}")
        return self
    
    def convert(self, new_format: str):
        # Simulate file conversion
        print(f"Converting file {self.name} to {new_format}")
        return self

class AudioFile(BaseFile):
    def __init__(self, name: str, size: int, date: datetime.datetime, owner: str, duration: int):
        super().__init__(name, size, date, owner)
        self.duration = duration
    
    def __str__(self):
        return f"{super().__str__()}, duration: {self.duration} seconds)"
    
    def __repr__(self):
        return f"Audio{super.__repr__()}, duration={self.duration} sec)"
import datetime
from files.audio_file import AudioFile
from files.video_file import VideoFile
from files.image_file import ImageFile

my_audiofile = AudioFile("song.mp3", 35000, datetime.datetime.now(), "user", 240)
my_video_file = VideoFile("movie.mp4", 150000, datetime.datetime.now(), "user", 7200, "1920x1080")
my_image_file = ImageFile("image.jpg", 5000, datetime.datetime.now(), "user", "1920x1080")

print("Audio file details:")
print(my_audiofile)
print("Video file details:")
print(my_video_file)
print("Image file details:")
print(my_image_file)

my_audiofile.create()
my_audiofile.open()
my_audiofile.close()
my_audiofile.rename("new_song.mp3")
my_audiofile.convert("wav")
my_audiofile.move("/new/location")
my_audiofile.delete()


my_audiofile2 = AudioFile("song2.mp3", 15000, datetime.datetime.now(), "user", 240)

print(f"Is my_audiofile > my_audiofile2: {my_audiofile > my_audiofile2}")

my_audiofiles = [AudioFile("song3.mp3", 25000, datetime.datetime.now(), "user", 240), my_audiofile, my_audiofile2]

my_audiofiles.sort()
print("Sorted audio files by size:")
for audio_file in my_audiofiles:
    print(audio_file.name)


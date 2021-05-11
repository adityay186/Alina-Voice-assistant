from playsound import playsound
import os
from os import walk

class Music:

    def getMusicList(self):
        f = []
        for (dirpath, dirnames, filenames) in walk("Music"):
            f.extend(filenames)
            break
        return f

    def main(self):
        pl="Sounds/AlrightPlaying-songs-from-you1620591136.mp3"
        os.system("play "+pl+" tempo 1.1")
        for i in range(len(self.getMusicList())):
            ns="Sounds/Playing-next-song1620591529.mp3"
            os.system("play "+ns+" tempo 1.1")
            pl="Music/"+self.getMusicList()[i]
            os.system("play "+pl+" tempo 1.0")
        hyej="Sounds/Your-playlist-was-awesomeI-ho1620591820.mp3"
        os.system("play "+hyej+" tempo 1.1")
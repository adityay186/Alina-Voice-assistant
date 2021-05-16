from playsound import playsound
import multiprocessing
import time

def foo():
    while True:
        url = 'https://radioindia.net/radio/vividhbharti/icecast.audio'
        playsound(url)

def radio_play():
    p = multiprocessing.Process(target=foo, name="Foo")
    p.start()
    time.sleep(20)
    p.terminate()
    p.join()

radio_play()
import itertools
import threading
import time
import sys

done = False
#here is the animation
def animate_monitor():
    for c in itertools.cycle(["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]):
        if done:
            break
        sys.stdout.write('\rMonitoring Home ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')

def animate_music():
    for c in itertools.cycle(["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]):
        if done:
            break
        sys.stdout.write('\rPlaying Music ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')

def music():
    t = threading.Thread(target=animate)
    t.start()
    for i in range(5):
        time.sleep(1)
        print("hello")
    done=True
#long process here
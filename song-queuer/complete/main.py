import time
import myqueue
import song
import os

def play_songs(song_queue):
    """
    When given a Queue of songs (see implementation
    of Queue in `myqueue.py`), plays all of the songs
    in first-in-first-out order.

    Ex: `Song A` is queued, and then `Song B` is queued.
        This should play `Song A` and THEN `Song B`, not
        the other way around.
    """
    print("SONGBOT v1.0 | Songs playing...")
    while not song_queue.is_empty():
        current_song = song_queue.dequeue()
        current_song.play_song()
        time.sleep(current_song.length)
    print("SONGBOT v1.0 | Songs done playing!\n")

# Now, you have to write some code that parses through 
# all songs in `songs.txt` and calls `play_songs()` on 
# each evaluated line.
#
# Every line is formatted in this way:
# [songnames]|[songtimes]
#
# [songnames] are strings and [songtimes] are floats, 
# both separated by commas (,).

cases = open(os.path.dirname(__file__) + "/../songs.txt")
for s in cases.readlines():
    s = s.strip().split("|")
    song_queue = myqueue.Queue()
    song_names = s[0].split(",")
    song_lengths = s[1].split(",")
    for i in range(len(song_names)):
        curr_song = song.Song(song_names[i], float(song_lengths[i]))
        song_queue.enqueue(curr_song)
    play_songs(song_queue)
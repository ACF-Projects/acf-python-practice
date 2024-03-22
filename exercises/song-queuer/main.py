import time

"""
Here, your task is to write code that mimics a playlist
that plays songs in order! You must wait for songs to
finish playing before going to the next song, until
the playlist eventually plays all queued songs.

To do this, it's a simple step-by-step process. First,
you must parse through information in a text file 
(see `songs.txt`), create Song() classes out of each
(see `song.py`), and call `play_songs()` on each one.

In `songs.txt`, every line is formatted in this way:
[songnames]|[songtimes]

[songnames] are strings and [songtimes] are floats, 
both separated by commas (,). Check `songs.txt` out!

If there are any questions about this
assignment, feel free to ask questions!
"""

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
        current_song = song_queue.pop()
        current_song.play_song()
        time.sleep(current_song.length)
    print("SONGBOT v1.0 | Songs done playing!\n")

# As practice, try to write code that creates a Queue. 
# Then, put a few self-created songs inside. 
# (Think: how do you create a new Song?)
# Then, call the `play_songs` function on the queue.



# Below, write the code that plays through the songs in
# `songs.txt`. See more in the large comment above!

cases = open("songs.txt")
for s in cases.readlines():
    s = s.strip().split("|")
    # Your code here (print statement is a placeholder)
    print(s) 
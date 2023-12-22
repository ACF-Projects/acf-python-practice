class Song:
    
    def __init__(self, song_name, song_length):
        """
        Initializes a new Song object that stores
        a string `song_name` (carries name of the
        song) and float `song_length` (length of
        the song in seconds).
        """
        self.title = song_name
        self.length = song_length

    def play_song(self):
        """
        Prints out a string that says that this
        song is currently playing.

        Of course, in an actual application, we may
        want this to play actual music.
        """
        print("Playing " + self.title + " (" + str(self.length) + "s)")
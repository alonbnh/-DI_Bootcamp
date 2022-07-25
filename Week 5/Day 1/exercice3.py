class song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_song(self):
        for elem in self.lyrics:
            print (elem)

stairway= song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"]) 
stairway.sing_me_song()
 
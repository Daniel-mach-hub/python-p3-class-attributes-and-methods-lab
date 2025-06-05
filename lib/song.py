class Song:
    # Class attributes
    count = 0
    artists = []
    genres = []
    artist_count = {}
    genre_count = {}

    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update class-level data on song creation
        self.add_song_to_count()
        self.add_to_artists()
        self.add_to_genres()
        self.add_to_artist_count()
        self.add_to_genre_count()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_artists(cls):
        if cls.__current_artist not in cls.artists:
            cls.artists.append(cls.__current_artist)

    @classmethod
    def add_to_genres(cls):
        if cls.__current_genre not in cls.genres:
            cls.genres.append(cls.__current_genre)

    @classmethod
    def add_to_artist_count(cls):
        if cls.__current_artist in cls.artist_count:
            cls.artist_count[cls.__current_artist] += 1
        else:
            cls.artist_count[cls.__current_artist] = 1

    @classmethod
    def add_to_genre_count(cls):
        if cls.__current_genre in cls.genre_count:
            cls.genre_count[cls.__current_genre] += 1
        else:
            cls.genre_count[cls.__current_genre] = 1

    # Since add_to_artists and others need the current artist and genre,
    # we’ll use a little trick to set class-level temporary variables in __init__:
    def add_song_to_count(self):
        Song.count += 1

    def add_to_artists(self):
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

    def add_to_genres(self):
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

    def add_to_artist_count(self):
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1

    def add_to_genre_count(self):
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1


# Example usage:
if __name__ == "__main__":
    song1 = Song("99 Problems", "Jay-Z", "Rap")
    song2 = Song("Halo", "Beyonce", "Pop")
    song3 = Song("Hotline Bling", "Drake", "Rap")

    print(Song.count)           # 3
    print(Song.artists)         # ['Jay-Z', 'Beyonce', 'Drake']
    print(Song.genres)          # ['Rap', 'Pop']
    print(Song.artist_count)    # {'Jay-Z': 1, 'Beyonce': 1, 'Drake': 1}
    print(Song.genre_count)     # {'Rap': 2, 'Pop': 1}

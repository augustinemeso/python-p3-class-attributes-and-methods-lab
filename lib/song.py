class Song:
    # Class Attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment song count when a new song is created
        Song.add_song_to_count()

        # Add the genre to the list and count it
        Song.add_to_genres(genre)
        Song.add_to_genre_count(genre)

        # Add the artist to the list and count it
        Song.add_to_artists(artist)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        # Add genre to the list only if it doesn't already exist
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        # Add artist to the list only if it doesn't already exist
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        # Increment the genre count or add the genre if it doesn't exist
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        # Increment the artist count or add the artist if it doesn't exist
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1


# Create instances of the Song class
song1 = Song("99 Problems", "Jay-Z", "Rap")    # 1st song
song2 = Song("Hotline Bling", "Drake", "Pop")   # 2nd song
song3 = Song("Halo", "Beyonce", "Pop")          # 3rd song
song4 = Song("Empire State of Mind", "Jay-Z", "Rap")  # 4th song

# Check the total number of songs created
print("Total Songs Created (Song.count):", Song.count)  # Expected: 4

# Check the list of unique artists
print("Unique Artists (Song.artists):", Song.artists)  # Expected: ['Jay-Z', 'Drake', 'Beyonce']

# Check the list of unique genres
print("Unique Genres (Song.genres):", Song.genres)  # Expected: ['Rap', 'Pop']

# Check the count of songs by genre
print("Song Count by Genre (Song.genre_count):", Song.genre_count)  # Expected: {'Rap': 2, 'Pop': 2}

# Check the count of songs by artist
print("Song Count by Artist (Song.artist_count):", Song.artist_count)  # Expected: {'Jay-Z': 2, 'Drake': 1, 'Beyonce': 1}

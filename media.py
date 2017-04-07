import webbrowser
import urllib
import json

class Movie():

    """
    This class provides a way to store movie related information
    generated via the OMDb database.

    Movie(title,trailer_url)

    Attributes:
        title (str) - Title of the movie
        trailer url (str) - Full youtube url of the movie's trailer
        poster_url (str) - Full url of the movie's poster image (OMDb)
        storyline (str) - A Summary of the storyline (OMDb)
        cast (str) - A list of the main cast (OMDb)
    """

    def __init__(self, title='', trailer_url=''):
        self.title = title
        self.trailer_url = trailer_url

        # Generate a JSON object of movie information using the OMDb API
        self.omdb = self.omdb_api()

        self.poster_url = self.omdb['Poster']
        self.storyline = self.omdb['Plot']
        self.cast = self.omdb['Actors']

    def omdb_api(self):
        # Open the OMDb API
        api = urllib.urlopen(
            "http://www.omdbapi.com/?t=%s" % self.title.replace(' ','+')
        )

        # Return the JSON object
        return json.loads(api.read())
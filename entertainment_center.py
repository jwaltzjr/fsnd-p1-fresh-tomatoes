import media
import fresh_tomatoes

toy_story = media.Movie(
    title='Toy Story',
    trailer_url = 'https://www.youtube.com/watch?v=KYz2wyBy3kc'
)

avatar = media.Movie(
    title='Avatar',
    trailer_url = 'https://www.youtube.com/watch?v=cRdxXPV9GNQ'
)

pitch_perfect = media.Movie(
    title='Pitch Perfect',
    trailer_url = 'https://www.youtube.com/watch?v=F03N-ApQdmw'
)

the_matrix = media.Movie(
    title='The Matrix',
    trailer_url = 'https://www.youtube.com/watch?v=m8e-FF8MsqU'
)

forrest_gump = media.Movie(
    title='Forrest Gump',
    trailer_url = 'https://www.youtube.com/watch?v=bLvqoHBptjg'
)

the_avengers = media.Movie(
    title='The Avengers',
    trailer_url = 'https://www.youtube.com/watch?v=eOrNdBpGMv8'
)

movies = [toy_story, avatar, pitch_perfect,the_matrix,forrest_gump,the_avengers]

#If run as a script, generate a webpage of the information and open it.
if __name__ == '__main__':
    fresh_tomatoes.open_movies_page(movies)
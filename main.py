from app.movie_listing.app import MovieListingApp
from app.movie_listing.model import Movie

if __name__ == "__main__":
    app = MovieListingApp()
    app.add_movie(Movie("The Shawshank Redemption", "Morgan Freeman, Tim Robbins", "Thriller/Crime", "1994", 2500000))
    app.add_movie(Movie("Titanic", "Leonardo DiCaprio, Kate Winslet", "Romance", "1997", 20000000))
    app.add_movie(Movie("Forrest Gump", "Tom Hanks, Robin wright", "Comedy/Romance", "1994", 5500000))
    app.main()
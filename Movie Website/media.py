#importing appropriate modules
import webbrowser

#creating a class called Movie
class Movie():
    """This class provides a way to store movie related information"""

    #instance varaibles
    valid_ratings = ["G", "P", "PG-13", "R"]

    #constructor
    def __init__(self, movie_title, movie_storyline, movie_poster, movie_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer

    #instance methods
    def show_trailer(self):
        webbrowser.open(self.trailer)
    

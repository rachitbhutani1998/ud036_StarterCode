class Movie:
    """This class is used to create instances for movies specifying their trailer url,poster url along with the title."""
    def __init__(self,name,poster,trailer):
        """
        Initialize the movie instance.
        Arguments:
        name: title of the movie
        poster: image_url of the movie poster
        trailer: trailer_url of the movie
        Returns: 
        None
        """
        self.title=name
        self.poster_image_url=poster
        self.trailer_youtube_url=trailer        

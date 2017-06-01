class Movie:
    """This class is used to create instances for movies specifying their trailer url,poster url along with the title."""
    def __init__(self,name,poster,trailer):
        self.title=name
        self.poster_image_url=poster
        self.trailer_youtube_url=trailer        

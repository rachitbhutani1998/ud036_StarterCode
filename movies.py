import movieClass
import fresh_tomatoes
avengers=movieClass.Movie("The Avengers","https://s-media-cache-ak0.pinimg.com/736x/0f/03/e6/0f03e6733b0cf567cc92e8e20290462f.jpg","https://youtu.be/eOrNdBpGMv8")
captain_america_cw=movieClass.Movie("Captain America: Civil War","https://s-media-cache-ak0.pinimg.com/originals/12/a1/c5/12a1c5ea3a2e8fef09dd373760302c0b.jpg","https://youtu.be/xnv__ogkt0M")
logan=movieClass.Movie("Logan","http://screencrush.com/files/2017/01/loganposter2.jpg","https://youtu.be/Div0iP65aZo")
deadpool=movieClass.Movie("Deadpool","https://s-media-cache-ak0.pinimg.com/originals/9c/c2/c1/9cc2c190f86819cfaeb26755482fc6a5.jpg","https://youtu.be/gtTfd6tISfw")
whiplash=movieClass.Movie("Whiplash","http://www.impawards.com/2014/posters/whiplash.jpg","https://youtu.be/aHDEZXoh4-c")
spiderman=movieClass.Movie("Spiderman Homecoming","https://i.redd.it/ono08hbmbeny.jpg","https://youtu.be/n9DwoQ7HWvI")
movies=[avengers,logan,deadpool,whiplash,spiderman,captain_america_cw]
fresh_tomatoes.open_movies_page(movies)

# importing appropriate modules
import media
import fresh_tomatoes

# creating objects of the Movie class
inception = media.Movie(
    "Inception",
    "A thief, who steals corporate secrets through use of dream-sharing "
    "technology, is given the inverse task of planting an idea into the mind "
    "of a CEO.",
    "https://vignette4.wikia.nocookie.net/inception/images/9/91/Inception_poster.jpg/revision/latest/scale-to-width-down/1000?cb=20140612010814",
    "https://www.youtube.com/watch?v=8hP9D6kZseM")

interstellar = media.Movie(
    "Interstellar",
    "A team of explorers travel through a wormhole in space in an attempt to "
    "ensure humanity's survival.",
    "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
    "https://www.youtube.com/watch?v=zSWdZVtXT7E")

shutter_island = media.Movie(
    "Shutter Island",
    "A U.S Marshal investigates the disappearance of a murderess who escaped "
    "from a hospital for the criminally insane.",
    "https://upload.wikimedia.org/wikipedia/en/7/76/Shutterislandposter.jpg",
    "https://www.youtube.com/watch?v=5iaYLCiq5RM")

deadpool = media.Movie(
    "Deadpool",
    "A former Special Forces operative turned mercenary is subjected to a "
    "rogue experiment that leaves him with accelerated healing powers, "
    "adopting the alter ego Deadpool.",
    "https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",
    "https://www.youtube.com/watch?v=ZIM1HydF9UA")

straight_outta_compton = media.Movie(
    "Straight Outta Compton",
    "The group NWA emerges from the mean streets of Compton in Los Angeles, "
    "California, in the mid-1980s and revolutionizes Hip Hop culture with "
    "their music and tales about life in the hood.",
    "https://upload.wikimedia.org/wikipedia/en/7/7a/Straight_Outta_Compton_poster.jpg",
    "https://www.youtube.com/watch?v=rsbWEF1Sju0")

now_you_see_me_2 = media.Movie(
    "Now You See Me 2",
    "The Four Horsemen resurface and are forcibly recruited by a tech genius "
    "to pull off their most impossible heist yet.",
    "https://upload.wikimedia.org/wikipedia/en/9/9a/Now_You_See_Me_2_poster.jpg",
    "https://www.youtube.com/watch?v=JzZh8kJJwe4")

# creating an array of the Movie objects
movies = [inception,
          interstellar,
          shutter_island,
          deadpool,
          straight_outta_compton,
          now_you_see_me_2]

# calling the fresh tomatoes' open movie page
# method with our given array of movies
fresh_tomatoes.open_movies_page(movies)

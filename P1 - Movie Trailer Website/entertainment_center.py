import os
import sys
import media
import fresh_tomatoes

#create instance of the Spirited Away movie
spirited_away = media.Movie("Spirited Away",
                        "Travel of ten-year old Chihiro and her parents to their new home",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BOGJjNzZmMmUtMjljNC00ZjU5LWJiODQtZmEzZTU0MjBlNzgxL2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UY1200_CR90,0,630,1200_AL_.jpghttps://images-na.ssl-images-amazon.com/images/M/MV5BOGJjNzZmMmUtMjljNC00ZjU5LWJiODQtZmEzZTU0MjBlNzgxL2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                        "https://www.youtube.com/watch?v=ByXuk9QqQkk")

#create instance of the Under the Toscan sun movie
under_the_tuscan_sun = media.Movie("Under the Tuscan Sun",
                     "Story of a writer impulsively buys a villa in Tuscany in order to change her life",
                     "https://upload.wikimedia.org/wikipedia/en/8/8e/Under_the_tuscan_sun_poster.jpg",
                     "https://www.youtube.com/watch?v=vdJGMZDY0-8")

#create instance of the Hachi: A Dog's Tale movie
hachi = media.Movie("Hachi: A Dog's Tale",
                     "A college professor's bond with the abandoned dog he takes into his home.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BYTNhZDFkN2ItMmZjNy00ODUwLTk1Y2MtMDZhYTA2N2MyNDU5XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg",
                     "https://www.youtube.com/watch?v=mhEHr7B1QiU")

#create instance of Race movie
race = media.Movie("Race",
                     "Athlete Jesse Owens, who won a record-breaking four gold medals at the 1936 Berlin Olympic Games",
                     "https://upload.wikimedia.org/wikipedia/en/0/02/Race_2016_film_poster.jpg",
                     "https://www.youtube.com/watch?v=E31LnSw47xo")

john_wick = media.Movie("John Wick: Chapter 2 Action",
                     "Retired super-assassin John Wick's plans to resume a quiet civilian life",
                     "http://aisleseat.com/johnwick2.jpg",
                     "https://www.youtube.com/watch?v=nMqETeQrgqU")

my_neighbor_totoro = media.Movie("My Neighbor Totoro",
                     "Japanese animated fantasy film written and directed by Hayao Miyazaki ",
                     "https://upload.wikimedia.org/wikipedia/en/0/02/My_Neighbor_Totoro_-_Tonari_no_Totoro_%28Movie_Poster%29.jpg",
                     "https://www.youtube.com/watch?v=92a7Hj0ijLs")

movies = [spirited_away, under_the_tuscan_sun, hachi, race, john_wick, my_neighbor_totoro]
#print(race.storyline)
#race.show_trailer()
fresh_tomatoes.open_movies_page(movies)
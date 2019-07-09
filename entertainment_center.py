import fresh_tomatoes
import media
import requests 

harry_potter_data = requests.get("http://www.omdbapi.com/?i=tt3896198&apikey=5fe86317&t=harry+potter")
deadpool2_data = requests.get("http://www.omdbapi.com/?i=tt3896198&apikey=5fe86317&t=deadpool+2")
avengers_data = requests.get("http://www.omdbapi.com/?i=tt3896198&apikey=5fe86317&t=avengers+endgame")
venom_data = requests.get("http://www.omdbapi.com/?i=tt3896198&apikey=5fe86317&t=venom")
logan_data = requests.get("http://www.omdbapi.com/?i=tt3896198&apikey=5fe86317&t=logan")
wall_street_data = requests.get("http://www.omdbapi.com/?i=tt3896198&apikey=5fe86317&t=the+wolf+of+wall+street")

deadpool2 = media.Movie(deadpool2_data.json()['Title'],
                          deadpool2_data.json()['Plot'],
                          deadpool2_data.json()['Poster'],
                          "https://www.youtube.com/watch?v=D86RtevtfrA")

harry_potter = media.Movie(harry_potter_data.json()['Title'],
                          harry_potter_data.json()['Plot'],
                          harry_potter_data.json()['Poster'],
                          "https://www.youtube.com/watch?v=5NYt1qirBWg")

avengers = media.Movie(avengers_data.json()['Title'],
                          avengers_data.json()['Plot'],
                          avengers_data.json()['Poster'],
                          "https://www.youtube.com/watch?v=TcMBFSGVi1c")

venom = media.Movie(venom_data.json()['Title'],
                          venom_data.json()['Plot'],
                          venom_data.json()['Poster'],
                          "https://www.youtube.com/watch?v=xLCn88bfW1o")

logan = media.Movie(logan_data.json()['Title'],
                          logan_data.json()['Plot'],
                          logan_data.json()['Poster'],
                          "https://www.youtube.com/watch?v=Div0iP65aZo")
wall_street = media.Movie(wall_street_data.json()['Title'],
                          wall_street_data.json()['Plot'],
                          wall_street_data.json()['Poster'],
                          "https://www.youtube.com/watch?v=iszwuX1AK6A")

movies = [deadpool2, harry_potter, avengers, venom, logan, wall_street]

fresh_tomatoes.open_movies_page(movies)

import requests

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzZWU2OWU1ODE0ODVlYzAyZjg1MTNmNDY1ZTU0MGJlMyIsInN1YiI6IjYyNGVjNjI2MDcyOTFjMDA1MDkxYzUxMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.xy58r19rmeLHVvgy1nxt78eENS5KhvZMwDJz3WWlhnM"

def call_tmdb_api(endpoint):
   full_url = f"https://api.themoviedb.org/3/{endpoint}"
   headers = {
       "Authorization": f"Bearer {API_TOKEN}"
   }
   response = requests.get(full_url, headers=headers)
   response.raise_for_status()
   return response.json()

def get_movies_list(list_type):
   return call_tmdb_api(f"movie/{list_type}")



def get_single_movie(movie_id):
    return call_tmdb_api(f"movie/{movie_id}")
    


def get_popular_movies():
    return call_tmdb_api(f"movie/popular")
  


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_single_movie_cast(movie_id):
    return call_tmdb_api(f"movie/{movie_id}/credits")
    


def get_movie_images(movie_id):
    return call_tmdb_api(f"movie/{movie_id}/images")


def get_movies(how_many, list_type='popular'):
    data = get_movies_list(list_type)
    return data["results"][:how_many]


def search(search_query):
    return call_tmdb_api(f"movie/?query={search_query}")
    


def get_airing_today():
    return call_tmdb_api(f"tv/airing_today")
    

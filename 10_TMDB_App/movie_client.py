import requests
import collections

MovieResult = collections.namedtuple(
	'MovieResult',
	'adult,backdrop_path,genre_ids,id,original_language,original_title,overview,popularity,poster_path,release_date,title,video,vote_average,vote_count'
)

class MovieClient:
	def __init__(self, search_text):
		self.search_text = search_text

	def perform_search(self):
		url = 'https://api.themoviedb.org/3/search/movie?api_key=65abcf69e20e8b8b77240ef3e53d670f&language=ru-RU&query={}'.format(self.search_text)


		r = requests.get(url)
		data = r.json()


		results = data['results']

		movies = [
			MovieResult(**m)
			for m in results
			]
		movies.sort(key=lambda m: m.title)

		return movies

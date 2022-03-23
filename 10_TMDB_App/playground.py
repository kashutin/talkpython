#
# Searcher string
# https://api.themoviedb.org/3/search/movie?api_key=65abcf69e20e8b8b77240ef3e53d670f&query=capital+c
#
# Name String

# Poster path
# https://image.tmdb.org/t/p/w500//xcJOgtQjjcJpLw8UOBqNmfPthhm.jpg



import requests
import collections

MovieResult = collections.namedtuple(
	'MovieResult',
	'adult,backdrop_path,genre_ids,id,original_language,original_title,overview,popularity,poster_path,release_date,title,video,vote_average,vote_count'
)


search = 'capital'
url = 'https://api.themoviedb.org/3/search/movie?api_key=65abcf69e20e8b8b77240ef3e53d670f&language=ru-RU&query={}'.format(search)

r = requests.get(url)
data = r.json()


results = data['results']

# movies = []
# for result in results:
# 	m = MovieResult(
# 		adult=result['adult'],
# 		backdrop_path=result['backdrop_path'],
# 		genre_ids=result['genre_ids'],
# 		id=result['id'],
# 		original_language=result['original_language'],
# 		original_title=result['original_title'],
# 		overview=result['overview'],
# 		popularity=result['popularity'],
# 		poster_path=result['poster_path'],
# 		release_date=result['release_date'],
# 		title=result['title'],
# 		video=result['video'],
# 		vote_average=result['vote_average'],
# 		vote_count=result['vote_count']
# 	)
# 	movies.append(m)


# def method_with_kws(pos1, **kwargs)
# pass

# movies = []
# for result in results:
# 	m = MovieResult(**result)
# 	movies.append(m)

movies = [
	MovieResult(**m)
	for m in results
]

print(len(movies))
print(movies)

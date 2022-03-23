from movie_client import MovieClient


def main():
		print_header()
		search_event_loop()


def print_header():
	print('-----------------------------')
	print(' The Movie DataBase Searcher')
	print('-----------------------------')


def search_event_loop():
	search = 'ONCE_THROUGH_LOOP'

	while search != 'x':
		search = input('Title search text (x to exit): ')
		if search != 'x':
			client = MovieClient(search)

			results = client.perform_search()
			print('Found {} results.'.format(len(results)))
			for r in results:
				print('Title:{} / {}\nReleased:{}\nDescription: {}\n'.format(
					r.title, r.original_title, r.release_date, r.overview
				))
			print('Found {} results.'.format(len(results)))

	print('exiting...')


if __name__ == '__main__':
	main()

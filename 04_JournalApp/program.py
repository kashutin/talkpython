import journal


# from journal import load, save
# from journal import *

def main():
	print_header()
	run_event_loop()


def print_header():
	print('------------------------')
	print('-------Дневник----------')
	print('------------------------')


def run_event_loop():
	print('Что делаем с дневником?')
	cmd = 'EMPTY'
	journal_name = 'default'
	journal_data = journal.load(journal_name)  # list()-новый список
	while cmd != 'x' and cmd:
		cmd = input('(L)Перечислить записи, (A) Добавить запись, (x) Выход: ')
		cmd = cmd.lower().strip()
		if cmd == 'l':
			list_entries(journal_data)
			# print_list(journal_data)
			# print_list2(journal_data)
		elif cmd == 'a':
			add_entry(journal_data)
		elif cmd != 'x' and cmd:
			print("Шото жмешь не то, лабасик. Команда '{}' не найдена.".format(cmd))

	print('Давай, досвидания!')
	journal.save(journal_name, journal_data)


def list_entries(data):
	print('Список твоих бредней: ')
	entries = reversed(data)
	for idx, entry in enumerate(entries):
		print('* [{}] {}'.format(idx + 1, entry))


def print_list(data):
	for item in data:
		print("this is item {}".format(item))


def print_list2(data):
	for idx in range(len(data)):
		print("номер {} запись {}".format(idx + 1, data[idx]))


def add_entry(data):
	text = input('Записую, шо хотел: ')
	journal.add_entry(text, data)
	# data.append(text)

print("__file__:\t" + __file__)
print("__name__:\t" + __name__)


if __name__ == '__main__':
	main()

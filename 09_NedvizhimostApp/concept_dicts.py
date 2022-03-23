
lookup = {}
lookup = dict()
lookup = {'age': 42, 'loc': 'Italy'}
lookup = dict(age=42, loc='Italy')


class Wizard:
	def __init__(self, name, level):
		self.level = level
		self.name = name

Janoff = Wizard('Janoff', 12)
print(Janoff.__dict__)


print(lookup)
print(lookup['loc'])

lookup['cat'] = 'Fun code demos'

if 'cat' in lookup:
	print(lookup['cat'])


# print(lookup)

import collections

User = collections.namedtuple('User', 'id, name, email')
users = [
	User(1, 'user1', 'user1@rada.org.ua'),
	User(2, 'user2', 'user2@rada.org.ua'),
	User(3, 'user3', 'user3@rada.org.ua'),
	User(4, 'user4', 'user4@rada.org.ua'),
]

lookup = dict()
for u in users:
	lookup[u.email] = u

print(lookup['user4@rada.org.ua'])
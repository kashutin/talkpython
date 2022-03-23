import random
import time

from actors import Wizard, Creature, Zver, Nark

def main():
	print_header()
	game_loop()


def print_header():
	print('----------------------------')
	print('      Jiva valit vseh')
	print('----------------------------')
	# pass


def game_loop():

	creatures = [
		Zver('Homyak', 1),
		Zver('Bober', 2),
		Nark('Rudyuk', 20, 10, False),
		Nark('Biba', 5, 10, True),
		Creature('Nevidim', 50),
		Wizard('Janoff', 30)
	]


	hero = Wizard('Jiva', 30)


	while True:

		active_creature = random.choice(creatures)
		print('\n{} {} levela viskochil iz padika...'.format(active_creature.name, active_creature.level))
		print()

		cmd = input('[B]uhaem, [p]idpaluemo, or bur[l]im?')
		if cmd.lower() == 'b':
			if hero.attack(active_creature):
				creatures.remove(active_creature)
			else:
				print('Jiva otoshel popustitsya...')
				time.sleep(5)
				print('Jiva PROTREZVEL!!!')


		elif cmd.lower() == 'p':
			print('{} ne uveren chto smojet perebuhat {}. Poshel DOLBIT'.format(hero.name, active_creature))
		elif cmd.lower() == 'l':
			print('{} prisel na lavku i palit s kem vlit slivu:'.format(hero.name))
			for c in creatures:
				print(' * {} {} levela'.format(c.name, c.level))
		else:
			print('Nabuhalsya i zhmesh sho popalo. Poka')
			break


		if not creatures:
			print('''
			-----------------------------------
			{} perebuhal VSEH!!!
			{} TEPER GLAVNAYA SLIVA RAYONA!!!
			-----------------------------------
			'''.format(hero.name, hero.name))
			break


if __name__ == '__main__':
	main()

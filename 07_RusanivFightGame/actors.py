import random


class Creature:
	def __init__(self, name, the_level):
		self.name = name
		self.level = the_level

	def __repr__(self):
		return "Rusanovskaya jivnost: {} {} levela".format(self.name, self.level)

	def get_defensive_roll(self):
		return random.randint(1, 12) * self.level



class Wizard(Creature):

	def attack(self, creature):
		print("{} vlil slivu v {}".format(
			self.name, creature.name
		))

		my_roll = self.get_defensive_roll()
		creature_roll = creature.get_defensive_roll()

		print('Master {} vlil {}...'.format(self.name, my_roll))
		print('{} vlil tebe v otvet {} ...'.format(creature.name, creature_roll))

		if my_roll >= creature_roll:
			print('{} legko perebuhal {}'.format(self.name, creature.name))
			return True
		else:
			print('{} uzhralsya v HLAM!!!'.format(self.name))
			return False



class Zver(Creature):
	def get_defensive_roll(self):
		base_roll = super().get_defensive_roll()
		return base_roll/2


class Nark(Creature):
	def __init__(self, name, level, scaliness, breaths_fire):
		super().__init__(name, level)
		self.breaths_fire = breaths_fire
		self.scaliness = scaliness


	def get_defensive_roll(self):
		base_roll = super().get_defensive_roll()
		# fire_modifier = None
		# if self.breaths_fire:
		# 	fire_modifier = 5
		# else:
		# 	fire_modifier = 1

		# fire_modifier = VALUE_IF_TRUE if SOME TEST else VALUE IS FALSE
		fire_modifier = 10 if self.breaths_fire else 1
		scale_modifier = self.scaliness / 10

		return base_roll * fire_modifier * scale_modifier







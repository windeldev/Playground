from game_object_v3 import GameObject

class Goblin(GameObject):
	def __init__(self, name):
		self.class_name = "goblin"
		self._desc = "A foul creature"
		self.health = 3
		super().__init__(name)

	@property
	def	desc(self):
		if self.health >= 3:
			return self._desc
		elif self.health == 2:
			health_line = "It has a wound on its knee."
		elif self.health == 1:
			health_line = "Its left arm has been cut off!"
		elif self.health <= 0:
			health_line = "It is dead."
		return self._desc + "\n" + health_line
	
	@desc.setter
	def desc(self, value):
		self._desc = value

	def get_desc(self):
		return super().get_desc() + "\nHealth: " + str(self.health)

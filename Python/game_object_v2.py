class GameObject:
	class_name = ""
	desc = ""
	objects = {}

	def __init__(self, name):
		self.name = name
		GameObject.objects[self.class_name] = self

	def get_desc(self):
		return self.class_name + "(" + self.name + ")" + "\n" + self.desc

class Goblin(GameObject):
	class_name = "goblin"
	desc = "A foul creature"

def examine(noun):
	if noun in GameObject.objects:
		return GameObject.objects[noun].get_desc()
	else:
		return "There is no {} here.".format(noun)

def list_objects():
	for x in GameObject.objects:
		print(GameObject.objects[x].get_desc())

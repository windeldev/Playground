class GameObject:
	class_name = ""
	desc = ""
	objects = {}

	def __init__(self, name):
		self.name = name
		GameObject.objects[self.class_name] = self

	def get_desc(self):
		return self.class_name + "(" + self.name + ")" + "\n" + self.desc

	def examine(noun):
		if noun in GameObject.objects:
			return GameObject.objects[noun].get_desc()
		else:
			return "There is no {} here.".format(noun)

	def list_objects():
		for x in GameObject.objects:
			print(GameObject.objects[x].get_desc())

	def hit(noun):
		#print(noun)
		msg ="There is no {} here.".format(noun)
		if noun in GameObject.objects:
			if GameObject.objects[noun]:
				thing = GameObject.objects[noun]
				thing.health = thing.health - 1
				if thing.health <= 0:
					msg = f"You killed the {thing.name}!"
				else:
					msg = "You hit the {}. {}".format(thing.class_name, thing.desc)
		return msg
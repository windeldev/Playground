class GameObject:
  class_name = ""
  desc = ""
  objects = {}

  def __init__(self, name):
    self.name = name
    GameObject.objects[self.class_name] = self

  def get_desc(self):
    return self.class_name + "\n" + self.desc

class Goblin(GameObject):
  class_name = "goblin"
  desc = "A foul creature"

def examine(noun):
  if noun in GameObject.objects:
    return GameObject.objects[noun].get_desc()
  else:
    return "There is no {} here.".format(noun)

goblin = Goblin("Gobbly")
print(goblin.name)
print(examine("goblin"))
print(GameObject.objects)

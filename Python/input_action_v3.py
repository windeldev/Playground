import sys, goblin as gob

def get_input():
	command = input("what?: ").split()
	verb_word = command[0]
	if verb_word in verb_dict:
		verb = verb_dict[verb_word]
	else:
		print("Unknown verb {}". format(verb_word))
		return

	if len(command) >= 2:
		noun_word = command[1]
		#print(command)
		if verb_word == "create":
			params = []
			if len(command) > 2:
				params = [command[x] for x in range(2, len(command))]
			print (verb(noun_word, params))
		else:
			print (verb(noun_word))
	else:
		if verb_word == "list":
			print(verb())
		else:
			print(verb("nothing"))

def say(noun):
	return 'You said "{}"'.format(noun)

def create(noun, *args):
	if noun == "goblin":
		go_name = "Gobbly"
		#print(args)
		if len(args) > 0:
			go_name = args[0][0]
		goblin = gob.Goblin(go_name)
		txt = gob.GameObject.examine(noun)
		return 'Created: {}'.format(txt)
	else:
		return 'Unable to create "{}"'.format(noun)

#def target_action(noun, *args):
#	if noun == "goblin":

def exit(noun):
	sys.exit()


verb_dict = {
	"say": say,
	"exit": exit,
	"bye": exit,
	"create": create,
	"hit": gob.GameObject.hit,
	"examine": gob.GameObject.examine,
	"list": gob.GameObject.list_objects
}

while True:
	get_input()
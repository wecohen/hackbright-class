direction_words = ["north", "south", "east", "west", "down", "up", "left", "right", "back"]
verbs = ["go", "stop", "kill", "eat"]
stop_words = ["the", "in", "of", "from", "at", "it"]
nouns = ["door", "bear", "princess", "cabinet"]
numbers = "0123456789"

d_w = ["direction_words"] *len(direction_words)
v = ["verbs"] * len(verbs)
s_w = ["stop_words"] * len(stop_words)
noun = ["nouns"] * len(nouns)
num = ["number"] * len(numbers)

#print d_w
verb=dict(zip(verbs, v))
stop=dict(zip(stop_words, s_w))
nou=dict(zip(nouns, noun))
number = dict(zip(numbers, num))
direction =dict(zip(direction_words, d_w))

lex = dict(verb.items() + stop.items() + nou.items() + number.items() + direction.items())


def scan():
	user_input = raw_input('>')
	words = user_input.split()
	alist = []
	for word in words:
		if word in lex:
			t = (lex[word], word)
			alist.append(t)
		else:
			if convert_number(word) == None:
				t = ("WordError", word)
				alist.append(t)
			else:
				t = ("ValueError", word)
				alist.append(t)
	return alist

def convert_number(s):
	try:
		return int(s)
	except ValueError:
		return None

stuff = scan()
print stuff
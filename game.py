#this is a game
import sys

#PSEUDO CODE PLANNING ::
#cyoa type game (ex. zed shaw)
#user input based (different outcomes based on different inputs), but give action options
#raw_input("choose: run, shoot, jump, hide")
#after a certain amount of guesses, trigger a hint
#user's answers take them to different questions as well as different endings.
#user's answers collectively will lead to a general output statement at the end "you answered x,y,z therefore you are a a crazy beast"


class Cave(object):

	def play(self):
		print """\
You have found yourself in the Cave of Wonders. There are shiny objects everywhere,
but watch out! There are hidden dangers behind every corner. There are 3 possible routes for you to choose from: a shadowy tunnel
straight ahead, a ladder leading out of the cave into the wilds, and a slide down into the dark depths
		"""

		my_treasure = self.treasure()
		hunter_input = raw_input("Do you choose the tunnel, the ladder, or the slide? ")
		if hunter_input == "tunnel":
			return BanditLair()
		elif hunter_input == "ladder":
			return Outside()
		elif hunter_input == "slide":
			return EarthsCore()



	def treasure(self):		
		treasure_input = raw_input("Would you like to take something with you before you leave? ")	
		if treasure_input == "yes":
			print """\
you pick up a tiny silver axe. It looks made for a child, or a hobbit. 
This will be your only tool you may bring with you. It will come in handy later.
			"""
			return "silver axe"
		if treasure_input == "no":
			print """\
okay. That was stupid. You'll need to bring something with you 
from one of the next rooms to retrieve your treasure at the end.
			"""	
			return "nothing"

	


	
class BanditLair(object):
	def play(self):
		print """\
Aha! You crawled through the shadowy tunnel to arrive in a Bandit Lair! Be careful, they could come back
at any moment. You begin to look around and see all of the loot the bandits have acquired. There are a number of
intriguing objects that catch your eye. Make haste! The bandit return is imminent! There are 2 possible paths to 
freedom: a possible pathway hidden behind a boulder, or wooden latch in the corner of the room.
		"""

		my_treasure = self.treasure()
		hunter_input = raw_input("Do you choose the boulder or the wooden latch? ")
		if hunter_input == "boulder":
			return EndRoom()
		if hunter_input == "wooden latch":
			print """\
The wooden latch was a trap! It was a hidey hole for their secret stash of Broadway Musicals. What a strange
group of bandits this is... Alas! They arrived and upon catching you red-handed with their Sondheim scores, they
flew into a senseless rage and stabbed you to death. This was not your day.
			"""
			return sys.exit(0)	

	def treasure(self):		
		treasure_input = raw_input("Do you want to take an intriguing object with you? ")
		if treasure_input == "yes":
			print "you take with you gilded flute. We're not really sure why you did that."
			return "gilded flute"

		if treasure_input == "no":
			# if instance.treasure == "silver axe":
			# 	print "You already have taken an item, don't be greedy."
			# else:
				print """\
You have to take something with you, thus you are forced to take an item. You grab a silly gilded flute.
This is your punishment for not following directions. Bad treasure hunter!
				"""
				return "gilded flute"


		


class Outside(object):
	def play(self):
		print """\
You chose the rickety ladder leading to the sliver of light outside of the cave. Why would you do that??
Caves are obviously where treasure is hidden, treasure is NOT hidden in the middle of an open field.
Where you have suddenly found yourself.
		"""
		hunter_input = raw_input("Do you want to try again? Yes or No? ")
		if hunter_input == "yes":
			return Cave()
		elif hunter_input == "no":
			print "fine. you're done homeslice."
			return sys.exit(0)


class EarthsCore(object):	
	def play(self):
		print """\
You took the slide and it was realllllllly long. You have arrived at the Earth's core. It's way too hot down here to survive.
Somehow, you have. Don't question it. You may hike back up the slide to the Cave, or you will die in the fiery
inferno that exists within the center of the Earth. 
		"""
		hunter_input = raw_input("Do you want to hike back up to the Cave? ")
		if hunter_input == "yes":
			return Cave()
		if hunter_input == "no":
			print "You died."	
			return sys.exit(0)


class EndRoom(object):
	def play(self):
		instance = Cave()
		bandstance = BanditLair()
		if instance.treasure() == "silver axe":
			print """\
You pushed open the boulder and found yourself in a glorious tavern full of delicious baked goods,
refreshing beverages, and more treasures than you ever could have imagined. But wait! There is a tiny
yet fearsome troll guarding the greatest treasure of them all. You battle the troll with your tiny child-sized
axe and win! You may now bask in the glory that is all this food and drink. Yay.
			"""
			return sys.exit(0)
		elif bandstance.treasure() == "gilded flute":
			print """\
You pushed open the boulder and found yourself in a glorious tavern full of delicious baked goods,
refreshing beverages, and more treasures than you ever could have imagined. But wait! There is a tiny
yet fearsome troll guarding the greatest treasure of them all. You lull him into a stupor with a mesmerizing
tune. You now may bask in the glory that is all of this wealth. That damn flute came in handy, after all. Yay.
			"""
			return sys.exit(0)


	

class TreasureHunter(object):
	def __init__(self, First_room):
		self.First_room = First_room

	def begin(self):
		next_room = self.First_room

		while True:
			next_room = next_room.play()


def main():
	print """\
Welcome to Treasure Hunter Extravaganza!!! The best game ever. Get super excited and remember that at some point,
you'll need to take an item with you from one level to another to retrieve your final treasure.
	"""
	game = TreasureHunter(Cave())
	game.begin()


if __name__ == "__main__":
	main()
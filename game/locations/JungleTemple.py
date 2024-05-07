from game import location
import game.config as config
from game.display import announce
from game.events import *


class EthanJungleTemple(location.Location):

    def __init__ (self, x, y, w):
        super().__init__(x, y, w)
        self.name = "temple"
        self.symbol = 'j'
        self.visitable = True
        self.starting_location = JungleEntrance(self)
        self.locations = {}
        self.locations["north"] = NorthEdge(self)
        self.locations["entrence"] = JungleEntrance(self)
        self.locations["east"] = EastEdge(self)
        self.locations["west"] = WestEdge(self)

        # Center temple
        self.locations["temple"] = JungleTemple(self)

    def enter(self, ship):
        announce ("You have arrived at a dense, mysterious jungle island.")

    def visit(self):
        config.the_player.location = self.starting_location
        config.the_player.location.enter()
        super().visit()

class NorthEdge(location.SubLocation):
    def __init__(self, m):
        super().__init__(m)
        self.name = "jungleNorthEdge"
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['east'] = self
        self.verbs['west'] = self

    def enter(self):
        announce ("You're surrounded by tall vines. There's nothing of interest here.")

    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "north" or verb == "east" or verb == "west"):
            announce ("They find the edge of the island\nPerhaps they should go south?")
        elif (verb == "south"):
            config.the_player.go = True
            config.the_player.next_loc = self.main_location.locations["entrence"]

class EastEdge(location.SubLocation):
    def __init__(self, m):
        super().__init__(m)
        self.name = "jungleEastEdge"
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['east'] = self
        self.verbs['west'] = self

    def enter(self):
        announce ("You're surrounded by tall vines. There's nothing of interest here.")

    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "east" or verb == "south"):
            announce ("They find the edge of the island\nPerhaps they should go south or west?")
        elif (verb == "south" or verb == "west"):
            config.the_player.go = True
            config.the_player.next_loc = self.main_location.locations["entrence"]
        elif (verb == "north"):
            config.the_player.go = True
            config.the_player.next_loc = self.main_location.locations["north"]

class WestEdge(location.SubLocation):
    def __init__(self, m):
        super().__init__(m)
        self.name = "jungleWestEdge"
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['east'] = self
        self.verbs['west'] = self

    def enter(self):
        announce ("You're surrounded by tall vines. There's nothing of interest here.")

    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "west" or verb == "south"):
            announce ("They find the edge of the island\nPerhaps they should go south or east?")
        elif (verb == "south" or verb == "east"):
            config.the_player.go = True
            config.the_player.next_loc = self.main_location.locations["entrence"]
        elif (verb == "north"):
            config.the_player.go = True
            config.the_player.next_loc = self.main_location.locations["north"]

class JungleEntrance(location.SubLocation):
    def __init__(self, m):
        super().__init__(m)
        self.name = "jungleEntrance"
        self.verbs['enter'] = self
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['east'] = self
        self.verbs['west'] = self

    def enter(self):
        announce ("You stand at the edge of a dense jungle. You can see a mysterious temple deeper inside.\nWill they enter the temple?")
    
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south"):
            announce ("You return to your ship.")
            config.the_player.next_loc = config.the_player.ship
            config.the_player.visiting = False
        elif (verb == "north" or verb == "east" or verb == "west"):
            config.the_player.next_loc = self.main_location.locations[verb]
        if (verb == "enter"):
            config.the_player.go = True
            config.the_player.next_loc = self.main_location.locations["temple"]


class JungleTemple(location.SubLocation):
    def __init__(self, m):
        super().__init__(m)
        self.name = "jungleTemple"
        self.verbs['enter'] = self

    def enter(self):
        announce ("You step into the ancient temple, feeling a sense of reverence and mystery.")
        # Add riddles to solve here, if you get them right, you go to the next room, if you get them wrong, you get attacked by a monster, if you defeat the monster, you go to the next room anyways. At the end, you get a special item, a golden claymore sword
    
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "test"):
            announce ("You return to your ship. WORK IN PROGRESS.")
            config.the_player.next_loc = config.the_player.ship
            config.the_player.visiting = False

"""
Here's the riddles

What has keys but can't open locks?
a) A piano
b) A computer
c) A book
d) A map
What has a head, a tail, is brown, and has no legs?
a) A penny
b) A snake
c) A horse
d) A banana
The more you take, the more you leave behind. What am I?
a) Footprints
b) A secret
c) Money
d) Time
What is always in front of you but can't be seen?
a) Tomorrow
b) The past
c) Air
d) Your nose
What comes once in a minute, twice in a moment, but never in a thousand years?
a) The letter "M"
b) The letter "E"
c) The letter "N"
d) The letter "O"
What can travel around the world while staying in a corner?
a) A stamp
b) A map
c) An airplane
d) A postcard
What has a head, a tail, is brown, and has no legs, but can sometimes walk?
a) A coin
b) A snake
c) A horse
d) A river
The more you take, the more you leave behind. What am I?
a) Footsteps
b) Breath
c) Memories
d) A trail
What is full of holes but still holds water?
a) A sponge
b) A strainer
c) A bottle
d) A pipe
What has a neck but no head?
a) A bottle
b) A snake
c) A pencil
d) A sweater
"""
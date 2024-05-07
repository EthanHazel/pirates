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
        self.locations["north"] = JungleEdge(self)
        self.locations["south"] = JungleEdge(self)
        self.locations["east"] = JungleEdge(self)
        self.locations["west"] = JungleEdge(self)

        # Center temple
        self.locations["temple"] = JungleTemple(self)

    def enter(self, ship):
        announce ("You have arrived at a dense, mysterious jungle island.")

    def visit(self):
        config.the_player.location = self.starting_location
        config.the_player.location.enter()
        super().visit()


# TODO: Convert this to eastEdge westEdge etc so you can find your way back to the temple.
class JungleEdge(location.SubLocation):
    def __init__(self, m):
        super().__init__(m)
        self.name = "jungleEdge"
        self.verbs['test'] = self

    def enter(self):
        announce ("You're surrounded by tall vines. There's nothing of interest here.")

    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "test"):
            announce ("You return to your ship. WORK IN PROGRESS.")
            config.the_player.next_loc = config.the_player.ship
            config.the_player.visiting = False

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
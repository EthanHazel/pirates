
from game import location
import game.config as config
from game.display import announce
from game.events import *
import game.items as items
import random

class EthanTemple(location.Location):
    """A temple in the jungle with a treasure on a pedestal, but it has a 50% chance for a booby trap to trigger than ingures the player grabbing it, but always misses if the player is lucky."""
    def __init__ (self, x, y, w):
        super().__init__(x, y, w)
        self.name = "temple"
        self.symbol = 'T'
        self.visitable = True
        self.starting_location = self
        self.locations = {}
        self.locations["beach"] = self.starting_location
        self.verbs = {}
        self.verbs['take'] = self
        self.treasure = items.GoldenClaymore()
        self.booby_trap_triggered = False

    def enter(self):
        description = "You enter a mysterious temple in the jungle. You see a " + self.treasure.name + " on a pedestal."
        announce(description)

    def process_verb(self, verb, cmd_list, nouns):
        if verb == "take":
            if self.treasure is not None and (len(cmd_list) > 1 and cmd_list[1] == self.treasure.name):
                announce("You take the " + self.treasure.name + " from the pedestal.")
                config.the_player.add_to_inventory([self.treasure])
                self.treasure = None
                config.the_player.go = True

                # 50% chance to trigger the booby trap
                if random.randint(1, 2) == 1:
                    self.booby_trap_triggered = True
                    c = random.choice(config.the_player.get_pirates())
                    if c.isLucky() == True:
                        announce("A booby trap is triggered, but you narrowly avoid an arrow!")
                    else:
                        announce(c.get_name() + " is hit by an arrow from a booby trap!")
                        if c.inflict_damage(1, "Hit by an arrow from a booby trap"):
                            announce(".. " + c.get_name() + " is injured!")
            else:
                announce("You don't see one of those around.")
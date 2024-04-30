import game.event as event
import random
import game.combat as combat
import game.superclasses as superclasses
from game.display import announce

class AbandonedShipEthan (event.Event):
    # THIS IS WORK IN PROGRESS
    # This is currently just a clone of the drowned pirates event as it is similar in combat but will later be what is described.
    '''
    An encounter with an abandoned ship with loot, that has a chance for an enemy pirate encounter.
    When the event is drawn, it gives the crew some loot drawn from it's loot table, but also has a 1 in 4 chance to spawn an enemy pirate, then kicks control over to the combat code to resolve the fight, then adds itself and a simple success message to the result
    '''

    def __init__ (self):
        self.name = " abandonded ship encounter"
        self.description = "You come across an abandoned ship. You can search it for loot, but beware, there may be pirates aboard!"
        self.loot = []
        self.pirates = 1 if random.randint(1, 4) == 1 else 0

    def process (self, world):
        '''Process the event. Populates a combat with a Crazed Pirate.'''
        result = {}
        result["message"] = "the crazed pirate is defeated!"
        crazed = []
        crazed.append(combat.CrazedPirate("Crazed pirate"))
        announce("You are attacked by a crazed pirate!")
        combat.Combat(crazed).combat()
        result["newevents"] = [ self ]
        return result
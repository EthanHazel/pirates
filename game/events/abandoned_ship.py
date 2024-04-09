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
        self.name = " drowed pirate attack"

    def process (self, world):
        '''Process the event. Populates a combat with Drowned monsters. The first Drowned may be modified into a "Pirate captain" by buffing its speed and health.'''
        result = {}
        result["message"] = "the drowned pirates are defeated!"
        monsters = []
        min = 2
        uplim = 6
        if random.randrange(2) == 0:
            min = 1
            uplim = 5
            monsters.append(combat.Drowned("Pirate captain"))
            monsters[0].speed = 1.2*monsters[0].speed
            monsters[0].health = 2*monsters[0].health
        n_appearing = random.randrange(min, uplim)
        n = 1
        while n <= n_appearing:
            monsters.append(combat.Drowned("Drowned pirate "+str(n)))
            n += 1
        announce ("You are attacked by a crew of drowned pirates!")
        combat.Combat(monsters).combat()
        result["newevents"] = [ self ]
        return result

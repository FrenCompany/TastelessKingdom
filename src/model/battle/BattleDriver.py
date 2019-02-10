from .Chef import Chef
from .BattleState.ChefTurn import ChefTurn


class BattleDriver:
    def __init__(self, player, citizens):
        # TODO: implement player class
        self.chef = Chef(player.deck, player.inventory, player.speciality, player.modifier, player.defense,
                         player.max_morale, citizens)
        self.state = ChefTurn(self)

    def set_state(self, state):
        self.state = state

    def battle_loop(self):
        # Tick buffs
        # Chef turn (cook)
        # Citizen turn (eat and react)
        # End battle?
        pass

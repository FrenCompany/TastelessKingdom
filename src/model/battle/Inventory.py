from src.model.Ingredients import Ingredients


class Inventory:
    # takes the player's basic inventory (a dictionary with the enum values as keys,
    # the quantity and regeneration of each ingredient) and creates the inventory needed
    # for battle, with available ingredients

    def __init__(self, player_inventory):
        self.inventory = {}
        for key in player_inventory:
            amount = player_inventory[key]
            regen = Ingredients.get_regen(key)
            # inventory: max, regeneration ratio, available
            self.inventory[key] = [amount, regen, amount]

    # regenerates ingredients according to their regeneration ratio
    def regenerate_ingredients(self):
        for i in self.inventory:
            item = self.inventory[i]
            # if item isn't fully stocked
            if item[2] < item[0]:
                # adds corresponding portion
                item[2] += item[1]

    # lowers the availability of the item by 1
    def use_item(self, item, amount):
        self.inventory[item][2] -= amount

    # returns true if chef has enough of the required ingredients
    def can_cook(self, recipe):
        for key in recipe.ingredient_list:
            if key not in self.inventory or recipe.ingredient_list[key] >= self.inventory[key][2]:
                return False
        return True

    def get_amount(self, ing_key):
        return self.inventory[ing_key][2]

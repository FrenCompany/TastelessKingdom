class Inventory:
    # takes the player's basic inventory (a dictionary with the enum values as keys,
    # the quantity and regeneration of each ingredient) and creates the inventory needed
    # for battle, with available ingredients

    def __init__(self, player_inventory):
        self.inventory = {}
        for i in player_inventory:
            item = player_inventory[i]
            # inventory: max, regeneration ratio, available
            self.inventory[i] = [item[0], item[1], item[0]]

    # regenerates ingredients according to their regeneration ratio
    def regenerate_ingredients(self):
        for i in self.inventory:
            item = self.inventory[i]
            # if item isn't fully stocked
            if item[2] < item[0]:
                # adds corresponding portion
                item[2] += item[1]

    # lowers the availability of the item by 1
    def use_item(self, item):
        self.inventory[item][2] -= 1

    # returns true if chef has enough of the required ingredients
    def can_cook(self, recipe):
        for i in recipe.ingredient_list:
            if i not in self.inventory or recipe.ingredient_list[i] >= self.inventory[i][2]:
                return False
        return True

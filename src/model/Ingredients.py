from enum import Enum, auto


class Ingredients(Enum):
    TOMATO = auto()
    LETTUCE = auto()
    STRAWBERRY = auto()

    @classmethod
    def get_name(cls, ingredient):
        return atributes[ingredient]['name']

    @classmethod
    def get_regen(cls, ingredient):
        return atributes[ingredient]['regeneration']

    @classmethod
    def get_img(cls, ingredient):
        return atributes[ingredient]['img']

    @classmethod
    def get_attributes(cls, ingredient):
        return atributes[ingredient]


atributes = {
    Ingredients.TOMATO: {
        'name': 'tomato',
        'regeneration': 1,
        'img': 'fruta manzana'
    },
    Ingredients.LETTUCE: {
        'name': 'lettuce',
        'regeneration': 1,
        'img': 'fruta arandano'
    },
    Ingredients.STRAWBERRY: {
        'name': 'strawberry',
        'regeneration': 1,
        'img': 'fruta frutilla'
    },
}

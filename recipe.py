'''
    Structure of one Recipe:
    |
    |--ID
    |--Name
    |--Comment
    |--num Portions
    |--Ingredients
    |  |--Ingredient1
    |  |  |--amount
    |  |  |--unit
    |  |  |--what
    |  |--Ingredient2
    |     |--amount
    |     |--unit
    |     |--what
    |   ...
    |--Instructions
    |--Rating
    |--Difficulty
    |--Preparation Time
    |--Cuisine
'''

class Recipe:

    def __init__(self, id, name, comment, portions, ingredients,
                 instructions, rating, difficulty, prep_time, cuisine):
        self.id = id
        self.name = name
        self.comment = comment
        self.portions = portions
        self.ingredients = ingredients
        self.instructions = instructions
        self.rating = rating
        self.difficulty = difficulty
        self.prep_time = prep_time
        self.cuisine = cuisine

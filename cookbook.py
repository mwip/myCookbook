'''
    Structure of one Cookbook:
    |
    |--Name
    |--Description
    |--Comment
    |--File Name
    |--Recipes
    |  |--Recipe 1 (cf. recipe, indicated by ID, referenced to table RECIPES)
    |  |--Recipe 2
    |--num Recipes
'''

class Cookbook:

    def __init__(self, name, description, comment, file_name, recipes):
        self.name = name
        self.description = description
        self.comment = comment
        self.file_name = file_name
        self.recipes = recipes
        self.num_recipes = len(self.recipes)


    def update_num_recipes(self):
        self.num_recipes = len(self.recipes)

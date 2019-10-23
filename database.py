from cookbook import Cookbook

class Database:
    
    def __init__(self, file_name):
        self.file_name = file_name


    def load_data_base(self):
        pass

    def create_dummy_database(self):
        self.initialize_database()
        self.create_dummy_recipe()

    def initialize_database(self):
        # create three tables: meta, cookbook and recipes
        qry_meta = '''CREATE TABLE META(
                      CDATE        INT PRIMARY KEY NOT NULL,
                      NAME         TEXT NOT NULL,
                      DESCRIPTION  TEXT,
                      VERSION      TEXT);'''

        qry_cookbook = '''CREATE TABLE COOKBOOK(
                          ID          INT PRIMARY KEY IDENTITY,
                          NAME        TEXT NOT NULL,
                          DESCRIPTION TEXT,
                          COMMENT     TEXT,
                          NUMRECIPES  INT);'''
        qry_recipes = '''CREATE TABLE RECIPES(
                          ID              INT PRIMARY KEY IDENTITY,
                          NAME            TEXT NOT NULL,
                          COMMENT         TEXT,
                          NUMPORTIONS     INT,
                          INGREDIENTS     TEXT,
                          INSTRUCTIONS    TEXT,
                          RATING          INT,
                          DIFFICULTY      INT,
                          PREPARATIONTIME INT,
                          CUISINE         CHAR(50));'''


    def create_dummy_recipe(self):
        # add dummy cookbook
        qry_cookbook = '''INSERT INTO COOKBOOK (NAME, DESCRIPTION, 
                          COMMENT, NUMRECIPES)
                          VALUES ('Cookbook1', 
                                  'A description on the cookbook', 
                                  'A comment on the cookbook', 1);'''

        # add dummy recipe
        qry_recipe = '''INSERT INTO RECIPES (NAME, COMMENT, 
                        INGREDIENTS, INSTRUCTIONS, RATING, DIFFICULTY,
                        PREPARATIONTIME, CUISINE)
                        VALUES ('Recipe1', 'A comment on the recipe', 
                        '1;kg;joy;2;liter;beer',
                        'drink beer and have the joy', 5, 1, 10, 
                        'Bavarian');'''
    

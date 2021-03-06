from cookbook import Cookbook
import sqlite3 # https://docs.python.org/3/library/sqlite3.html
import base64
from PIL import Image
from io import BytesIO


class Database:
    
    def __init__(self, file_name):
        self.file_name = file_name

    def query_db(self, query):
        self.conn = sqlite3.connect(self.file_name)
        self.c = self.conn.cursor()
        self.c.execute(query)
        if query.find('select') > -1:
            result = self.c.fetchall()
            self.conn.commit()
            self.conn.close()
            return result
        self.conn.commit()
        self.conn.close()

    def load_data_base(self):
        # meta = self.query_db("select * from meta;")
        # print(meta)
        # cookbook = self.query_db("select * from cookbook;")
        # print(cookbook)
        self.recipes = self.query_db("select * from recipes;")
        # print(self.recipes)
        
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
        self.query_db(qry_meta)

        qry_cookbook = '''CREATE TABLE COOKBOOK(
                          ID          INT PRIMARY KEY,
                          NAME        TEXT NOT NULL,
                          DESCRIPTION TEXT,
                          COMMENT     TEXT,
                          NUMRECIPES  INT);'''
        self.query_db(qry_cookbook)
        qry_recipes = '''CREATE TABLE RECIPES(
                          ID              INTEGER PRIMARY KEY AUTOINCREMENT,
                          NAME            TEXT NOT NULL,
                          COMMENT         TEXT,
                          NUMPORTIONS     INT,
                          INGREDIENTS     TEXT,
                          INSTRUCTIONS    TEXT,
                          RATING          INT,
                          DIFFICULTY      INT,
                          PREPARATIONTIME INT,
                          IMAGE           TEXT,
                          CUISINE         CHAR(50));'''
        self.query_db(qry_recipes)
 

    def create_dummy_recipe(self):
        # add dummy cookbook
        qry_cookbook = '''INSERT INTO COOKBOOK (NAME, DESCRIPTION, 
                          COMMENT, NUMRECIPES)
                          VALUES ('Cookbook1', 
                                  'A description on the cookbook', 
                                  'A comment on the cookbook', 1);'''
        self.query_db(qry_cookbook)

        # add dummy recipe
        qry_recipe = '''INSERT INTO RECIPES (NAME, COMMENT, 
                        INGREDIENTS, INSTRUCTIONS, RATING, DIFFICULTY,
                        PREPARATIONTIME, CUISINE)
                        VALUES ('Recipe1', 'A comment on the recipe', 
                        '1;kg;joy;2;liter;beer',
                        'drink beer and have the joy', 5, 1, 10, 
                        'Bavarian');'''
        self.query_db(qry_recipe)
        self.query_db(qry_recipe)


    def encode_image(self, image_file):
        # base64 encode image
        # https://stackoverflow.com/q/3715493/3250126
        with open(image_file, "rb") as image_file: 
            encoded_image = base64.b64encode(image_file.read())
        return encoded_image

    def decode_image(self, encoded_string):
        image = Image.open(BytesIO(base64.b64decode(data)))
        # im.save('image1.png', 'PNG')
        return image

   

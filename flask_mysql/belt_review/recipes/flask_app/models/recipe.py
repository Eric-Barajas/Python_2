# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database

DATABASE = 'recipes_shema'

class Recipe:
    def __init__( self , data ):
        self.id = data['id']
        self.user_id = data['user_id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.recipe_timing = data['recipe_timing']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    
    #! CREATE
    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (user_id, name, description, instructions, recipe_timing) VALUES (%(user_id)s ,%(name)s, %(description)s, %(instructions)s, %(recipe_timing)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    #! READ (ALL)
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of friends
        recipes = []
        # Iterate over the db results and create instances of friends with cls.
        for recipe in results:
            recipes.append( cls(recipe) )
            # indide the parenthesis is DATABASE and Query
        return recipes

    #! READ (ONE)
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])

    #! UPDATE
    @classmethod
    def update(cls, data):
        print("***************** in Recipe.update")
        query = "UPDATE recipes SET user_id = %(user_id)s , name = %(name)s, description = %(description)s, instructions = %(instructions)s , recipe_timing = %(recipe_timing)s WHERE id = %(id)s;"
        connectToMySQL(DATABASE).query_db(query, data)
        # getting back a list of dictionaries
        
        # want the first result in the list

    #! DELETE
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
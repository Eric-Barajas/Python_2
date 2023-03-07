# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
# TODO import the Pet class to be used below
from flask_app.models.ninja import Ninja

DATABASE = 'dojos_and_ninjas_schema'

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.ninjas = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    
    #! CREATE
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    #! READ (ALL)
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of friends
        dojos = []
        # Iterate over the db results and create instances of friends with cls.
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    #! READ (ONE)
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])

    #! READ ONE WITH MANY
    @classmethod
    def get_one_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        dojo = Dojo(results[0])
        for result in results:
            temp_ninja = {
                'id' : result['ninjas.id'],
                'dojo_id' : result['dojo_id'],
                'first_name' : result['first_name'],
                'last_name' : result['last_name'],
                'age' : result['age'],
                'created_at' : result['ninjas.created_at'],
                'updated_at' : result['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(temp_ninja))
        return dojo

    #! UPDATE
    @classmethod
    def update(cls, data):
        print("***************** in Dojo.update")
        query = "UPDATE dojos SET name = %(name)s WHERE id = %(id)s;"
        connectToMySQL(DATABASE).query_db(query, data)
        # getting back a list of dictionaries
        
        # want the first result in the list

    #! DELETE
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
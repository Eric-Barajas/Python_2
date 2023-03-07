# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database

DATABASE = 'dojos_and_ninjas_schema'

class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.dojo_id = data['dojo_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    
    #! CREATE
    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (dojo_id, first_name, last_name, age) VALUES (%(dojo_id)s ,%(first_name)s, %(last_name)s, %(age)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    #! READ (ALL)
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of friends
        ninjas = []
        # Iterate over the db results and create instances of friends with cls.
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas

    #! READ (ONE)
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])

    #! UPDATE
    @classmethod
    def update(cls, data):
        print("***************** in Ninja.update")
        query = "UPDATE ninjas SET dojo_id = %(dojo_id)s , first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s WHERE id = %(id)s;"
        connectToMySQL(DATABASE).query_db(query, data)
        # getting back a list of dictionaries
        
        # want the first result in the list

    #! DELETE
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
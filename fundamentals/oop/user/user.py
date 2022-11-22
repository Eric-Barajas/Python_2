class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.gold_card_points)
        return self
# Have this method print all of the users' details on separate lines.

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200 
        return self
# Have this method change the user's member status to True 
# and set their gold card points to 200.

    def spend_points(self, amount):
        self.gold_card_points -= amount
        return self
# Have this method decrease the user's 
# points by the amount specified.

cole = User('cole','jacobs','cole@gmail.com',23)
aaron = User('aaron','andrews','aaron@gmail.com',41)


cole.display_info().enroll().spend_points(50).display_info()
aaron.enroll().spend_points(80).display_info()

# cole.display_info()
# cole.enroll()
# cole.spend_points(50)


# aaron.display_info()
# aaron.enroll()
# aaron.spend_points(80)





# Add the display_info(self) method to the User class

# In the outer scope, create a user instance and call the display_info method to test.

# Add the enroll method to the User class, implement and test by calling the method on the user in the outer scope.

# Make 2 more instances of the User class.

# Implement the spend_points(self, amount) method

# Have the first user spend 50 points

# Have the second user enroll.

# Have the second user spend 80 points

# Call the display method on all the users.

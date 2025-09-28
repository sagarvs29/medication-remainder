# methods
class Dog:
    # Constructor method (init method)
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.tricks = []

    # Instance method to make the dog bark
    def bark(self):
        print(f"{self.name} is barking!")

    # Instance method to add a trick to the dog's list of tricks
    def learn_trick(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}")

    # Instance method to display information about the dog
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Tricks: {', '.join(self.tricks)}")

# Creating instances (objects) of the Dog class
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Poodle")

# Calling methods on the dog objects
dog1.bark()
dog1.learn_trick("Sit")
dog1.learn_trick("Roll over")
dog1.display_info()

dog2.bark()
dog2.learn_trick("Fetch")
dog2.display_info()

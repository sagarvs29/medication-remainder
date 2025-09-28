from dog import Dog

#  Creating instances (objects) of the Dog class
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

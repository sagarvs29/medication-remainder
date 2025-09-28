
import turtle
import random

# Function to move a turtle forward by a random distance
def move_turtle(turtle_obj):
    distance = random.randint(1, 10)
    turtle_obj.forward(distance)

# Function to close the window and exit the program
def close_game():
    window.bye()

# Create a window
window = turtle.Screen()
window.title("Turtle Racing Game")
window.bgcolor("white")

# Create multiple turtles for racing
num_turtles = 6
turtles = []

for i in range(num_turtles):
    turtle_obj = turtle.Turtle()
    turtle_obj.shape("turtle")
    turtle_obj.color("blue")
    turtle_obj.penup()
    turtle_obj.goto(-100, 40 * i - 80)
    turtles.append(turtle_obj)

# Create a finish line
finish_line = turtle.Turtle()
finish_line.penup()
finish_line.goto(250, -150)
finish_line.pendown()
finish_line.goto(250, 250)

# Keyboard binding to close the window
window.listen()
window.onkeypress(close_game, "Escape")

# Main race loop
winner = None
while winner is None:
    for turtle_obj in turtles:
        move_turtle(turtle_obj)

        # Check if a turtle has crossed the finish line
        if turtle_obj.xcor() > 230:  # Adjusted position to be within bounds
            winner = turtles.index(turtle_obj) + 1
            print(f"Turtle {winner} wins!")
            break

window.mainloop()
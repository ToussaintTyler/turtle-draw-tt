import turtle
import math

TEXTFILENAME = 'turtle-draw.txt'

TEXTFILENAME = input("Enter the name of the input file: ")

total_distance = 0.0
previous_point = None

with open(TEXTFILENAME, 'r') as file:
        for line in file:
             parts = line.strip().split()

screen = turtle.Screen()
screen.title("Turtle Draw")
screen.setup(width=450, height=450)

t = turtle.Turtle()
t.speed(10)
t.penup()

turtleDrawTextfile = open(TEXTFILENAME, 'r')
line = turtleDrawTextfile.readline()
while line:
    print(line, end='')
    parts = line.split(' ')

    if (len(parts) == 3):
        color = parts[0]
        x = int(parts[1])
        y = int(parts[2])

        t.color(color)
        t.goto(x,y)

        if previous_point is not None:
                dx = x - previous_point[0]
                dy = y - previous_point[1]
                distance = math.sqrt(dx**2 + dy**2)
                total_distance += distance

        t.pendown()
        previous_point = (x, y)

    if (len(parts) == 1):
        t.penup()
        previous_point = None

    line = turtleDrawTextfile.readline()

t.penup()
t.goto(150, -200)
t.color("pink")
t.write(f"Total Distance: {total_distance: .2f}", align="right", font=("Arial", 10, "bold"))

input("\nPress Enter to close window...")

turtle.bye()

turtleDrawTextfile.close()

print('\nEnd')

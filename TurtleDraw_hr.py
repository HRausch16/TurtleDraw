# TurtleDraw
# Reading a text file line by line and execute.
#
# By: Hannah Rausch
#

TEXTFILENAME = input('Please input text file name: ')

import turtle

turtleScreen = turtle.Screen()
turtleScreen.setup(450, 450)
def f1():
    print('\nThanks for using Fenrir!\n')
    turtleScreen.bye()

print('Processing your masterpiece...\n')

fenrir = turtle.Turtle()
fenrir.speed(10)
fenrir.penup()

d = [] # Chose to use d to ensure no confusion to program

print('Reading your masterpiece instructions line by line...\n')
turtleDrawTextfile = open(TEXTFILENAME, 'r')
line = turtleDrawTextfile.readline()
while line:
    print(line, end='')
    parts = line.split(' ')

    if (len(parts) == 3):
        color = parts[0]
        x = int(parts[1])
        y = int(parts[2])

        d.append(fenrir.distance(x,y))

        fenrir.color(color)
        fenrir.goto(x,y)
        
        fenrir.pendown()
        
    else: # Assumes that a single word on a line is "Stop"
        fenrir.penup()

    line = turtleDrawTextfile.readline()

fenrir.penup()
fenrir.goto(150,-200)

totalDistance = 0
for D in d:
    totalDistance += D

fenrir.write('Total distance marked = %d' % (totalDistance), align='right')

print('\nEnd. Please press "Enter" to exit.')

turtleScreen.onkey(f1, 'Return')
turtleScreen.listen()
turtleScreen.mainloop()

turtle.done()
turtleDrawTextfile.close()



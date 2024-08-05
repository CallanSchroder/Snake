import turtle
from turtle import Turtle, position

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:


    def __init__(self) :
     self.my_turtles = []
     self.create_snake()
     self.head = self.my_turtles[0]

    def create_snake(self):
        for POSITION in START_POS:
            self.add_segment(position)

    def add_segment(self):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.speed("fastest")
        tim.goto(position)
        self.my_turtles.append(tim)

    def extend(self):
        self.add_segment(self.my_turtles[-1].position())




    def move(self):
        for turt_num in range(len(self.my_turtles) - 1, 0, -1):
            new_x = self.my_turtles[turt_num - 1].xcor()
            new_y = self.my_turtles[turt_num - 1].ycor()
            self.my_turtles[turt_num].goto(new_x, new_y)
        self.my_turtles[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.my_turtles[0].setheading(UP)



    def down(self):
        if self.head.heading() != UP:
            self.my_turtles[0].setheading(DOWN)


    def left(self):
        if self.head.heading() != RIGHT:
            self.my_turtles[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.my_turtles[0].setheading(RIGHT)



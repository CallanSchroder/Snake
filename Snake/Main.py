from turtle import Screen, Turtle
from snake import Snake
from Food import Food
import time
from snake import Snake
from Score import Score

screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("SnakieSnake")
screen.tracer(0)

my_turtles = []
start_pos = [(0,0), (-20, 0), (-40,0)]

snake = Snake()
food = Food()
score = Score()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        score.clear()
        score.new_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        score.game_over()

    for segment in snake.my_turtles:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_on = False













































screen.exitonclick()
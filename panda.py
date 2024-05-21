# Import Turtle Module
from turtle import Turtle, Screen

#Create Turtle Object

new_turtle = Turtle()
scren = Screen()

#Create a function to draw a circle with dynamic radius and color.

def draw_circle(radius, color):
    new_turtle.begin_fill()
    new_turtle.fillcolor(color)
    new_turtle.circle(radius)
    new_turtle.end_fill()

#Draw ears of Panda with black color circles.

draw_circle(15,"black")
new_turtle.penup()
new_turtle.forward(100)
new_turtle.pendown()
draw_circle(15,"black")

    

#Draw face of Panda with white color circle.
new_turtle.penup()
new_turtle.setpos(50,-50)    
new_turtle.pendown()
draw_circle(45, "white")    

#Draw eyes of Panda with black and white color concentric circles.

new_turtle.penup()
new_turtle.setpos(20,-10)  
draw_circle(10,"black")
new_turtle.penup()
new_turtle.setpos(20,-2)  
draw_circle(3,"white")

new_turtle.penup()
new_turtle.setpos(80,-10)  
new_turtle.pendown()
draw_circle(10,"black")
new_turtle.penup()
new_turtle.setpos(80,-2)  
draw_circle(3,"white")
new_turtle.hideturtle()

#Draw nose of Panda with black color circle.

new_turtle.penup()
new_turtle.setpos(50,-25)  
draw_circle(7,"black")

#Draw two semicircle for mouth below nose.

new_turtle.up()
new_turtle.setpos(50, -25)
new_turtle.down()
new_turtle.right(90)
new_turtle.circle(5, 180)
new_turtle.up()
new_turtle.setpos(50, -25)
new_turtle.down()
new_turtle.left(360)
new_turtle.circle(5, -180)
new_turtle.hideturtle()










scren.exitonclick()

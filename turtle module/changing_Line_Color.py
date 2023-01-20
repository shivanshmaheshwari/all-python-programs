import turtle 

painter = turtle.Turtle()

painter.pencolor("blue")
painter.speed(10)
for i in range(50):
    painter.forward(50)
    painter.left(123) #  counterclockwise 
    
painter.pencolor("red")
for i in range(50):
    painter.forward(100)
    painter.left(123)
    
turtle.done()
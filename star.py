import turtle
shivi = turtle.Turtle()
rainbow = ["red","orange","yellow","green","blue","purple"]
shivi.width(5)
shivi.speed(0)
shivi.penup()
shivi.back(50)
shivi.pendown()
for color in rainbow:
    shivi.color(color)
    for side in [1, 2, 3, 4, 5]:
        shivi.forward(50)
        shivi.right(144)
    shivi.right(60)
    shivi.penup()
    shivi.forward(60)
    shivi.pendown()
shivi.hideturtle()        

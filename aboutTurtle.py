import turtle

# s = turtle.Screen()
# s.bgcolor('orange')
# p = turtle.Pen()
# p.forward(100)
# p.left(120)
# p.forward(100)
# p.left(120)
# p.forward(100)
# p.left(120)


# s.exitonclick()


# EXERCISE 1 :  مثلت بالا و پایین بکشید
# 2 : پنجضلعی بکشید
# 3 : شش ضلعی بکشید

s = turtle.Screen()
s.register_shape('strawberry.gif')
s.bgcolor('orange')
# s.bgpic('mario.png')
p = turtle.Pen()
# p.shape('turtle')
p.shape('strawberry.gif')
p.pencolor('red')
p.pensize(4)
p.circle(50)

s.exitonclick()

import turtle


s = turtle.Screen()
s.register_shape("strawberry.gif")
s.bgcolor('cyan')

p = turtle.Pen()
# p.shape('turtle')  # 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
p.shape('strawberry.gif')

p.forward(100)
p.left(120)
p.forward(100)
p.left(120)
p.forward(100)
p.left(120)

s.exitonclick()

import turtle

s = turtle.Screen()

p = turtle.Pen()

# draw first square
p.fillcolor('red')
p.begin_fill()
for i in range(4):
    p.fd(50)
    p.lt(90)
p.end_fill()

# go forward 50 steps
p.fd(50)

# draw second square
p.fillcolor('yellow')
p.begin_fill()
for i in range(4):
    p.fd(50)
    p.lt(90)
p.end_fill()
# go to (0, 0)
p.goto(0, 0)

# draw third square
p.fillcolor('green')
p.begin_fill()
for i in range(4):
    p.fd(50)
    p.rt(90)
p.end_fill()
# go forward 50 steps
p.fd(50)

# draw forth square
p.fillcolor('blue')
p.begin_fill()
for i in range(4):
    p.fd(50)
    p.rt(90)
p.end_fill()

s.exitonclick()

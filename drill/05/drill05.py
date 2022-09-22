import turtle as t

def end():
    t.bye()
    
def down():
    t.setheading(270)
    t.forward(50)
    
def up():
    t.setheading(90)
    t.forward(50)

def right():
    t.setheading(0)
    t.forward(50)

def left():
    t.setheading(180)
    t.forward(50)
    
t.listen()    
t.shape("turtle")
t.onkeypress(right,"D")
t.onkeypress(left,"A")
t.onkeypress(end,"Escape")
t.onkeypress(up,"W")
t.onkeypress(down,"S")

from turtle import *

#we want to paint a house
speed(100)
#steo 1: draw a square
width(7)
color("blue")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door


forward(70)
color("black")
begin_fill()
left(90)
forward(100)   #height of the door
right(90)
forward(60)
right(90)
forward(100)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of the roof


#drawing windows
#drawing left window
penup()
goto(20, 170)  
setheading(0)
pendown()
color("brown")
begin_fill()

forward(40)
        
right(90)
forward(40)
        
right(90)
forward(40)
        
right(90)
forward(40)
        
right(90)

end_fill()




# Drawing right window
penup()
goto(140,130)      # Moved to the right side
setheading(0)
pendown()
begin_fill()

forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)

end_fill()

    
exitonclick()
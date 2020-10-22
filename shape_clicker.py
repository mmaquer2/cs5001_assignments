'''
Michael Maquera
CS 5001
Fall 2020
shaper clicker.py

'''

import turtle as t
import positionservice as posserv



#create the screen to the proper size
#create the turtle element declared to the letter " C " 

c = t.Turtle()
t.setup(970,635)
screen = t.Screen()


#create the circle turtle and draw it at the origin 0,0
c.setx(0)
c.sety(0)
c.ht()
c.pencolor("green")
c.circle(80)
c.speed(0)

def check_circle(x,y):
#calculate the current area of the circle
   print(x,y)
   x_radius_pos = x + 10
   x_radius_neg = x - 10
   y_radius_pos = y + 8
   y_radius_neg = y - 10
   
#if user has clicked inside the area of the circle, hide the drawing
   if((c.xcor() < x_radius_pos) and (c.ycor() < y_radius_pos)) or ((c.xcor() > x_radius_neg) and (c.ycor() > y_radius_neg)):   
       c.clear()
       posserv.set_visible( False )
       print('circle is hidden')     
   else:
#if the user has clicked on the screen that is not inside the circle, draw a new circle at that coordinate
        move_circle(x,y)
        
def move_circle(x,y):
    #go to the onclick coordinate and draw a new circle
    c.penup()
    c.goto(x,y)
    c.clear()
    c.penup()
    c.goto(x,y)
    c.pendown()
    c.pencolor("green")
    c.ht()
    c.circle(80)
    new_coor = c.pos()
    print('circle has now moved to coordinates ', new_coor)

#when screen is clicked run the check circle function
screen.onscreenclick(check_circle, 1)

screen.mainloop()









   
    

 




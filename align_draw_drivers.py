'''
Michael Maquera
CS 50001
Fall 2020

align_draw_drivers.py

'''



def init_shape():
    import turtle

     
# draw the square
    #create the square with the turtle function
    square = turtle.Turtle()
    square.shape("square")
    square.color('red')
    #create the square with a size of 80
    square.shapesize(8,10)
    # set the location of the square (0,0)
    square.sety(0)
    square.setx(0)



# draw the circle
    circle = turtle.Turtle() 
    circle.shape("circle")
    circle.color('blue')
    #create the cricle within the square
    circle.shapesize(8,10)
    #
    circle.sety(0)
    circle.setx(-0)

    control_shapes(square,circle)

    


def control_shapes(square, cricle):

    s = square
    c = cricle

#get user input based on where to move shapes based on x and y coordinates
    x_square = int(input('where do you want to move the square left/right in pixels ' ))
    y_square = int(input('where do you want to move the square up/doown in pixels ' ))

    x_circle = int(input('where do you want to move the circle left/right in pixels '))
    y_circle = int(input('where do you want to move the circle up/down in pixels ' ))

    move_shapes(s,c,x_square,y_square,x_circle,y_circle)

def move_shapes(square,circle,x_square,y_square,x_circle,y_circle):

#move the shapes based on user input
    # the up and down, function removes the line when
    #moving shapes
    square.up()
    #move the square to the new x and y coordinates
    square.goto(x_square, y_square)
    square.down()

    circle.up()
    #move the circle to the new c and y coordinates
    circle.goto(x_circle, y_circle)
    circle.down()

#end



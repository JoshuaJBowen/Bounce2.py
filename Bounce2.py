#Bounce2 (with OOP)
#Josh Bowen
#4/30/2022

import turtle
import random

class Ball():

    def __init__(self, name, color, distance, bounds):
        self.name = name
        self.distance = distance
        self.bounds = bounds
        self.xcor = 0 #random.randint(self.bounds[3],self.bounds[1])
        self.ycor = 0 #random.randint(self.bounds[2],self.bounds[0])
        self.heading = random.randrange(0,360)
        
        self.name = turtle.Turtle()
        self.name.color(color)
        self.name.speed(0)
        self.name.shape("circle")
        self.name.up()
        self.name.goto(self.xcor, self.ycor)
        self.name.lt(self.heading)
        self.name.down()

    def forward(self):
        self.name.forward(self.distance)
        self.xcor = int(self.name.xcor())
        self.ycor = int(self.name.ycor())

    def bounce(self):
        #side wall collision formula:
        if abs(self.xcor) > abs(self.ycor):
            self.heading = (180 - self.heading)%360

        #top or bottom wall collision formula:
        else:
            self.heading = (360 - self.heading)%360
        self.name.seth(self.heading)
        
    def close(self):
        close = False

        if abs(self.bounds[0]) - abs(self.ycor) < self.distance:
            if self.heading > 0 and self.heading < 180:
                close = True
        if abs(self.bounds[1]) - abs(self.xcor) < self.distance:
            if self.heading < 90 or self.heading > 270:
                close = True
        if abs(self.bounds[2]) - abs(self.ycor) < self.distance:
            if self.heading > 180 and self.heading < 360:
                close = True
        if abs(self.bounds[3]) - abs(self.xcor) < self.distance:
            if self.heading > 90 and self.heading < 270:
                close = True
        
        return close

    def inside(self):
        if self.xcor >= self.bounds[3] and self.xcor <= self.bounds[1] and self.ycor >= self.bounds[2] and self.ycor <= bounds[0]:
            return True
        else:
            return False
            
def main(bound_list):
    #assume tbound > bbound and rbound > lbound
    #assume bound_list goes top, right, bottom, left
    
    wn = turtle.Screen()
    wn.bgcolor("Black")
    
    bound = turtle.Turtle()
    bound.color("White")
    bound.speed(0)
    bound.width(5)
    bound.ht()
    bound.up()
    bound.goto(bound_list[3], bound_list[2])
    bound.down()
    bound.goto(bound_list[1], bound_list[2])
    bound.goto(bound_list[1], bound_list[0])
    bound.goto(bound_list[3], bound_list[0])
    bound.goto(bound_list[3], bound_list[2])

    distance = 10
    tennis_ball = Ball("ball", "lightgreen", distance, bound_list)

    while tennis_ball.inside():
        if tennis_ball.close():
            tennis_ball.bounce()
        tennis_ball.forward()

#only works well with squares evenly spaced in the four quadrants
bounds = [300, 300, -300, -300]
main(bounds)

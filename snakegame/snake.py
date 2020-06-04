import turtle
import time,random
delay=0.2
score=0
high_score=0
#set up the screen

wn=turtle.Screen()
wn.title("Snake game by mohnish")
wn.bgcolor("green")
wn.setup(width=600,height=600)
wn.tracer(0)
# snake head
head=turtle.Turtle()
head.speed(0) # moves head as fast as possible
head.shape("square")
head.color('black')
head.penup()#doesnt draw lines on the screen
head.goto(0,0)#start from center of the srcreen
head.direction="stop" #stays there or else it would be dynamic
# set the score and hifh_score
pen=turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.penup()
pen.color('white')
pen.hideturtle()
pen.goto(0,260)
pen.write("Score:0 High_Score:0",align='center',font=('courier',18,'normal'))
# snake food
food=turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0,100)

segments=list()
# function
def go_up():
    if head.direction !='down':
        head.direction='up'
def go_down():
    if head.direction !='up':
        head.direction='down'
def go_right():
    if head.direction != 'left':
        head.direction='right'
def go_left():
    if head.direction != 'right':
        head.direction="left"

def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=='down':
        y=head.ycor()
        head.sety(y-20)
    if head.direction=='right':
        x=head.xcor()
        head.setx(x+20)
    if head.direction=='left':
        x=head.xcor()
        head.setx(x-20)
# keyboard bindings
wn.listen()
wn.onkeypress(go_up,'w')
wn.onkeypress(go_down,'s')
wn.onkeypress(go_right,'d')
wn.onkeypress(go_left,'a')
wn.onkeypress(go_up,'Up')
wn.onkeypress(go_down,'Down')
wn.onkeypress(go_right,'Right')
wn.onkeypress(go_left,'Left')

#main game
while True:
    wn.update()
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor() <-290:
        time.sleep(0.7)
        head.goto(0,0)
        head.direction='stop'
        #hide the segments
        for segment in segments:
            segment.goto(1000,1000)

        #clear the segment list
        segments.clear()

        # reset the score
        score=0
        pen.clear()
        pen.write("Score:{} High_Score:{}".format(score, high_score), align='center', font=('courier', 18, "normal"))
        #reset the delay as snakeis faster when it consumes food
        delay=0.2
    if head.distance(food) <20:
        # move the food to random position
        x=random.randint(-285,285)
        y=random.randint(-285,285)
        food.goto(x,y)
        # add a segment
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.color('grey')
        new_segment.shape('square')
        new_segment.penup()
        segments.append(new_segment)

        #shorten the delay time bcoz as snake increases programme gtes slow
        delay -=0.001
        #increase the score

        score+=10

        if score> high_score:
            high_score=score
        pen.clear()
        pen.write("Score:{} High_Score:{}".format(score,high_score),align='center',font=('courier',18,"normal"))

        #appending new box after having food in reverse manner
    for index in range(len(segments)-1,0,-1): #still 0 is excluded
         x=segments[index-1].xcor()
         y=segments[index-1].ycor()
         segments[index].goto(x,y)
        #move segment zero to where the head is
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
    move()
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(0.7)
            head.goto(0,0)
            head.direction='stop'
            #hide the segments
            for segment in segments:
                segment.goto(1000,1000)
                #clear the segments
                segment.clear()
            # reset the core
            score=0
            pen.clear()
            pen.write("Score:{} High_Score:{}".format(score, high_score), align='center',
                      font=('courier', 18, "normal"))

            # reset the delay as snakeis faster when it consumes food
            delay = 0.2
    time.sleep(delay)

wn.mainloop()


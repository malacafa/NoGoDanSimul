import turtle as t
import random

plantArray=[]
t.bgcolor("orange")
file = open("file.txt","w")
def tdefault():
    t.speed(0)
    t.pensize(3)
    t.hideturtle()
    
def Printmap():
    tdefault()
    t.penup()
    t.goto(0,-300)
    t.pendown()
    t.color(0,1,0)
    t.begin_fill()
    t.circle(300)
    t.end_fill()
    
def turtleDistance(x,y):
    tdefault()
    t.penup()
    t.goto(x,y)
    return t.distance(0,0)

def isrange(x,y):
    tdefault()
    t.penup()
    for i,j in plantArray:
        if abs(i-x)<50 and abs(j-y)<50:
            t.goto(i,j)
            if t.distance(x,y)<20:
                return 1
    return 0

def setPlant():
    tdefault()
    index=0
    x=random.randrange(-300,300)
    y=random.randrange(-300,300)
    for _ in range(10):
        while 270<=turtleDistance(x,y) or [x,y] in plantArray or isrange(x,y):
            x=random.randrange(-300,300)
            y=random.randrange(-300,300)
        plantArray.append([x,y])
        t.goto(x,y)
        t.pendown()
        t.color(1,0,0)
        t.begin_fill()
        t.circle(7)
        t.end_fill()
        print(index+1,":plant planted")
        index+=1
        
Printmap()
setPlant()

FRAMERATE=100000

setkey=int(input("[1]방치 [2]선택적 보존(관람객 허용) [3]전적 보존(관람객 불가)"))

if setkey==1:
    die=0.1
    grow=0.9
    
if setkey==2:
    die=0.25
    grow=0.7

if setkey==3:
    die=0.4
    grow=0.5
    
for runtime in range(FRAMERATE):
    appendArray=[]
    deleteArray=[]
    print("FRAME:::",runtime,"FOR_NUM:::",len(plantArray))
    line = '%d %d'%(runtime,len(plantArray))
    file.write(line)
    if runtime%10==1:    
        print("winter")
    for x,y in plantArray:
        if random.random()>0.5:
            pgrow=random.random()
            pdie=random.random()
            if runtime%10==1:
                pgrow=1
                pdie-=0.05
            if pdie<die:
                tdefault()
                t.penup()
                t.goto(x,y)
                t.color(0,1,0)
                t.begin_fill()
                t.circle(7)
                t.end_fill()
                deleteArray.append([x,y])
            elif pgrow<grow:
                tdefault()
                xx=random.randrange(0,31)-15
                yy=random.randrange(0,31)-15
                t.penup()
                t.goto(xx+x,yy+y)
                if [xx+x,y+yy] not in plantArray and 300>t.distance(0,0):   
                    tdefault()
                    t.penup()
                    t.goto(x+xx,y+yy)
                    appendArray.append([x+xx,y+yy])
                    t.color(1,0,0)
                    t.begin_fill()
                    t.circle(7)
                    t.end_fill()
    for x,y in appendArray:
        if [x,y] not in plantArray:
            plantArray.append([x,y])
    for x,y in deleteArray:
        del plantArray[plantArray.index([x,y])]
    
        

    
        





        
        

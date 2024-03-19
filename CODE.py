from time import sleep
import turtle
import math
import random
wn=turtle.Screen()
wn.title("LABYRINTHE")
wn.bgcolor("black")
wn.setup(1000,1000)
turtle.register_shape("wall1.gif")
turtle.register_shape("dragon1.gif")
def labyFromFile(fn) :
    f = open(fn)
    laby = []
    indline = 0
    for fileline in f:
        labyline = []
        inditem = 0
        for item in fileline:
            if item == ".":
                labyline.append(0)
            elif item == "#":
                labyline.append(1)
            elif item == "x":
                labyline.append(0)
                mazeIn = [indline, inditem]
            elif item == "X":
                labyline.append(0)
                mazeOut = [indline, inditem]
            inditem += 1
        laby.append(labyline)
        indline += 1
    f.close()
    return [laby, mazeIn, mazeOut]
def afficheTextuel(l):
    liste=[]
    c1=0
    for y in l[0]:
        g=""
        c=0
        for x in y:
            if x==1:
                g=g+"X"
            elif x==0: 
                if c==l[2][1] and c1==l[2][0]:
                    g=g+"F"
                elif c==l[1][1] and c1==l[1][0]:
                    g=g+"S"
                else:
                    g=g+" "
            c=c+1
        c1=c1+1
        liste.append(g)
    return liste
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("dragon1.gif")
        self.color("blue")
        self.penup() 
        self.speed(0)
        self.gold=0
    global autot
    def go_up(self):
        move_to_x=player.xcor()
        move_to_y=player.ycor()+24
        if (move_to_x,move_to_y) not in walls and autot==False and inverse==False:
            revese.append("down")
            self.goto(move_to_x,move_to_y)
    def go_down(self):
        move_to_x=player.xcor()
        move_to_y=player.ycor()-24
        if (move_to_x,move_to_y) not in walls and autot==False and inverse==False:
            revese.append("up")
            self.goto(move_to_x,move_to_y)      
    def go_right(self):
        move_to_x=player.xcor()+24
        move_to_y=player.ycor()
        if (move_to_x,move_to_y) not in walls and autot==False and inverse==False:
            revese.append("left") 
            self.goto(move_to_x,move_to_y)      
    def go_left(self):
        move_to_x=player.xcor()-24
        move_to_y=player.ycor()
        if (move_to_x,move_to_y) not in walls and autot==False and inverse==False:
            revese.append("right")
            self.goto(move_to_x,move_to_y)
    def is_collision(self,other):
        a=self.xcor()-other.xcor()
        b=self.ycor()-other.ycor()
        distance=math.sqrt((a**2)+(b**2))
        if distance<5:
            return True
        else:
            return False
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()
    def move(self,direction):
        if direction=="up":
            dx=0
            dy=24
        elif direction=="down":
            dx=0
            dy=-24
        elif direction=="left":
            dx=-24
            dy=0
        elif direction=="right":
            dx=24
            dy=0
        movex=self.xcor()+dx
        movey=self.ycor()+dy
        self.goto(movex,movey)
class Treasure(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold=100
        self.goto(x,y)
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()
class Enemy(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold=25
        self.goto(x,y)
        self.direction=random.choice(["up","down","left","right"])
    def move(self):
        if self.direction=="up":
            dx=0
            dy=24
        elif self.direction=="down":
            dx=0
            dy=-24
        elif self.direction=="left":
            dx=-24
            dy=0
        elif self.direction=="right":
            dx=24
            dy=0
        else:
            dx=0
            dy=0
        if self.is_close(player):
            if player.xcor()<self.xcor():
                self.direction="left"
            elif player.xcor()>self.xcor():
                self.direction="right"
            elif player.ycor()<self.ycor():
                self.direction="down"
            elif player.ycor()>self.ycor():
                self.direction="up" 
        movex=self.xcor()+dx
        movey=self.ycor()+dy
        if (movex,movey)not in walls and (movex,movey)not in treas:
            self.goto(movex,movey)
        else:
            self.direction=random.choice(["up","down","left","right"])
        turtle.ontimer(self.move,t=200)
    def is_close(self,other):
        a=self.xcor()-other.xcor()
        b=self.ycor()-other.ycor()
        distance=math.sqrt((a*a)+(b*b))
        if distance<100:
            return True
        else:
            return False
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()
class Score(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,300)
        self.write("Score: {}  Highscore: {}".format(player.gold,high_score),align="center",font=("Courier",24,"normal"))
k=0
levels=[]
level_2=[
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP XXXXXXX          XXXXX",
"X  XXXXXXX  XXXXXX  XXXXX",
"X       XX EXXXXXX EXXXXX",
"X       XX  XXX        XX",
"XXXXXX  XX  XXX E      XX",
"XXXXXX  XX  XXXXXX  XXXXX",
"XXXXXX  XX    XXXX  XXXXX",
"X  XXX        XXXXT XXXXX",
"X  XXX  XXXXXXXXXXXXXXXXX",
"X         XXXXXXXXXXXXXXX",
"XE               XXXXXXXX",
"XXXXXXXXXXXX     XXXXXT X",
"XXXXXXXXXXXXXXX  XXXXX  X",
"XXXT XXXXXXXXXX         X",
"XXX                     X",
"XXX         XXXXXXXXXXXXX",
"XXXXXXXXXX  XXXXXXXXXXXXX",
"XXXXXXXXXX             TX",
"XXT  XXXXXE             X",
"XX   XXXXXXxxxxxxx  XXXXX",
"XX    YXXXXXXXXXXX  XXXXX",
"XX          XXXX        X",
"XXXXE                   X",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]
level_0=[
"XXXXXXXXXXXXXXSX",
"X             PX",
"FTXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXX"
]
level_1=[
"XXXXXXXXXXXXXXX",
"X X XT        F",
"X X   XXXXXXXXX",
"XT  X         X",
"XXXXXXXXXXXXX X",
"XXXXXXXXXXXXX X",
"XT          X X",
"XXXXXXXXXXX   X",
"XT          X X",
"XXXXXXXXXXXXX X",
"SP            X",
"XXXXXXXXXXXXXXX"
]
levels.append(level_0)
levels.append(level_1)
levels.append(level_2)
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character=level[y][x]
            screen_x=-(24*round(len(level[0])/2))+(x*24)
            screen_y=(24*round(len(level)/2))-(y*24)            
            if character!='S' and character!='F':
                if character=="X":
                    pen.goto(screen_x,screen_y)
                    pen.shape("wall1.gif") 
                    pen.stamp()
                    walls.append((screen_x,screen_y))
                if character=="P":
                    pp.append(screen_x)
                    pp.append(screen_y)
                    player.goto(screen_x,screen_y)
                if character =="T":
                    treas.append((screen_x,screen_y))
                    treasures.append(Treasure(screen_x,screen_y))
                if character=="E":
                    enemies.append(Enemy(screen_x,screen_y))
            else:
                if character=='S':
                    j.shape("square")
                    j.penup()
                    j.speed(0)
                    walls.append((screen_x,screen_y))
                    j.goto(screen_x,screen_y)
                    starte.append(screen_x)
                    starte.append(screen_y)
                    j.color("green")
                    j.stamp()
                else:
                    p.shape("square")
                    p.penup()
                    p.speed(0)
                    p.goto(screen_x,screen_y)
                    final.append(screen_x)
                    final.append(screen_y)
                    p.color("red")
                    p.stamp()
                j.hideturtle()
                p.hideturtle()
def startbutton():
    b=turtle.Turtle()
    b.hideturtle()
    b.color("white")
    b.penup()
    b.goto(0,0)
    b.pendown()
    for i in range(2):
        b.forward(200)
        b.left(90)
        b.forward(50)
        b.left(90)
    b.penup()
    b.goto(10,5)
    b.write("START GAME",font=("Courier",18,"normal"))
    def buttonClick(x,y):
        if x>0 and x<200 and y>0 and y<50:
            global start
            start=True
    turtle.listen()
    turtle.onscreenclick(buttonClick,1)
def autobutton():
    b=turtle.Turtle()
    b.hideturtle()
    b.color("white")
    b.penup()
    b.goto(-600,100)
    b.pendown()
    for i in range(2):
        b.forward(100)
        b.left(90)
        b.forward(50)
        b.left(90)
    b.penup()
    b.goto(-590,100)
    b.write("Auto",font=("Courier",18,"normal"))
    def buttonClick(x,y):
        if x>=-600 and x<=-500 and y>=100 and y<=150:
            global autot
            autot=True
    global wn
    wn.listen()
    wn.onscreenclick(buttonClick,1)
def creatbutton():
    b=turtle.Turtle()
    b.hideturtle()
    b.color("white")
    b.penup()
    b.goto(-600,0)
    b.pendown()
    for i in range(2):
        b.forward(120)
        b.left(90)
        b.forward(50)
        b.left(90)
    b.penup()
    b.goto(-590,0)
    b.write("Create",font=("Courier",18,"normal"))
    def buttonClick(x,y):
        if x>=-600 and x<=-480 and y>=0 and y<=50:
            global creat
            creat=True
    global wn
    wn.listen()
    wn.onscreenclick(buttonClick,1)
def creature():
    cx=None
    s=turtle.Turtle()
    s.shape("square")
    s.color("green")
    s.penup()
    f=turtle.Turtle()
    f.shape("square")
    f.color("red")
    f.penup()
    m=turtle.Turtle()
    m.shape("wall1.gif")
    m.penup()
    t=turtle.Turtle()
    t.shape("circle")
    t.color("yellow")
    t.penup()
    e=turtle.Turtle()
    e.shape("circle")
    e.color("red")
    e.penup()
    m.goto(-600,300)
    m.stamp()
    m.hideturtle()
    t.goto(-600,200)
    t.stamp()
    t.hideturtle()
    e.goto(-600,100)
    e.stamp()
    e.hideturtle()
    s.goto(-600,0)
    s.stamp()
    s.hideturtle()
    f.goto(-600,-100)
    f.stamp()
    f.hideturtle()
    d={
        m:[-600,300],
        t:[-600,200],
        e:[-600,100]
    }
    def buttonClick(x,y):
        if x>-612 and x<-588 :
            if y<112 and y>88:
                global cx
                cx="e"
            elif y<212 and y>188:
                cx="t"
            elif y<312 and y>288:
                cx="m"
            elif y<12 and y>-12:
                cx="s"
            elif y<-88 and y>-112:
                cx="f"
        else: 
            z=pixel2cell(x,y)
            u=cell2pixel(z[0],z[1])
            x=u[0]
            y=u[1]
            if cx=="e":
                e.goto(x,y)
                e.stamp()
                e.goto(d[e][0],d[e][1])
            elif cx=="m":
                m.goto(x,y)
                m.stamp()
                m.goto(d[e][0],d[e][1])
            elif cx=="t":
                t.goto(x,y)
                t.stamp()
                t.goto(d[e][0],d[e][1])
            elif cx=="s":
                s.goto(x,y)
                s.stamp()
                s.goto(d[e][0],d[e][1])
            elif cx=="f":
                f.goto(x,y)
                f.stamp()
                f.goto(d[e][0],d[e][1])
    global wn
    wn.listen()
    wn.onscreenclick(buttonClick,1)
def pixel2cell(pos_x,pos_y):
    for y in range(-(len(levels[k])-(len(levels[k])//2)),(len(levels[k])//2)+1):
        z=-12
        if (z+(y*24))<=pos_y<=(-z+(y*24)):
            case_y=y
            for x in range(-(len(levels[k][0])-(len(levels[k][0])//2)),(len(levels[k][0])//2)+1):
                o=-12
                if (o+(24*x))<=pos_x<=(-o+(24*x)):
                    case_x=x
                    return [case_x,case_y]
    return "out of range"
def testclick(x,y):
    if not(x>=-600 and x<=-480 and y>=0 and y<=50)and not(x>=-600 and x<=-500 and y>=100 and y<=150):
        print(pixel2cell(x,y))
        print(identification(x,y))
        print(typecellule(x,y))
    elif x>=-600 and x<=-480 and y>=0 and y<=50:
        global creat
        creat=True
    elif x>=-600 and x<=-500 and y>=100 and y<=150:
        global autot
        autot=True
def cell2pixel(x,y):
    return [24*x,24*y]
def typecellule(x,y):
    l1=pixel2cell(x,y)
    l2=cell2pixel(l1[0],l1[1])
    if (l2[0],l2[1])in walls and (l2[0]not in starte or l2[1] not in starte):
        return "wall"
    elif (l2[0],l2[1])in treas:
        return "Treasure"
    elif l2[0]in starte and l2[1]in starte:
        return "Start"
    elif l2[0]in final and l2[1]in final:
        return "End"
    else:
        return ""
def identification(x,y):
    if isinstance(pixel2cell(x,y),list):    
        z=pixel2cell(x,y)
        t=cell2pixel(z[0],z[1])
        x=t[0]
        y=t[1]
        if (x,y) not in walls:
            if ((x-24,y)in walls and (x+24,y)in walls and(x,y+24) in walls)or((x,y-24)in walls and (x,y+24)in walls and(x+24,y) in walls)\
                or((x-24,y)in walls and (x+24,y)in walls and(x,y-24) in walls)or((x,y-24)in walls and (x,y+24)in walls and(x-24,y) in walls):
                return "impasse"
            elif ((x-24,y)in walls and (x+24,y)in walls) or ((x,y+24)in walls and (x,y-24) in walls):
                return "passage "
            else:
                return "carefour"
    return ""
p=turtle.Turtle()
j=turtle.Turtle()
high_score=0
start=False
auto=[
    ["left","left","left","left","left","left","left","left","left","left","left","left","down","left","left"],
    ["right","right","right","right","right","right","right","right","right","right","right","right",\
    "up","up","up","up","up","up","up","left","left","left","left","left","left","left","left","up","up",\
    "right","right","right","right","right","right","right","right","right"]
]
unit=[]
creat=False
while True:
        if start==False:
            wn.bgcolor("black")
            wn.tracer(0)
            startbutton()
            if start==True:
                wn.tracer(0)
                wn.clearscreen()
                wn.bgcolor("black")
        while start==True and creat==False:
            inverse=False
            starte=[]
            final=[]
            sleep(0.01)
            wn.bgcolor("black")
            wn.tracer(0)
            pen=Pen()
            player=Player()
            walls=[]
            treasures=[]
            treas=[]
            enemies=[]
            pp=[]
            revese=[]
            setup_maze(levels[k])
            print(-(len(levels[k][0])-round(len(levels[k][0])/2)),round(len(levels[k][0])/2))
            creat=False
            autot=False
            if k<2:
                autobutton()
            else:
                creatbutton()
            if autot==False:
                turtle.listen()
                turtle.onkey(player.go_left,"Left")
                turtle.onkey(player.go_right,"Right")
                turtle.onkey(player.go_up,"Up")
                turtle.onkey(player.go_down,"Down")
            score=Score()
            for enemy in enemies:
                turtle.ontimer(enemy.move,t=250)
            wn.update()
            while True:
                u=0
                wn.listen()
                wn.onscreenclick(testclick,1)
                for treasure in treasures:
                    if player.is_collision(treasure):
                        player.gold +=treasure.gold
                        score.clear()
                        if player.gold>high_score:
                            high_score=player.gold
                        score=Score()
                        treasure.destroy()
                        treasures.remove(treasure)
                for enemy in enemies:
                    if player.is_collision(enemy):
                        player.destroy()
                        u=1
                if creat==True:
                    break
                if autot==True:
                    player.hideturtle()
                    player.goto(pp[0],pp[1])
                    player.showturtle()
                    for i in auto[k]:
                        wn.tracer(0)
                        player.move(i)
                        for treasure in treasures:
                            if player.is_collision(treasure):
                                treasure.destroy()
                                treasures.remove(treasure)
                                break
                        wn.update()
                        sleep(0.2)
                    wn.tracer(0)
                if player.is_collision(p):
                    inverse=True
                    for i in revese[::-1]:
                        wn.tracer(0)
                        player.move(i)
                        wn.update()
                        sleep(0.2)                    
                    b=turtle.Turtle()
                    b.hideturtle()
                    b.penup()
                    b.pencolor("white")
                    b.goto(-30,0)
                    b.write("Bravo",font=("Courier",18,"normal"))
                    sleep(2)
                    u=1
                    k=k+1
                if u!=1:
                    wn.update()
                if u==1 :
                    break
            wn.clearscreen()
            wn.bgcolor("black")
            if creat==True:
                break
        if creat==True:
            break
if creat==True:
    wn.clearscreen()
    wn.bgcolor("black")
    wn.tracer(0)
    creature()
    wn.update()
    wn.mainloop()

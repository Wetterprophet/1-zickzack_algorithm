hght = 420
wdth = 1188
#size(1188,420)               #define window size - doesnt work unless in setup
inix = int(random(10,50))                    #define x as first value for loop
iniy1 = int(random(0,hght))    #define y1 as random between 0 and 420=height, no global value yet
#iniy2 = iniy1
iniy2 = int(random(0,hght))    #define y2 ---"--- , start values for first line
while iniy1 == iniy2 :
    iniy2 = int(random(0,hght))    #iniy1 and iniy2 shouldnt be the same value
cnt = 0                     #define count and assign value 0
x = 0
isw = int(random (1,3))    #initial strokeweight random


x_values=[]                 #create a list to hold the x values
y_values=[]                 #create a list to hold the y values







def setup():
    global x
    background(255)           #white bg (RGB)
    stroke(0)                 #black stroke
    size(wdth,hght)            #define window size
    x= inix

    strokeWeight(isw)
    line(inix, iniy1, inix, iniy2)   #draws the initial vertical line
    x_values.append(inix)
    x_values.append(inix)
    y_values.append(iniy1)
    y_values.append(iniy2)

    print("X",x_values,"Y", y_values)





#while cnt =< hour():




def draw():
 #   delay(2000)
    global x, inix, cnt, isw




    y=year()
    mo=month()
    d=day()
    h=hour()
    m=minute()
    s=second()
    timeframe = str(str(y)+"-"+str(mo)+"-"+str(d)+"-"+str(h)+":"+str(m)+":"+str(s))
 #   print(timeframe)




    while cnt<= second():

        loop()

        cnt=cnt+1
        print ('count',  cnt)



        colorMode(HSB, 255)       #set color mode to HSB - max value = 255
        hu= int(random(0,255))    #random color
        sa= int(random(150,255))
        br= int(random(150,255))
        op= int(random(50,200))
        stroke(hu,255,50,)

        y1= int(random(0,height))
        x1= int(random(inix, width))
        x_values.append(x1)
        y_values.append(y1)
        print("X",x_values,"Y", y_values)
        fill(hu,sa,br,op)
        strokeWeight(isw)           #define width of stroke
        beginShape()
        vertex(x_values[-3], y_values[-3])
        vertex(x_values[-2], y_values[-2])
        vertex(x_values[-1], y_values[-1])
        vertex(x_values[-3], y_values[-3])
        endShape()
        #saveFrame("1-4-####.png")








def mousePressed():
    noLoop()                 #Holding down the mouse activates looping

def mouseReleased():
    loop()                   #Releasing the mouse stops looping draw()

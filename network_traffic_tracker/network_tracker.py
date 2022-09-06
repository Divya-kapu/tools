from requests import *
import csv
from requests.adapters import HTTPAdapter
import turtle
t1 = turtle.Turtle()
screen = turtle.Screen()
line_count = 0
path = './ip_sheet.csv'


def session_with_retries(url):
     s = Session()
     s.mount(url,HTTPAdapter(max_retries=5))
     return s


def turtle_dotted_lines(x,y):
    print("turtle.xcor()" , turtle.xcor())
    print(x)
    print("turtle.ycor()", turtle.ycor())
    print(y)
    print("entered func")
    for _ in range(1000):
        print(x)
        print(y)
        print('turtle.xcor()', turtle.xcor())
        print('turtle.ycor()', turtle.ycor())
        if x < 0 and y < 0:
            print('if x < 0 and y < 0:')
            if turtle.xcor() <= x and turtle.ycor() <= y:
                print('if - if x < 0 and y < 0:')
                # if turtle.position() >= (x,y):
                break
            else:
                print('else - if x < 0 and y < 0:')
                turtle.pendown()
                if turtle.xcor() > x and turtle.ycor() > y:
                    print('else if - if x < 0 and y < 0:')
                    turtle.setheading(x)
                    turtle.setheading(y)
                    print(turtle.position())
                    turtle.speed('fastest')
                    turtle.forward(3)
                    turtle.penup()
                    turtle.hideturtle()
                else:
                    print('else else - if x < 0 and y < 0:')
                    print("else")
                    # turtle.goto(x, y)
                    turtle.penup()
                    turtle.goto(0, 0)
                    # turtle.tracer(n=2, delay=0)
                    # turtle.pendown()
                    break
        elif x > 0 and y > 0:
            print('x > 0 and y > 0')
            if turtle.xcor() >= x and turtle.ycor() >= y:
                print('if x > 0 and y > 0:')
                # if turtle.position() >= (x,y):
                break
            else:
                print('else x > 0 and y > 0:')
                turtle.pendown()
                if turtle.xcor() < x and turtle.ycor() < y:
                    print('else-if x > 0 and y > 0:')
                    turtle.setheading(x)
                    turtle.setheading(y)
                    print(turtle.position())
                    turtle.speed('fastest')
                    turtle.forward(3)
                    turtle.penup()
                    turtle.hideturtle()
                else:
                    print('else-else x > 0 and y > 0:')
                    print("else")
                    # turtle.goto(x, y)
                    turtle.penup()
                    turtle.goto(0, 0)
                    # turtle.tracer(n=2, delay=0)
                    # turtle.pendown()
                    break
        elif x < 0 and y > 0:
            print('if x < 0 and y > 0:')
            if turtle.xcor() <= x and turtle.ycor() >= y:
                print('if-if x < 0 and y > 0:')
                # if turtle.position() >= (x,y):
                break
            else:
                print('elae x < 0 and y > 0:')
                turtle.pendown()
                if turtle.xcor() > x and turtle.ycor() < y:
                    print('else-if x < 0 and y > 0:')
                    turtle.setheading(x)
                    turtle.setheading(y)
                    print(turtle.position())
                    turtle.speed('fastest')
                    turtle.forward(3)
                    turtle.penup()
                    turtle.hideturtle()
                else:
                    print('else-else x < 0 and y > 0:')
                    print("else")
                    # turtle.goto(x, y)
                    turtle.penup()
                    turtle.goto(0, 0)
                    break
                    # turtle.tracer(n=2, delay=0)
                    # turtle.pendown()

        elif x > 0 and y < 0:
            print('if x > 0 and y < 0:')
            if turtle.xcor() >= x and turtle.ycor() <= y:
                print('turtle.xcor()', turtle.xcor())
                print('turtle.ycor()', turtle.xcor())
                print('x', x)
                print('y', y)
                print('if-if x > 0 and y < 0:')
                # if turtle.position() >= (x,y):
                break
            else:
                print('else x > 0 and y < 0:')
                turtle.pendown()
                if turtle.xcor() < x and turtle.ycor() > y:
                    print('else-if x > 0 and y < 0:')
                    turtle.setheading(x)
                    turtle.setheading(y)
                    print(turtle.position())
                    turtle.speed('fastest')
                    turtle.forward(1)
                    turtle.penup()
                    turtle.hideturtle()
                else:
                    print('else-else x > 0 and y < 0:')
                    turtle.goto(x, y)
                    turtle.penup()
                    turtle.goto(0, 0)
                    break
    return


def turtlefunc(x,y):
    turtle.pencolor("red")
    # turtle_dotted_lines(x,y)
    #turtle.pendown()
    # turtle.forward(10)
    # turtle.penup()
    # turtle.forward(10)
    turtle.home()
    turtle_dotted_lines(x, y)
    # turtle.goto(x, y)
    # turtle.penup()
    # turtle.tracer(n=2, delay=0)
    # turtle.goto(0, 0)
    #turtle.hideturtle()
    return


def getlatlong(lat, long):
    print("getlatlong")
    #t1 = turtle.Turtle()
    #screen = turtle.Screen()
    screen.bgpic("worldmap1.gif")
    #screen.addshape('worldmap1.gif')
    #turtle.shape('worldmap1.gif')
    print(turtle.position())
    x = long
    y = lat
    turtlefunc(x,y)
    return


def main():
    global line_count
    with open(path,'r') as f:
        data = csv.reader(f)
        for i in data:
            line_count += 1
            print('line_count', line_count)
            if i[0] == 'network':
                continue
            else:
                    ip = i[0][:-3]
                    url = f'http://ip-api.com/json/{ip}'
                    #print(url.url)#s = Session()#s.mount(url, HTTPAdapter(max_retries=5))
                    retry = session_with_retries(url)
                    try:
                        resp = retry.get(url=url)
                        print(resp.json())
                        latitude = resp.json()['lat']
                        longitude = resp.json()['lon']
                        print("latitude", latitude)
                        print("longitude", longitude)
                        try:
                            getlatlong(latitude, longitude)
                        except:
                            print("function error")
                    except:
                        pass
        print("done with tracing the traffic")
    screen.listen()
    screen.exitonclick()


if __name__ == "__main__":
    main()




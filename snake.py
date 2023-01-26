from turtle import Turtle
X = 0
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
RIGHT = 0
DOWN = 270


class Snake:

    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):

        for turtle in range(0, 3):
            self.add_segment(turtle)
            self.new_turtle.showturtle()

    def add_segment(self, position):
        global X
        self.new_turtle = Turtle("square")
        self.new_turtle.hideturtle()
        self.new_turtle.penup()
        self.new_turtle.color("white")
        self.new_turtle.goto(0, 0)

        self.segments.append(self.new_turtle)



    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        self.new_turtle.showturtle()
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


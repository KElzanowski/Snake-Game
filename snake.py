from turtle import Turtle
START_X_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):

        self.snake_segments = []
        """Each snake chunk (yummy). Increases by one segment for every food piece eaten."""
        self.create_snake()
        """Creates snake in main file using the function below."""
        self.head = self.snake_segments[0]
        """Attribute sets up the controls for the snake segment direction and the front of the snake."""

    def create_snake(self):
        for position in START_X_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake_segment = Turtle(shape="square")
        snake_segment.color("green")
        snake_segment.penup()
        snake_segment.goto(position)
        self.snake_segments.append(snake_segment)

    def extend(self):
        self.add_segment(self.snake_segments[-1].position())
        """Extends snake by appending a snake segment to the end of the self.snake_segments list."""

    def move(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            """Range from last snake segment in list to first, decreasing by 1."""
            new_x_cor = self.snake_segments[seg_num - 1].xcor()
            new_y_cor = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(new_x_cor, new_y_cor)
            """Moves each segment to the position of the next segment."""
        self.snake_segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            """So the snake can't turn around 180 degrees."""
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

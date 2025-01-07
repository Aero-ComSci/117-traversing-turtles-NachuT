#chat-gpt helped me with zip function in python
import turtle as trtl

class TurtleDraw:
    def __init__(self, turtle_shapes, turtle_colors, starting_length=100, increment=18, heading=0):
        if len(turtle_shapes) != len(turtle_colors):
            raise ValueError("Object Error")

        self.turtle_shapes = turtle_shapes
        self.turtle_colors = turtle_colors
        self.length = starting_length
        self.increment = increment
        self.heading = heading
        self.turtles = []

    def draw_turtles(self):
        for shape, color in zip(self.turtle_shapes, self.turtle_colors):
            t = trtl.Turtle(shape=shape)
            t.color(color)
            t.penup()
            if not self.turtles:
                t.goto(0, 100)
            else:
                t.goto(self.turtles[-1].pos())
            t.setheading(self.heading)
            t.pendown()
            t.forward(self.length)
            t.right(60)
            self.length += self.increment
            self.heading = t.heading()
            self.turtles.append(t)

turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "classic", "square"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", "yellow", "pink"]

try:
    turtle_drawer = TurtleDraw(turtle_shapes, turtle_colors)
    turtle_drawer.draw_turtles()
except ValueError as e:
    print(f"Error: {e}")

wn = trtl.Screen()
wn.mainloop()

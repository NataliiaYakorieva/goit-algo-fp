import turtle


def draw_branch(t: turtle.Turtle, length: float,
                angle: float, depth: int) -> None:
    """
    Recursively draws branches for the Pythagoras tree fractal.

    Args:
        t (turtle.Turtle): The turtle object used for drawing.
        length (float): The length of the current branch.
        angle (float): The angle between branches.
        depth (int): The current recursion depth.
    """
    if depth == 0:
        return

    t.forward(length)

    position = t.position()
    heading = t.heading()

    t.left(angle)
    draw_branch(t, length * 0.75, angle, depth - 1)

    t.setposition(position)
    t.setheading(heading)

    t.right(angle)
    draw_branch(t, length * 0.75, angle, depth - 1)

    t.setposition(position)
    t.setheading(heading)


def create_pythagoras_tree(depth: int) -> None:
    """
    Sets up the turtle screen and draws the Pythagoras tree fractal.

    Args:
        depth (int): The recursion depth for the fractal.
    """
    screen: turtle.Screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title(f"Pythagoras Tree Fractal. Recursion level = {depth}")
    screen.setup(800, 600)

    t: turtle.Turtle = turtle.Turtle()
    t.speed(0)
    t.pensize(2)
    t.left(90)
    t.penup()
    t.goto(0, -250)
    t.pendown()

    draw_branch(t, 100, 30, depth)

    t.hideturtle()
    screen.exitonclick()


if __name__ == "__main__":
    input_depth: int = int(input("Recursion level: "))
    create_pythagoras_tree(input_depth)

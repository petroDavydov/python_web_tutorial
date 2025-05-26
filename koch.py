import turtle


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_curve(order, size=300):
    try:
        window = turtle.Screen()
        window.bgcolor("white")

        t = turtle.Turtle()
        t.speed(0)
        t.penup()
        t.goto(-size / 2, size / 3)
        t.pendown()

        for _ in range(3):
            koch_curve(t, order, size)
            t.right(120)

        window.exitonclick()  # use hint(закрити після кліку)
    except turtle.Terminator:
        print("Closed before painting ended.")
    except Exception as error:
        print(f"Error occured: {error}")


# Level of recursion
try:
    user_order = int(input("Enter level of recursion (0-5): "))
    if 0 <= user_order <= 5:
        draw_koch_curve(user_order)
    else:
        print("Level of recursion must be from 0 to 5.")
except ValueError:
    print("Enter integer numnber(1,2,3,4,5).")
except turtle.Terminator:
    print("Window closed before painting ended.")

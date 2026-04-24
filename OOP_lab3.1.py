import tkinter as tk

# ===== БАЗОВЫЙ КЛАСС =====
class Shape:
    def draw(self, canvas):
        pass


# ===== КРУГ =====
class Circle(Shape):
    def __init__(self, x, y, radius=20):
        self.x = x
        self.y = y
        self.radius = radius
        print(f"Circle created at ({x}, {y})")

    def draw(self, canvas):
        canvas.create_oval(
            self.x - self.radius,
            self.y - self.radius,
            self.x + self.radius,
            self.y + self.radius,
            outline="black",
            width=2
        )


# ===== ПРЯМОУГОЛЬНИК =====
class Rectangle(Shape):
    def __init__(self, x, y, size=30):
        self.x = x
        self.y = y
        self.size = size
        print(f"Rectangle created at ({x}, {y})")

    def draw(self, canvas):
        canvas.create_rectangle(
            self.x - self.size,
            self.y - self.size,
            self.x + self.size,
            self.y + self.size,
            outline="blue",
            width=2
        )


# ===== КОНТЕЙНЕР =====
class ShapeContainer:
    def __init__(self):
        self.shapes = []

    def add(self, shape):
        self.shapes.append(shape)

    def draw_all(self, canvas):
        for shape in self.shapes:
            shape.draw(canvas)


# ===== ГЛАВНОЕ ОКНО =====
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Lab GUI")

        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # контейнер вместо списка
        self.container = ShapeContainer()

        # режим
        self.mode = "circle"

        # события
        self.canvas.bind("<Button-1>", self.on_click)
        self.root.bind("c", self.set_circle)
        self.root.bind("r", self.set_rectangle)

    def set_circle(self, event):
        self.mode = "circle"
        print("Mode: Circle")

    def set_rectangle(self, event):
        self.mode = "rectangle"
        print("Mode: Rectangle")

    def on_click(self, event):
        if self.mode == "circle":
            shape = Circle(event.x, event.y)
        else:
            shape = Rectangle(event.x, event.y)

        self.container.add(shape)
        self.redraw()

    def redraw(self):
        self.canvas.delete("all")
        self.container.draw_all(self.canvas)


# ===== ЗАПУСК =====
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

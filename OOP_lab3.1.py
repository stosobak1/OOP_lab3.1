
import tkinter as tk
import math

# ===== БАЗОВЫЙ КЛАСС =====
class Shape:
    def __init__(self):
        self.selected = False

    def draw(self, canvas):
        pass

    def contains(self, x, y):
        return False


# ===== КРУГ =====
class Circle(Shape):
    def __init__(self, x, y, radius=20):
        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, canvas):
        color = "red" if self.selected else "black"
        canvas.create_oval(
            self.x - self.radius,
            self.y - self.radius,
            self.x + self.radius,
            self.y + self.radius,
            outline=color,
            width=2
        )

    def contains(self, x, y):
        return math.hypot(x - self.x, y - self.y) <= self.radius


# ===== КОНТЕЙНЕР =====
class ShapeContainer:
    def __init__(self):
        self.shapes = []

    def add(self, shape):
        self.shapes.append(shape)

    def draw_all(self, canvas):
        for shape in self.shapes:
            shape.draw(canvas)

    def clear_selection(self):
        for shape in self.shapes:
            shape.selected = False

    def get_shapes_at(self, x, y):
        return [s for s in self.shapes if s.contains(x, y)]

    def delete_selected(self):
        self.shapes = [s for s in self.shapes if not s.selected]


# ===== ГЛАВНОЕ ОКНО =====
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Lab GUI")

        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.container = ShapeContainer()

        # события
        self.canvas.bind("<Button-1>", self.on_click)
        self.root.bind("<Delete>", self.delete_selected)

    def on_click(self, event):
        ctrl = (event.state & 0x0004) != 0  # Ctrl нажат?

        shapes = self.container.get_shapes_at(event.x, event.y)

        if shapes:
            if not ctrl:
                self.container.clear_selection()

            for s in shapes:
                s.selected = not s.selected if ctrl else True
        else:
            if not ctrl:
                self.container.clear_selection()

            circle = Circle(event.x, event.y)
            self.container.add(circle)

        self.redraw()

    def delete_selected(self, event):
        self.container.delete_selected()
        self.redraw()

    def redraw(self):
        self.canvas.delete("all")
        self.container.draw_all(self.canvas)


# ===== ЗАПУСК =====
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

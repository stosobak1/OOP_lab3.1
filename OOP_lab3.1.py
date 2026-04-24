import tkinter as tk

# ===== КЛАСС КРУГА =====
class Circle:
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
            outline="black"
        )


# ===== ГЛАВНОЕ ОКНО =====
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Lab GUI")

        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # список кругов
        self.circles = []

        # событие клика
        self.canvas.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        # создаём круг
        circle = Circle(event.x, event.y)
        self.circles.append(circle)

        # перерисовка
        self.redraw()

    def redraw(self):
        self.canvas.delete("all")
        for circle in self.circles:
            circle.draw(self.canvas)


# ==== ЗАПУСК ====
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

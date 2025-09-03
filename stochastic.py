import random
import turtle
import time
from memory_profiler import memory_usage

class StochasticLSystem:
    def __init__(self, axiom, rules, angle, iterations):
        self.axiom = axiom
        self.rules = rules
        self.angle = angle
        self.iterations = iterations
        self.sentence = axiom

    def generate(self):
        start_time = time.time()
        for _ in range(self.iterations):
            next_sentence = ""
            for char in self.sentence:
                if char in self.rules:
                    # Losowe wybieranie reguły na podstawie prawdopodobieństw
                    rule, _ = random.choices(
                        population=self.rules[char],
                        weights=[prob for _, prob in self.rules[char]],
                        k=1
                    )[0]
                    next_sentence += rule
                else:
                    next_sentence += char
            self.sentence = next_sentence
        end_time = time.time()
        generation_time = end_time - start_time
        return generation_time

    def draw(self, length):
        start_time = time.time()
        stack = []
        for command in self.sentence:
            if command == 'F':
                turtle.forward(length)
            elif command == '+':
                turtle.right(self.angle)
            elif command == '-':
                turtle.left(self.angle)
            elif command == '[':
                stack.append((turtle.position(), turtle.heading()))
            elif command == ']':
                position, heading = stack.pop()
                turtle.penup()
                turtle.setposition(position)
                turtle.setheading(heading)
                turtle.pendown()
        end_time = time.time()
        drawing_time = end_time - start_time
        return drawing_time

# Parametry L-Systemu
axiom = "FFFB"
rules = {
    "B": [("F[+FB][-FB]" , 0.7), ("FFB", 0.1), ("F-FB", 0.1), ("F+FB", 0.1)]
}
angle = 25.7
iterations = 5

# Ustawienia długości linii (możesz ją zmienić)
line_length = 20  # Długość rysowanej linii

# Pomiar pamięci i czasu
start_memory = memory_usage()[0]
start_time = time.time()

# Tworzenie i generowanie L-Systemu
lsys = StochasticLSystem(axiom, rules, angle, iterations)
generation_time = lsys.generate()

# Inicjalizacja okna turtle
turtle.speed(0)  # Maksymalna prędkość rysowania
turtle.hideturtle()  # Ukrycie "żółwia" podczas rysowania
turtle.bgcolor("white")  # Kolor tła
turtle.color("black")  # Kolor rysowania

# Przesunięcie obrazka w dół
turtle.penup()
turtle.goto(0, -200)  # Przesunięcie startowej pozycji w dół
turtle.pendown()

# Ustawienie kierunku żółwia na północ (do góry)
turtle.setheading(90)

# Rysowanie L-Systemu z możliwością ustawienia długości linii
drawing_time = lsys.draw(line_length)

end_time = time.time()
end_memory = memory_usage()[0]

# Podsumowanie
print(f"L-system performance:")
print(f"Total execution time: {end_time - start_time:.4f} seconds")
print(f"Generation time: {generation_time*1000:.4f} miliseconds")
print(f"Drawing time: {drawing_time:.4f} seconds")
print(f"Current memory usage: {end_memory:.2f} MB")
print(f"Peak memory usage: {end_memory:.2f} MB")
print(f"Final state length: {len(lsys.sentence)}")

# Zapewnienie, że okno turtle pozostanie otwarte
turtle.done()

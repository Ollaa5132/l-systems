import turtle
import time
import tracemalloc

# Ustawienia L-systemu
axiom = "FX"
rules = {"X": "X+YF+", "Y": "-FX-Y"}  # Przykładowa reguła dla drzewa
angle = 90  # Kąt obrotu (możesz zmienić)
length = 4  # Długość kroku (możesz zmienić)
iterations = 12  # Liczba iteracji (możesz zmienić)

# Funkcja do generowania ciągu na podstawie reguł L-systemu
def generate_l_system(axiom, rules, iterations):
    for _ in range(iterations):
        new_axiom = ""
        for character in axiom:
            new_axiom += rules.get(character, character)
        axiom = new_axiom
    return axiom

# Funkcja do rysowania L-systemu za pomocą Turtle
def draw_l_system(instructions, length, angle):
    stack = []
    for command in instructions:
        if command == "F":
            turtle.forward(length)
        elif command == "+":
            turtle.right(angle)
        elif command == "-":
            turtle.left(angle)
        elif command == "[":
            position = turtle.position()
            heading = turtle.heading()
            stack.append((position, heading))
        elif command == "]":
            position, heading = stack.pop()
            turtle.penup()
            turtle.goto(position)
            turtle.setheading(heading)
            turtle.pendown()

# Rozpoczęcie monitorowania pamięci
tracemalloc.start()

# Pomiar czasu generowania
start_time = time.time()

# Generowanie L-systemu
instructions = generate_l_system(axiom, rules, iterations)

# Pomiar czasu po generowaniu
end_time = time.time()
generation_time = (end_time - start_time) * 1_000_000  # w mikrosekundach

# Pomiar pamięci po generowaniu
current_memory, peak_memory = tracemalloc.get_traced_memory()

# Konfiguracja ekranu Turtle
screen = turtle.Screen()
screen.setup(width=1000, height=800)
turtle.speed(0)
turtle.bgcolor("white")
turtle.pencolor("black")
turtle.penup()
turtle.goto(0, -screen.window_height() // 4 + 200)  # Start bliżej dołu ekranu
turtle.pendown()
turtle.setheading(90)  # Kierunek w górę
# Pomiar czasu rysowania
start_time_drawing = time.time()

# Rysowanie L-systemu
draw_l_system(instructions, length, angle)

# Pomiar czasu po rysowaniu
end_time_drawing = time.time()
drawing_time = (end_time_drawing - start_time_drawing) * 1000  # w milisekundach

# Zakończenie monitorowania pamięci
tracemalloc.stop()

# Obliczanie użycia pamięci
final_state_length = len(instructions)
current_memory_kb = current_memory / 1024  # kB
peak_memory_kb = peak_memory / 1024  # kB

# Ukrycie strzałki (kursora) po zakończeniu rysowania
turtle.hideturtle()

# Wyświetlanie wyników
print(f"L-system performance:")
print(f"Total execution time: {generation_time / 1000 + drawing_time:.4f} ms")  # Suma: mikrosekundy na milisekundy
print(f"Generation time: {generation_time:.4f} μs")
print(f"Drawing time: {drawing_time:.4f} ms")
print(f"Current memory usage: {current_memory_kb:.2f} kB")
print(f"Peak memory usage: {peak_memory_kb:.2f} kB")
print(f"Final state length: {final_state_length}")

# Zakończ program po kliknięciu
turtle.done()

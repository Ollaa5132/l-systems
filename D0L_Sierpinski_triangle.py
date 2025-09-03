import turtle
import time
import tracemalloc

# Ustawienia L-systemu dla trójkąta Sierpińskiego
axiom = "F-G-G"
rules = {"F": "F-G+F+G-F", "G": "GG"}  # Reguły dla trójkąta Sierpińskiego
angle = 120  # Kąt obrotu (120 stopni dla trójkąta równobocznego)
length = 10  # Długość kroku (możesz zmienić)
iterations = 4  # Liczba iteracji (możesz zmienić)

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
    for command in instructions:
        if command == "F" or command == "G":
            turtle.forward(length)
        elif command == "+":
            turtle.right(angle)
        elif command == "-":
            turtle.left(angle)

# Rozpoczęcie monitorowania pamięci
tracemalloc.start()

# Pomiar czasu generowania
start_time = time.time()

# Generowanie L-systemu
instructions = generate_l_system(axiom, rules, iterations)

# Pomiar czasu po generowaniu
end_time = time.time()
generation_time = end_time - start_time

# Pomiar pamięci po generowaniu
current_memory, peak_memory = tracemalloc.get_traced_memory()

# Konfiguracja ekranu Turtle
turtle.speed(0)
turtle.bgcolor("white")
turtle.pencolor("black")
turtle.penup()
turtle.goto(-200, 100)  # Przesunięcie startowe, aby środek trójkąta był widoczny
turtle.pendown()

# Pomiar czasu rysowania
start_time_drawing = time.time()

# Rysowanie L-systemu
draw_l_system(instructions, length, angle)

# Pomiar czasu po rysowaniu
end_time_drawing = time.time()
drawing_time = end_time_drawing - start_time_drawing

# Zakończenie monitorowania pamięci
tracemalloc.stop()

# Obliczanie użycia pamięci
final_state_length = len(instructions)
current_memory_mb = current_memory / 1024 / 1024  # MB
peak_memory_mb = peak_memory / 1024 / 1024  # MB

# Ukrycie strzałki (kursora) po zakończeniu rysowania
turtle.hideturtle()

# Wyświetlanie wyników
print(f"L-system performance:")
print(f"Total execution time: {generation_time + drawing_time:.4f} seconds")
print(f"Generation time: {generation_time:.4f} seconds")
print(f"Drawing time: {drawing_time:.4f} seconds")
print(f"Current memory usage: {current_memory_mb:.2f} MB")
print(f"Peak memory usage: {peak_memory_mb:.2f} MB")
print(f"Final state length: {final_state_length}")

# Zakończ program po kliknięciu
turtle.done()

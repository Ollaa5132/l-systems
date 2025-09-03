import time
import tracemalloc
import turtle

class LSystem:
    def __init__(self, axiom, rules, angle, length):
        """
        Inicjalizuje parametry L-systemu.

        :param axiom: Ciąg początkowy (aksjomat).
        :param rules: Słownik z regułami przekształceń.
        :param angle: Kąt obrotu dla symboli '+' i '-'.
        :param length: Długość początkowa odcinka (skalowana).
        """
        self.axiom = axiom  # Przechowuje aksjomat
        self.rules = rules  # Przechowuje reguły przekształceń
        self.angle = angle  # Przechowuje kąt obrotu
        self.length = length  # Przechowuje długość odcinka
        self.state = axiom  # Stan bieżący L-systemu, początkowo równy aksjomatowi

    def apply_rules(self, symbol, param):
        """
        Stosuje reguły przekształceń do danego symbolu z parametrem.

        :param symbol: Symbol, do którego stosujemy regułę.
        :param param: Parametr związany z danym symbolem.
        :return: Przekształcony symbol z parametrami.
        """
        if symbol in self.rules:
            rule = self.rules[symbol]
            return rule(param)  # Zwraca przekształcony symbol według reguły
        else:
            return symbol + f"({param})"  # Zwraca symbol bez zmian, jeśli nie ma reguły

    def generate(self, iterations):
        """
        Generuje ciąg L-systemu po określonej liczbie iteracji.

        :param iterations: Liczba iteracji do przeprowadzenia.
        """
        for _ in range(iterations):
            next_state = ""
            i = 0
            
            while i < len(self.state):
                if self.state[i] in self.rules:
                    symbol = self.state[i]
                    i += 2  # Pomijamy '('
                    param_str = ""
                    while self.state[i] != ')':
                        param_str += self.state[i]
                        i += 1
                    param = float(param_str)
                    next_state += self.apply_rules(symbol, param)
                    i += 1  # Pomijamy ')'
                else:
                    next_state += self.state[i]
                    i += 1
            self.state = next_state  # Aktualizuje stan na nowo wygenerowany ciąg

    def get_state(self):
        """
        Zwraca bieżący stan L-systemu.
        """
        return self.state

    def interpret(self, turtle):
        """
        Interpretuje ciąg L-systemu i rysuje go za pomocą turtle.

        :param turtle: Obiekt turtle do rysowania.
        """
        i = 0
        while i < len(self.state):
            if self.state[i] == 'F':
                i += 2  # Pomijamy '('
                param_str = ""
                while self.state[i] != ')':
                    param_str += self.state[i]
                    i += 1
                length = float(param_str)
                turtle.forward(length * self.length)  # Rysujemy linię o długości proporcjonalnej do parametru
            elif self.state[i] == '+':
                turtle.right(self.angle)  # Obrót w prawo o określony kąt
            elif self.state[i] == '-':
                turtle.left(self.angle)  # Obrót w lewo o określony kąt
            i += 1

def measure_performance(lsystem, iterations):
    """
    Mierzy wydajność generowania i rysowania L-systemu.

    :param lsystem: Obiekt L-systemu.
    :param iterations: Liczba iteracji.
    """
    # Rozpoczęcie śledzenia pamięci
    tracemalloc.start()
    
    # Pomiar czasu generowania
    start_time_generation = time.time()
    lsystem.generate(iterations)
    end_time_generation = time.time()
    generation_time = end_time_generation - start_time_generation

    # Pomiar czasu rysowania
    start_time_drawing = time.time()
    
    # Konfiguracja ekranu Turtle
    turtle.speed(0)  # Ustawienie maksymalnej prędkości rysowania
    turtle.penup()  # Podniesienie pióra, aby przesunąć turtle bez rysowania
    turtle.goto(-lsystem.length // 2, 0)  # Ustawienie pozycji początkowej
    turtle.pendown()  # Opuszczenie pióra, aby rozpocząć rysowanie

    lsystem.interpret(turtle)  # Interpretacja stanu L-systemu i rysowanie

    end_time_drawing = time.time()
    drawing_time = end_time_drawing - start_time_drawing
    
    # Zatrzymanie śledzenia pamięci
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    # Obliczenie użycia pamięci
    current_memory_mb = current / 1024 / 1024  # MB
    peak_memory_mb = peak / 1024 / 1024  # MB

    # Wyświetlanie wyników
    print(f"L-system performance:")
    print(f"Total execution time: {generation_time + drawing_time:.4f} seconds")
    print(f"Generation time: {generation_time:.4f} seconds")
    print(f"Drawing time: {drawing_time:.4f} seconds")
    print(f"Current memory usage: {current_memory_mb:.2f} MB")
    print(f"Peak memory usage: {peak_memory_mb:.2f} MB")
    print(f"Final state length: {len(lsystem.get_state())}")

if __name__ == "__main__":
    # Definicja parametrycznego L-systemu: krzywa Koch'a
    c = 1.0
    p = 0.3
    q = c - p
    h = (p * q) ** 0.5
    axiom = "F(1)"  # Początkowy ciąg
    rules = {
        'F': lambda x: f"F({x*p})+F({x*h})--F({x*h})+F({x*q})"  # Reguła przekształceń dla symbolu 'F'
    }
    angle = 75  # Kąt obrotu dla '+' i '-'
    length = 300  # Długość początkowa odcinka

    # Tworzenie obiektu L-systemu
    lsystem = LSystem(axiom, rules, angle, length)

    # Liczba iteracji
    iterations = 4

    # Pomiar wydajności
    measure_performance(lsystem, iterations)

    # Zakończenie rysowania
    turtle.done()

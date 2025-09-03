L-System Visualizations

  Projekt prezentuje różne rodzaje L-systemów (systemów Lindenmayera) w formie wizualizacji przy użyciu Pythona i modułu turtle. Został przygotowany w ramach pracy magisterskiej.

Rodzaje L-systemów
Projekt zawiera następujące typy systemów:
1. D0L L-systemy
- Pliki: DOL_dragon.py, DOL_koch.py, DOL_Sierpinski_triangle.py
- Klasyczne systemy deterministyczne.
- Generują znane fraktale: smok Heighwaya, krzywą Kocha, trójkąt Sierpińskiego.

2. Stochastyczny L-system
- Plik: stochastic.py
- Wybiera reguły losowo według zdefiniowanych prawdopodobieństw.
- Generuje naturalnie wyglądające drzewka.

3.Parametryczny L-system
- Plik: parametric_fern.py
- Umożliwia modyfikację długości odcinków w każdej iteracji.
- Przykład: liście paproci lub krzywe Koch'a z parametrami długości.

Funkcjonalności:
- Generowanie ciągu L-systemu dla zadanej liczby iteracji.
- Rysowanie fraktali w turtle.
- Pomiar czasu generowania i rysowania.
- Pomiar użycia pamięci (przybliżony).
- Możliwość modyfikacji parametrów systemu bez API (bezpośrednio w kodzie).

Uruchamianie:

1. Zainstaluj Python (wersja ≥ 3.8).
2. Zainstaluj zależności (opcjonalnie):

pip install memory-profiler

3. Otwórz plik .py odpowiadający wybranemu L-systemowi.
4. Zmień parametry w kodzie (axiom, reguły, kąt, długość, iteracje).
5. Uruchom skrypt:
   
python DOL_dragon.py

6. Obserwuj rysowanie w oknie turtle oraz wyniki wydajności w terminalu.

Pliki

DOL_dragon.py – smok Heighwaya (D0L)
DOL_koch.py – krzywa Kocha (D0L)
DOL_Sierpinski_triangle.py – trójkąt Sierpińskiego (D0L)
stochastic.py – drzewko losowe (stochastyczny)
parametric_fern.py – liście/paprocie (parametryczny)

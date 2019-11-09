# Projekt z Podstaw Sztucznej Inteligencji - przeszukiwanie
## MM.AE2 Problem komiwojarzera - algorytm ewolucyjny

### Treść zadania

Rozwiązanie powinno opierać się na wybranym algorytmie ewolucyjnym z pewnym modelem osobników oraz odpowiednio 
zaimplementowanymi operacjami krzyżowania i mutacji. Sensownie przedstawić postęp w działaniu algorytmu 
(np. Wypisując kluczowe informacje diagnostyczne). WE: plik z definicją mapy/grafu, WY: najkrótszy cykl łączący punkty.


### Struktura grafu

Graf jest zbudowany ze słowników Pythona. Kluczem słownika grafu jest wierzchołek, a wartością jest następny słownik 
przedstawiający krawędź. Słownik krawędzi jako klucz ma wierzchołek, a wartością jest koszt krawędzi.

Przykład:
```python
self.graph = {
  'A': {'B': 2, 'C': 3},
  'B': {'A': 2},
  'C': {'A': 3}
}
```

### Populacja

Populacja to lista ścieżek przez wszystkie miasta.

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

### Generowanie grafu

Do generowania grafów służy specjalna funkcja ```genGraph()```.
Pozwala ona na swtorzenie grafu o zadanej liczbie wierzchołków i gęstości.
Koszty krawędzi są wyliczane na podstawie rozkładu normalnego. Także możliwe jest
przypisanie wierzchołkom grafu specjalnych nazw podając do funkcji listę stringów.

### Osobnik

Osobniki są reprezentowane przez cykle przechodzące
przez wszystkie wierzchołki (cykle Hamiltona). 

### Populacja

Populacja to lista cykli przez wszystkie miasta.

### Funkcja przystosowania

Funkcja oceny czy też przystosowania dla każdego osobnika tj. cyklu jest obliczana
na podstawie odwrotnej proporcjonalności do jego długości (kosztu).
W przypadku gdy dany osobnik nie jest cyklem Hamiltona funkcja oceny zwraca
-1 co odpowiada minimalnej wartości funkcji przystosowania.

### Selekcja

Sposobami wyboru osobników jest strategia elitarna oraz metoda koła ruletki.
Najpierw jest wybierane kilka osobników, którzy przejdą do procesu reprodukcji.
Następnie pozostałe osobniki wybierani są metodą koła ruletki.

### Krzyżowanie

Odbywa się w następujący sposób:
Losowo wybieramy indeks początkowy i końcowy, które określają sekwencje genów w każdym
z rodziców. Każde dziecko będzie zawierało tą sekwencje od jednego rodzica oraz geny 
drugiego rodzica, które nie występują w tej sekwencji.

Przykład:

- *Pierwszy rodzic* 
    - 1 2 3 4 5 6

- *Drugi rodzic* 
    - 2 4 3 1 6 5

- Wylosowane indeksy: 3 i 5

- Wybrane sekwencje:

    *Pierwszy rodzic*     
    - 1 2 **3 4 5** 6
    
    *Drugi rodzic*     
    - 2 4 **3 1 6** 5
    
- *Piersze dziecko*

    - Sekwencja piewszego rodzica 3 4 5 oraz geny drugiego rodzica które nie występują
    w tej sekwencji czyli 2 1 6: 
        
        **3 4 5 2 1 6**
        
- *Drugie dziecko*

    - Analogicznie do pierwszego:
    
        **3 1 6 2 4 5**
        

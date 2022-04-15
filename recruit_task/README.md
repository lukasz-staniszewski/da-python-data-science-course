##### ŁUKASZ STANISZEWSKI
# DAFTCODE RECRUITMENT TASK
## I. Task:

Masz za zadnie znaleźć ścieżkę w trójkącie zbudowanym z liczb od 0 do 9 (od górnego wierzchołka do podstawy trójkąta) z największą sumą liczb budujących ścieżkę, oraz sumę liczb w tej ścieżce. Wychodząc z dowolnej liczby w każdym kolejnym wierszu trójkąta zawsze możesz pójść na dół w lewo lub w prawo (poza ostatnim wierszem którego cyfra kończy ścieżkę). Reprezentacje ścieżki uzyskujemy sklejając wszystkie cyfry ze ścieżki ze sobą.

## II. Example:
Przykładowy trójkąt:
```python
    9
   2 7
  2 9 1
 2 6 8 6
```

Możliwe ścieżki:
- 9→7→1→6
- 9→7→1→8
- 9→7→9→8
- 9→7→9→6
- 9→2→9→8
- 9→2→9→6
- 9→2→2→6
- 9→2→2→2

Ścieżka z największą sumą: 9798 (sklejone 9→7→9→8)
Suma liczb z "największej" ścieżki : 33

## III. Info:
Do tego zadania są 3 podpunkty. We wszystkich należy podać sumę jak i reprezentację ścieżki jako liczby. Odpowiedzi należy podać jako liczby bez podawania rozwiązania. poprawną reprezentacją ścieżki są tylko liczby, bez strzałek, spacji czy innych znaków specjalnych np '9798'

Przykładowa odpowiedź na pytanie:
a) Podaj najdłuższą ścieżkę trójkąta (przykładowy): 9798
b) Podaj sumę liczb z najdłuższej ścieżki trójkąta (przykładowy): 33

Odpowiedzi z innymi wartościami niż cyfry nie będą sprawdzane np:
- 9+7+9+8
- 9→7→9→8
- 9 7 9 8

W niektórych przypadkach istnieje więcej niż jedna ścieżka najdłuższa, wystarczy podać jedną lub więcej reprezentacji by uzyskać punkty, jeśli uda się podać wszystkie możliwe warianty, przewidziano extra punkty.

Format odpowiedzi dla podawania większej ilości ścieżek to oddzielone ścieżki znakami nowej linii np:
4638613421
4644532118
4644532118
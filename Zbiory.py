zbior = {10, 20, 50, 100} # deklaracja zbioru
set() # deklaracja pustego zbioru
print(len(zbior))
zbior.add(10) # Zbiór przyjmuje tylko unikalne wartości dodatnie takiej samej, nie zwiększa jesgo elementów
print(zbior)
zbior.add(200) # Uwaga zbiór nie zawiera indexów dlatego też nie można używać operatora []
               # trzeba zbiór przerobić do TUPLI lub LISTY!!!


zbiorA = {1, 2, 3}
zbiorB = {4, 5, 6}

print(zbiorA | zbiorB) # SUMA zbiorów A & B
print(zbiorA - zbiorB) # RÓŻNICA zbiorów A & B
print(zbiorA & zbiorB) # ILOCZYN zbiorów A & B
print(zbiorA ^ zbiorB)

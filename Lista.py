lista = [10, 20, 50, 100, 200] # deklaracja listy
list() # utworzenie pustej listy za pomocą konstruktora
lista1 = [] # utworzenie pusatej listy za pomocą operatora Dostępu

print(len(lista)) # wypisz liczbę elementów Listy


if 10 in lista: # Sprawdzenie czy "10" znajduje się w lista.
    print("True")
else:
    print("False")

lista[0] = 5 # Operatorem przypisania zmieniamy pojedyńczy element poprzez wskazanie indeksu
print(lista)
lista.append(300) # Dodanie elementu na koniec listy
print(lista)

lista1.insert(0, "abc") # dodanie elementu pod wskazany adres indeksu i podanie wartości
print(lista1)

print(lista)
lista[1:3] = ["abc", "def"]
print(lista)
del lista[1:3] # usunięce elementów z listy
print(lista)
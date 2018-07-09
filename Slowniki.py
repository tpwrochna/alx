oceny = {"jan": 4, "ola": 5, "dominik": 3} # deklaracja słownika
dict() # deklaracja pustego słownika

print(oceny["jan"]) # wypiszę wartośc z klucza "jan"

oceny["tomasz"] = 6 # dodanie do słownika Klucza "tomasz" i wartości 6
print(oceny["tomasz"])

del oceny["dominik"] # usunięcie klucza dominik
print(oceny)
print(len(oceny))
print(oceny)

if "tomasz" in oceny: # Sprawdzamy czy "tomasz" zawiera się w słowniku Ocenty.
    print(oceny["tomasz"])
else:
    print("Nie ma ocen dla Tomasza")




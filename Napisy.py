napis = "tekst"
print(len(napis)) # wypisz długość napisu
print(napis[0]) # wypisz indeks 0 dla napisu
print(napis[1:3])
print(f'Czy znaduje się "s" w napis')
if "s" in napis:
    print(f'Znajduje się {napis[-2]} napis!')
else:
    print(f'Nie znajduje się {napis[-2]} w napis!')
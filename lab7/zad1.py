print("Zapis do pliku")

file = open("plik.txt", "w")
for i in range(1, 20 + 1):
    if i%4 == 0:
        file.write(str(i) + " ")

file.close()
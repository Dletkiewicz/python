print("podaj wartosc")
value = input();
counter = 0;
for i in range(0, len(value)):
    if value[i].isspace() == True:
        counter += 1;
print(counter);
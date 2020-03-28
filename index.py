#4 git testing

menu = []

while True:
    comida = str(input('digite uma comida: ')).lower().strip()
    menu.append(comida)
    if comida == 'fim':
        break

menu.pop()
print(menu)
valores = []
for cont in range (0,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate (valores):
    print(f'Na posição {c} encontrei no valor {v}!')
print(f'Cheguei ao final da lista')
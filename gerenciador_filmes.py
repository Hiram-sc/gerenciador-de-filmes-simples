titulo = []

quant_titulo = int(input("Informe a quantidade de filmes que deseja inserir: "))
for i in range(quant_titulo):
    filme = input(f"Digite o título do {i+1}° filme: ")
    titulo.append(filme)

print("----- LISTA ----- ")
print(f"Número de filmes cadastrados: {len(titulo)}")
print(", ".join(titulo))

print("Primeiro filme da lista: ", titulo[0])
print("Último filme da lista: ", titulo[-1])

filme_final = input("Insira mais um filme para o final: ")
titulo.append(filme_final)

filme_inicio = input("Insira mais um filme para o início: ")
titulo.insert(0, filme_inicio)

print("----- LISTA ----- ")
print(f"Número de filmes cadastrados: {len(titulo)}")
print(", ".join(titulo))

remove_filme = input("Remova um filme pelo título: ")
if remove_filme in titulo:
    titulo.remove(remove_filme) 

print("Lista ordenada: ")
lista_ordenada = sorted(titulo)
print(", ".join(lista_ordenada))

print("Lista inversa: ")
titulo.reverse()
print(", ".join(titulo))

copia_filmes = titulo.copy()
titulo.clear()

print(f"Lista original (limpa): {titulo}")
print(", " .join(copia_filmes))
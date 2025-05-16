#1. Questão: Suponha que você tem um array que armazena os nomes de cinco frutas: [“Maçã”, “Banana”, “Cereja”, “Damasco”, “Uva”].
# Como você adicionaria uma nova fruta ao final do array e como removeria a fruta da terceira posição?

frutas = ["Maçã", "Banana", "Cereja", "Damasco", "Uva"]
frutas.append("laranja")
del frutas[2]
print(frutas)

# em pseudocódigo:
#frutas = [“Maçã”, “Banana”, “Cereja”, “Damasco”, “Uva”]
#frutas.adicionar("laranja")
#frutas.remover_na_posição(2)

#--------------------------------------------------------------------------------------------------------------------
#2. Questão: Imagine um array que armazena os nomes de três cores: “Azul”, “Vermelho” e “Amarelo”.
#Como você adicionaria a cor “Verde” ao início da lista e como removeria a segunda cor?

cores = ["Azul", "Vermelho", "Amarelo"]
cores.insert(0, "Verde")
cores.pop(1)
print(cores)

#--------------------------------------------------------------------------------------------------------------------
#3. Questão: Considere uma pilha utilizada para gerenciar uma sequência de livros.
#Se você adicionar três livros à pilha e depois remover o livro no topo, qual livro será o próximo no topo da pilha? Dê um exemplo com os livros “Livro A”, “Livro B” e “Livro C”.

pilha = []
pilha.append("Livro A")
pilha.append("Livro B")
pilha.append("Livro C")
pilha.pop()
topo = pilha[-1]
print("O livro no topo agora é:", topo)

#--------------------------------------------------------------------------------------------------------------------
#4. Questão: Imagine uma fila utilizada para gerenciar a ordem de atendimento em um consultório médico.
#Se quatro pacientes são adicionados à fila e dois são atendidos, quem serão os próximos dois pacientes na ordem de atendimento? Considere os pacientes “Paciente 1”, “Paciente 2”, “Paciente 3” e “Paciente 4”.

from collections import deque

fila = deque()
fila.append("Paciente 1")
fila.append("Paciente 2")
fila.append("Paciente 3")
fila.append("Paciente 4")
fila.popleft()
fila.popleft()
proximo1 = fila.popleft()
proximo2 = fila.popleft()
print("Próximos a serem atendidos:", proximo1, "e", proximo2)

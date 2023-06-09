import random
import time

def fitness(board):
    attacks = 0
    for i in range(len(board)):
        for j in range(i+1,len(board)):
            if board[i] == board[j]:
                attacks += 1
            offset = j - i
            if board[i] == board[j] - offset or board[i] == board[j] + offset:
                attacks += 1
    return attacks

def generate_board(size):
    board = [0]*size
    for i in range(size):
        board[i] = random.randint(0,size-1)
    return board

def crossover(board1,board2):
    size = len(board1)
    new_board = [0]*size
    for i in range(size):
        if i < size/2:
            new_board[i] = board1[i]
        else:
            new_board[i] = board2[i]
    return new_board

def mutate(board):
    size = len(board)
    new_board = list(board)
    new_board[random.randint(0,size-1)] = random.randint(0,size-1)
    return new_board

def evolve(population):
    new_population = []
    for i in range(len(population)):
        board1 = population[random.randint(0,len(population)-1)]
        board2 = population[random.randint(0,len(population)-1)]
        child = crossover(board1,board2)
        if random.random() < 0.1:
            child = mutate(child)
        new_population.append(child)
    return new_population

def genetic_algorithm(size,population_size,max_generations):
    population = [generate_board(size) for i in range(population_size)]
    for i in range(max_generations):
        population = sorted(population,key=lambda x:fitness(x))
        if fitness(population[0]) == 0:
            return population[0]
        population = evolve(population)
    return None


def runTest100():
    with open("test100.txt", "r") as f:
        for line in f:
            line = line.split(",")
            print("Teste com tabuleiro tamanho 8, população 100 e gerações maximas de 10000: ")
            start_time = time.time()
            solution = genetic_algorithm(int(line[0]), int(line[1]), int(line[2]))
            end_time = time.time()
            print("Tempo de execução: ", end_time - start_time, "s")
            if solution:
                print(solution)
            else:
                print("Nenhuma solução encontrada")

def runTest1000():
    with open("test1000.txt", "r") as f:
        for line in f:
            line = line.split(",")
            print("Teste com tabuleiro tamanho 8, população 1000 e gerações maximas de 100000: ")
            start_time = time.time()
            solution = genetic_algorithm(int(line[0]), int(line[1]), int(line[2]))
            end_time = time.time()
            if solution:
                print(solution)
            else:
                print("Nenhuma solução encontrada")
            print("Tempo de execução: ", end_time - start_time)

def main():
    count = 0
    while count < 3:
        print("Teste ",count+1 ," - Configuração 1")
        runTest100()
        count += 1

    count = 0
    while count < 3:
        print("Teste ",count+1 ," - Configuração 2")
        runTest1000()
        count += 1


main()
# solution = genetic_algorithm(8,1000,100000)
# if solution:
#     print(solution)
# else:
#     print("Nenhuma solução encontrada")

#!/usr/bin/python3
import time

def leitura_dados():
    n = int(input())
    
    alpha = float(input())
    new_alpha = 1 - alpha
    
    matriz_adj = [[] for i in range(n)] 
    matriz_ligacao = [[0]*n for i in range(n)] 
    u = 1
    v = 1
    
    while v != 0 and u != 0:
        u, v = map(int, input().split())
        if u != 0 and v != 0:
            matriz_adj[u-1].append(v-1)
    
    for i in range(0, n):
        len_m = len(matriz_adj[i])
        for j in matriz_adj[i]:
            matriz_ligacao[j][i] = new_alpha/len_m
                
    return matriz_ligacao, alpha

def scale(matriz, alpha):
    start_scale = time.time()
    
    n = len(matriz)
    
    for i in range(0, n):
        for j in range(0, n):
            matriz[i][j] += alpha/n
            if i == j:
                matriz[i][j] -= 1      
        
    for i in range(0, n-1):
        max_ai = matriz[i][i]
        ind = 0
        for j in range(i+1, n):
            if abs(matriz[j][i]) > max_ai: 
                max_ai = matriz[j][i]
                ind = j
        
        if ind != 0:
            matriz[i], matriz[ind] = matriz[ind], matriz[i]
        
        max_ai = matriz[i][i]
        for h in range(i+1, n):
            a = matriz[h][i]/max_ai             
            for g in range(i, n):
                matriz[h][g] = matriz[h][g] - a * matriz[i][g]
    
    result = [0] * n
    result[n-1] = 1
    
    sum_result = 1
    for i in range(n-2, -1, -1):
        sum_i = 0
        for j in range(i+1, n):
            sum_i += matriz[i][j]*result[j]
        result[i] = -(sum_i)/matriz[i][i]
        sum_result += result[i]

    for i in range(0, n):
        result[i] = result[i]/sum_result
    
    end_scale = time.time()
    
    return result, (end_scale-start_scale)
    
def interative(matriz, alpha):
    start_interative = time.time()
    n = len(matriz)
    
    V = []
    L = []
    C = []
    
    x = []
    z = []
    
    alpha_n = alpha/n
    c = abs(1-(2*alpha_n))
    new_c = c/(1-c)
    eps = 1
    
    for i in range(n):
        x.append(1/n)
        z.append(0)
        for j in range(n):
            if matriz[i][j] != 0:
                V.append(matriz[i][j])
                L.append(i)
                C.append(j)
    
    rep = 0
    while eps >= 1e-5:
        rep += 1
        for i in range(len(V)):
            z[L[i]] += V[i]*x[C[i]]
        
        sum_eps = 0
        
        for i in range(n):
            sum_eps += abs(z[i]+alpha_n-x[i])
            x[i] = z[i] + alpha_n
            z[i] = 0
            
        eps = new_c*sum_eps
    end_interative = time.time()
    
    return x, (end_interative-start_interative), rep
    
def compare(m):
    return m[1]
    
def rank(matriz):
    n = len(matriz)
    rankeamento = [[i] for i in range(1, n+1)]
    for i in range(0, n):
        rankeamento[i].append(matriz[i])
    
    rankeamento.sort(key=compare, reverse=True)
    
    return rankeamento

def main_scale(matriz_scale, alpha):
    result_scale, tempo_execucao_scale = scale(matriz_scale, alpha)
    matriz_rank_scale = rank(result_scale)
    
    return result_scale, matriz_rank_scale, tempo_execucao_scale
    
def main_interative(matriz_interative, alpha):
    result_interative, tempo_execucao_interative, rep = interative(matriz_interative, alpha)
    matriz_rank_interative = rank(result_interative)
    
    return result_interative, matriz_rank_interative, tempo_execucao_interative, rep
    
def main():
    matriz, alpha = leitura_dados()
    matriz_1 = [row[:] for row in matriz]
    result_scale, rank_scale, tempo_execucao_scale = main_scale(matriz_1, alpha)
    result_interative, rank_interative, tempo_execucao_interative, numero_repeticoes = main_interative(matriz, alpha)
    
    maior_diff = 0
    menor_diff = 1
    for i in range(len(result_scale)):
        diff = abs(result_scale[i]-result_interative[i])
        if diff > maior_diff:
            maior_diff = diff
            
        if menor_diff > diff:
            menor_diff = diff
        
    while True:
        print("Deseja ver quais dados?")
        s = input("Digite S (Rank do método escalonamento), L (Rank do método interativo), A (Análise dos métodos) ou F (Finalizar programa): ")
        
        if s == "F":
            break
            
        if s == "S" or s == "L":
            quant = int(input("Quantos primeiros do rank deseja mostrar?: "))
            
            if s == "S":
                print("\n------------ Rank do método por escalonamento ------------\n")
                print("       Rank            Página         Importância (%)")
                for i in range(quant):
                    print("\t%d°\t\t%d\t\t%2.6f%%" %(i+1, rank_scale[i][0], rank_scale[i][1]*100))
                
            if s == "L":
                print("\n------------ Rank do método interativo ------------\n")
                print("       Rank            Página         Importância (%)")
                for i in range(quant):
                    print("\t%d°\t\t%d\t\t%.6f%%" %(i+1, rank_interative[i][0], rank_interative[i][1]*100))
                
        if s == "A":
            print("\n------------------ Análise dos Métodos ------------------\n")
            print("Tempo de execução: ")
            print("\t Escalonamento: \t %.5f segundos" %(tempo_execucao_scale))
            print("\t Interativo: \t \t %.5f segundos \n" %(tempo_execucao_interative))
            print("Número de repetições método interativo: %d \n" %(numero_repeticoes))
            print("Diferença: ")
            print("\t Maior: \t %e" %(maior_diff))
            print("\t Menor: \t %e \n" %(menor_diff))
            print("Rank: ")
            print("\t Página mais importante e menos importante:")
            print("\t \t Escalonamento: \t %d e %d" %(rank_scale[0][0], rank_scale[len(rank_scale)-1][0]))    
            print("\t \t Interativo: \t \t %d e %d" %(rank_interative[0][0], rank_interative[len(rank_interative)-1][0]))
        
        print("\n--------------------------------------------------------\n")
        
main()    

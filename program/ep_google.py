import time
 
'''
1°Opcao:
    gerar para n posições k números aleatórios entre 1 e n-1
            Como escolher as posicoes desses números aleatórios?
                pegar k e colocar na posição k assim por diante
                    parece ruim tem uns contra pontos bem mee, tipo
                    eu nao evito casos que eu tenha que pesquisar muito as coisas sem mudar muito a complexidade
                    
2°Opcao:
'''

def leitura_dados(): #Leitura e criação da matriz de ligação
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
    

def scale(matriz, alpha): #1°Método
    start_scale = time.time()
    # matrix nxn
    n = len(matriz)
    for i in range(0, n):
        for j in range(0, n):
            matriz[i][j] += alpha/n
            if i == j:
                matriz[i][j] -= 1      
        
    # Processo de escalonamento
    for i in range(0, n-1):
        # Pegar maior valor em módulo da coluna
        max_ai = matriz[i][i]
        ind = 0
        for j in range(i+1, n):
            if abs(matriz[j][i]) > max_ai: 
                max_ai = matriz[j][i]
                ind = j
        
        if ind != 0:
            matriz[i], matriz[ind] = matriz[ind], matriz[i] #swap
        
        # Scale
        max_ai = matriz[i][i]
        for h in range(i+1, n):
            a = matriz[h][i]/max_ai             
            for g in range(i, n):
                matriz[h][g] = matriz[h][g] - a * matriz[i][g]
    
    # Pegando resultado
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
    
def limit(matriz, alpha): #2°Método
    start_limit = time.time()
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
    end_limit = time.time()
    
    return x, (end_limit-start_limit), rep
    
def compare(m):
    return m[1]
    
def rank(matriz): # Rankear as paginas de acordo com a importância
    n = len(matriz)
    rankeamento = [[i] for i in range(1, n+1)]
    for i in range(0, n):
        rankeamento[i].append(matriz[i])
    
    rankeamento.sort(key=compare, reverse=True)
    
    return rankeamento
    
def gerar_txt(matrix, nomeArq):
    gen = open(nomeArq, "w")
    
    for i in range(0, len(matrix)):
        for j in range(len(matrix[i])):
            if j != len(matrix[i]) - 1:
                gen.write(str(matrix[i][j]) + '\t')
            else:
                gen.write(str(matrix[i][j]) + "\n")
    gen.close()
    return gen

def main_scale(matriz_scale, alpha):
    result_scale, tempo_execucao_scale = scale(matriz_scale, alpha)
    matriz_rank_scale = rank(result_scale)
    gerar_txt(matriz_rank_scale, "results/scale")
    
    return result_scale
    
def main_limit(matriz_limit, alpha):
    result_limit = limit(matriz_limit, alpha)
    matriz_rank_limit = rank(result_limit)
    gerar_txt(matriz_rank_limit, "results/limit")
    
    return result_limit
    
def main():
    matriz, alpha = leitura_dados()
    matriz_1 = [row[:] for row in matriz]
    result_scale = main_scale(matriz, alpha)
    result_limit = main_limit(matriz_1, alpha)
    
    result_diff = []
    for i in range(len(result_scale)):
        result_diff.append([i+1, abs(result_scale[i]-result_limit[i])])
    gerar_txt(result_diff, "results/diff")
    
    result_stats = [[tempo_execucao_scale],[tempo_execucao_limit],[numero_repeticoes]]
    gerar_txt(result_stats, "results/stats")
    
    '''
    print("       Rank            Página         Importância")
    for i in range(0, len(rj)):
        print("\t%d°\t\t%d\t\t%2.3f%%" %(i+1, rj[i][0], rj[i][1]*100))
    '''
    
main()    

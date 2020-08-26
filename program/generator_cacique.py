def generator_cacique(nomeArq, k, alpha):
    gen = open(nomeArq, "w")
    i = 1
    n = (k*(3+k))/2
    
    gen.write(str(int(n)) + "\n")
    gen.write(str(alpha) + "\n")
    
    j = 1
    while j <= n:
        for f in range(j, j+i+1):
            for e in range(f, j+i+1):
                if f != e:
                    gen.write(str(f) + " " + str(e) + "\n")
                    gen.write(str(e) + " " + str(f) + "\n")
        i += 1
        j += i

    i = 1
    j = 1
    while j <= n:
        i += 1
        h = j+i
        l = i
        while h <= n:
            gen.write(str(j) + " " + str(h) + "\n")
            gen.write(str(h) + " " + str(j) + "\n")
            l += 1
            h += l
            
        j += i
    gen.write("0 0")
    gen.close()
    
#def generator_normais(nomeArq, n_pag, alpha):
    
def main():
    generator_cacique("tests/cacique_20", 20, 0.15)
    generator_cacique("tests/cacique_40", 40, 0.15)

main()


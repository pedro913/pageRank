def gen_cacique(nomearq, k, alpha):
    gen = open(nomearq, "w")
    i = 1
    n = (k*(3+k))/2

    gen.write(str(k) + "_c_" + str(alpha) + "\n")
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

def gen_max(nomearq, n, alpha):
    gen = open(nomearq, "w")

    gen.write(str(n) + "_max_" + str(alpha) + "\n")
    gen.write(str(n) + "\n")
    gen.write(str(alpha) + "\n")
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            gen.write(str(i) + " " + str(j) + "\n")
            gen.write(str(j) + " " + str(i) + "\n")
    gen.write("0 0")
    gen.close()

def main():
    start, end = map(int, input().split())
    alpha = float(input())

    for i in range(start, end+1, 100):
        gen_max("tests_max/" + str(i) + "_max_" + str(alpha), i, alpha)

main()


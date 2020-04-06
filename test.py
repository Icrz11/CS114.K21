def main():

    n, k = map(int, input().split())
    pairs = []
    for i in range (k):
        pairs.append([])
        z, t = map(int, input().split())
        pairs[i].append(z)
        pairs[i].append(t)
    j = 0
    country = []
    s = 0
    pairs.sort()
    country = []
    used1 = []
    used = []
    for i in range (k):
        used.append (0)
    for i in range (n):
        used1.append(0)
    for i in range (n):
        if (used1[i] == 0):
            sum = 1
            for j in range (k):
                if (used[j] == 0 and i in pairs[j]):
                    sum += 1
                    used[j] = 1
                    used1[pairs[j][0]] = 1
                    used1[pairs[j][1]] = 1
                country.append(sum)
        else:
            country.append(0)
    print (country)
    print (pairs)
            



    

    
main()
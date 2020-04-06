
f = open ('Barbones.txt', mode = 'r')#mo file
g = open('BBB.py', mode = 'w') #file de ghi

#ham chuyen doi tu cau lenh while(barebones) -> while (python)
def convert_while(line):
    line = str(line)
    line = line.replace(';','')
    line = line.split()
    tmp = line
    for i in range (len(tmp)):
        if (tmp[i] == 'while'):
            c = str (tmp[i+1])
        if (tmp[i] == 'not'):
            d = str (tmp[i+1])
    g.write ('while')
    g.write (' ')
    g.write (c)
    g.write (' ')
    g.write ('!=')
    g.write (' ')
    g.write(d)
    g.write(' ')
    g.write (':')
    g.write('\n')

#ham chuyen doi tu cau lenh incr variable (barbones) -> variable = variable + 1 (python)
def convert_incr(line):
    line = str(line)
    line = line.replace(';','')
    line = line.split()
    tmp = line
    for i in range (len(tmp)):
        if (tmp[i] == 'incr'):
            c = tmp[i+1]
    g.write(c)
    g.write(' += 1 ')


#ham chuyen doi tu cau lenh decr variable (barbones) -> variable = variable - 1 (python)
def convert_decr(line):
    line = str(line)
    line = line.replace(';','')
    line = line.split()
    tmp = line
    for i in range (len(tmp)):
        if (tmp[i] == 'decr'):
            c = tmp[i+1]
    g.write(c)
    g.write(' -= 1 ')


#ham chuyen doi tu cau lenh clear variable (barbones) -> variable = 0(python)
def convert_clear (line):
    line = str(line)
    line = line.replace(';','')
    line = line.split()
    tmp = line
    for i in range (len(tmp)):
        if (tmp[i] == 'clear'):
            c = tmp[i+1]
    g.write(c)
    g.write (' = 0')
    
#ham dung de check bug
def check_bug (line):
    line = str (line)
    if (';' not in line):
        return False
    line = line.replace (';','')
    line = line.split()
    
    if ('while' in line):
        if (len(line) != 5):
            return False
    if ('decr' in line):
        if (len(line) != 2):
            return False
    if ('incr' in line):
        if (len(line) != 2):
            return False
    if ('clear' in line):
        if (len(line) != 2):
            return False
    return True


def main ():
    line = f.readlines()

    #bien cac chu hoa thanh chu thuong( vi barebones khong phan biet ki tu)
    for i in range (len (line)):
        line[i] = str(line[i])
        line[i] = line[i].lower()

    #kiem tra loi cu phap
    for i in range (len(line)):
        if (check_bug(line[i]) == False):
            print ('Loi o dong thu: ',i + 1)

    #mang danh dau cac cau lenh da duoc bien dich tu Barbones sang python
    used = []
    for i in range (len(line)):
        used.append(0)

     #bien kiem tra xem co dang trong vong while khong   
    check_while = 0
    for i in range (len(line)):
        if (check_while != 0):
            g.write(check_while * '\t')
        if ('while' in line[i] and used[i] == 0):
             convert_while (line[i])
             used[i] = 1
             check_while += 1
        if ('end' in line[i]):
            check_while -= 1
            g.write ('\n')
        if ('incr' in line[i] and used[i] == 0):
            convert_incr(line[i])
            g.write('\n')
            used[i] = 1
        if ('decr' in line[i] and used[i] == 0):
            convert_decr(line[i])
            g.write('\n')
            used[i] = 1
        if ('clear' in line[i] and used[i] == 0):
            convert_clear(line[i])
            g.write('\n')
            used[i] = 1

main()


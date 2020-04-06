def convert(line):
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



def convert_incr(line):
    line = str(line)
    line = line.replace(';','')
    line = line.split()
    tmp = line
    for i in range (len(tmp)):
        if (tmp[i] == 'incr'):
            c = tmp[i+1]
    g.write(c)
    g.write('+=1')
    g.write('\n')
    g.write('\t')

def convert_decr(line):
    line = str(line)
    line = line.replace(';','')
    line = line.split()
    tmp = line
    for i in range (len(tmp)):
        if (tmp[i] == 'decr'):
            c = tmp[i+1]
    g.write(c)
    g.write('+=1')
    g.write('\n')
    g.write('\t')
def convert_clear (line):
    line = str(line)
    line = line.replace(';','')
    line = line.split()
    tmp = line
    for i in range (len(tmp)):
        if (tmp[i] == 'clear'):
            c = tmp[i+1]
    g.write ('c = 0')
    g.write('\n')

def main ():
    f = open ('Barbones.txt', mode = 'r')
    g = open ('BBB.py', mode = 'w')

    line = f.readlines()
 
    for i in range (len(line)):
        if ('while' in line[i]):
            convert(line[i])
            g.write('\t')
        if ('end' in line[i]):
            g.write('\n')
        if ('incr' in line[i]):
            convert_incr(line[i])
        if ('decr' in line[i]):
            convert_decr(line[i])
        if ('clear' in line[i]):
            convert_clear(line[i])

main()

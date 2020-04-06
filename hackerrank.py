import numpy as np
import random
import time

def search_opt (array, x):
    n = len(array)
    array.append(x)
    i = 0
    while array[i] != x:
        i += 1
    
    if (i == n):
        return -1 
    else:
        return i
def search (array, x):
    i = 0
    n = len(array)
    while array[i] != x and i < n:
        i += 1
    return i 

def main():
    f = open('array.txt', 'r')
    work = f.read()
    work = work.split()
    array = []
    for i in range (len(work)):
        work[i] = int (work[i])
    re = 0
    array = [679834,13653, 617248,478794, 862768,944730 ,82009,947153,674038,305344 ]
    opt = []
    normal = []

    print (search_opt(work, 944730))
    print(work[262034])
    print (work[len(work) - 1])









   
    

    
main()

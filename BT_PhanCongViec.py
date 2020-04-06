n = int (input ('So cong viec: '))
m = int (input('So may: '))

time_works = []
id_works = []
result = []
machine = []


def change_position(a, b):
   tmp = a 
   a = b 
   b = tmp
   return a, b

for i in range (n):
   time_works.append(int (input()))
for i in range (n):
   id_works.append(i+1)
for i in range (m):
   machine.append(0)
for i in range (m):
   result.append ([])

print ()



def sort (time, index, n):
   for i in range (n):
      for j in range (i , n):
         if (time[i] < time[j]):
            time[i], time[j] = change_position(time[i], time[j])
            index[i], index[j] = change_position(index[i], index[j])


def work_assigment(work_index, n ,m, index):
   for i in range (m):
      if (machine[i] == min(machine)):
         machine[i] = machine[i] +  work_index
         result[i].append(id_works[index])
         print (i, ' ' ,machine[i])
         break

def main():
   sort (time_works, id_works, n)
   for i in range (n):
      work_assigment(time_works[i], n, m, i)
   print(result)

main()
   


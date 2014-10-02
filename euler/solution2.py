def sequence(n):
   if n <= 1:
       return n
   else:
       return(sequence(n-1) + sequence(n-2))


i = 1
j = 0
total = 0


while j < 4000000:
    j = sequence(i)
    if j%2:
        print(j)
    else:
        print(j)
        total = total + j
    i+=1
print("the sum of the even-valued terms")
print(total)

input_data = open('input.txt' , 'r')
data = input_data.read()
a = int(data)
k = 0
while a !=0:
    if a % 3 == 0:
        a = a - 3
        k +=1
    elif a % 3 == 1:
        a = a - 1
        k +=1
    elif a % 3 == 2:
        a = a - 2
        k +=1
output_data = open('output.txt','w')
output_data.write(str(k))
input_data.close()
output_data.close()
n = int(input("Enter the length of the sequence: ")) # Do not change this line
first = 0
second = 1
third = 2
temp = 3

for i in range(0,n):
    
    

    if i >=2:
        '''
        if i % 1 ==0:
            first = first + second + third
        elif i % 2 ==0:
            second = first + second + third
        else: 
            third = first + second + third
        '''
        print(str(first)+ '+' + str(second) + '+' + str(third))
        print("first is " + str(first+second+third))
        temp = first + second + third
        first = second
        second = third
        third = temp
    else:
        print(i+1)
        

    
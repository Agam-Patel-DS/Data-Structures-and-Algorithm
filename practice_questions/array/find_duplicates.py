def find_duplicates(numbers):
    #first find all the unique numbers
    # numbers = [1,2,4,3,5,4,3]
    unique=[]
    count=[]
    for i in range(len(numbers)):
        if numbers[i] not in unique:
            unique.append(numbers[i])
    #unique=[1,2,4,3,5]
    #now find if that element occurs again or not
    for i in range(0,len(numbers)):
        if numbers[i] in unique:
            count+=1
            
    


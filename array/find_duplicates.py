def find_duplicates(numbers):
    #first find all the unique numbers
    # numbers = [1,2,4,3,5,4,3,4,5,6,3,6,7,8,7,5,3,5,6,7,8,6,4,3,5,6,7,8,8,2,3,4,5,6,7,8,7,6,5,4,3,3,5]
    unique=[]
    index_of_first=[]
    duplicate=[]
    for i in range(len(numbers)):
        if numbers[i] not in unique:
            unique.append(numbers[i])
            index_of_first.append(i)
    for i in range(len(numbers)):
        if i not in index_of_first and (numbers[i] in unique and numbers[i] not in duplicate):
            duplicate.append(numbers[i])

    return duplicate

numbers=[1,2,4,3,5,4,3,4,5,6,3,6,7,8,7,5,3,5,6,7,8,6,4,3,5,6,7,8,8,2,3,4,5,6,7,8,7,6,5,4,3,3,5]
number=[1]
print(f"The duplicates are : {find_duplicates(number)}")
    


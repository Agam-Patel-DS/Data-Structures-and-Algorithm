def  second_largest_element(lst):
    second_largest=-1
    largest=-1
    for i in range(len(lst)):
        if lst[i]>largest:
            print(f"into the loop for {i}")
            second_largest=largest
            largest=lst[i]

        if lst[i]<largest and lst[i]>second_largest:
            second_largest=lst[i]
            
    return second_largest


lst=[1,5,4,5,2,7,6,5,5]
print(second_largest_element(lst))
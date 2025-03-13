def third_largest_element(lst):
    largest=-1
    second_largest=-1
    third_largest=-1

    for i in range(len(lst)):
        if lst[i]>largest:
            third_largest=second_largest
            second_largest=largest
            largest=lst[i]

        elif lst[i]<largest and lst[i]>second_largest:
            third_largest=second_largest
            second_largest=lst[i]

        elif lst[i]<largest and lst[i]<second_largest and lst[i]>third_largest:
            third_largest=lst[i]

    return third_largest

simple_lst=[2,4,5,6,7,8]
medi_lst=[2,5,3,6,4]
tough_lst=[2,5,4,6,4,9,8,7,8]

print(f"Third largest in simple list is {third_largest_element(simple_lst)}")
print(f"Third largest in medi list is {third_largest_element(medi_lst)}")
print(f"Third largest in tough list is {third_largest_element(tough_lst)}")
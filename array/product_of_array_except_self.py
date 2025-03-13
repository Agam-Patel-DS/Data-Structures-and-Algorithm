

def basic_product(l1):
    # basic approach
    answer=[]
    for i in range(len(l1)):
        product=1
        for j in range(len(l1)):
            if i!=j:
                product=product*l1[j]
        answer.append(product)

    return answer

def divide_product(l1):
    answer=[]
    all_product=1
    for i in range(len(l1)):
        all_product=all_product*l1[i]

    for i in range(len(l1)):
        answer.append(int(all_product/l1[i]))

    return answer

l1=[10,3,5,6,2]
print(basic_product(l1))
print(divide_product(l1))
        

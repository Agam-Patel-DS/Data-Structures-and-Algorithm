def return_subsequences(string:str)->list:
    if string=="":
        ans=[""]
        return ans
    
    small_ans= return_subsequences(string[1:])
    mychar=string[0]
    ans = []
    ans.extend(small_ans)
    for i in small_ans:
        ans.append(mychar+i)

    return ans
    




string = "abc"
l1 = return_subsequences(string)
print(l1)

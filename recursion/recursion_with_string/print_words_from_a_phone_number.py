keys = {"1":"", "2": "abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

def return_all_words(string):
    if string=="":
        return [""]
    
    ans=[]

    small_input=string[1:]
    smallInputWords=return_all_words(small_input)

    keyLetter=keys[string[0]]

    for myChar in keyLetter:
        for word in smallInputWords:
            ans.append(myChar+word)


    return ans


ans = return_all_words("23278")
print(ans)
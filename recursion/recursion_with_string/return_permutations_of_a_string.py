# Origional
def return_permutations(string, takenSoFar):
    if len(string)==0:
        return [takenSoFar]
    
    ourchar=string[0]
    smallInput=string[1:]
    small_ans=return_permutations(smallInput, takenSoFar)
    takenSoFar=small_ans
    ans=[]
    # ans.extend(small_ans)
    for i in range(len(small_ans)):
        for j in range(len(small_ans[i])+1):
            ans.append(takenSoFar[i][0:j]+ourchar+takenSoFar[i][j:])

    return ans

# Course Solution
def return_permutations_2(string):
    if len(string)==0:
        return [""]

    currentchar=string[0]
    permutations=return_permutations_2(string[1:])
    ans=[]

    for perm in permutations:
        for position in range(0, len(perm)+1):
            ans.append(perm[0:position]+currentchar+perm[position:])

    return ans

string = "abcd"

print(return_permutations(string,""), "\n")
print(return_permutations_2(string))

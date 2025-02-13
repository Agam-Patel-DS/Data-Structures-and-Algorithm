def check_palindrome(string,s,e):
    if s>e:
        return True
    
    small_ans=check_palindrome(string,s+1,e-1)
    if string[s]==string[e] and small_ans:
        return True
    else:
        return False
    


#base_case => is s>=e then return false
#recursive_call => check_palindrome(string,s+1,e-1)
#work => if s==e-1 and string[s]==string[e] return true
#work => if s<e and string[s] == string [e] return recursive call

string = "abbaa"
ans = check_palindrome(string,0,len(string)-1)
print(f"String {string} is a palindrome: {ans}")
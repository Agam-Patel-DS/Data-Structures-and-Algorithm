# Input: a string of small english alphabets.
# Output: a string of removed duplicates
# Ex: abbact ----> ct
# Use: stack



def remove_duplicates(s):
    if len(s)==0 or len(s)==1:
        return s
    stack=[]
    for char in s:
        if len(stack)==0:
            stack.append(char)
            #print(f"appended {char}")
        elif stack[-1]!=char:
            #print(f"stack[-1]= {stack[-1]} and char= {char} and appended {char}")
            stack.append(char)
            
        elif stack[-1]==char:
            #print(f"stack[-1]= {stack[-1]} and char= {char} and popped {char}")
            stack.pop()
            
        
    final_string = ""
    for char in stack:
        final_string=final_string+char
    
    return final_string


sample_string=""
print(remove_duplicates(sample_string))


# Input is a string of braces which is balanced - {{[({})]}}
# Output is true or false telling if the string in balanced or not


# First mind approach
map={')':'(', ']':'[', '}':'{'}
stack =[]

def is_valid(s):
    l=len(s)
    
    for char in s:
        if char in map.values():
            stack.append(char)
        elif char in map:
            if not stack or stack[-1]!=map[char]:
                return False
            stack.pop()
        else:
            return False
        
    return len(stack) == 0



sample_string="{[({{{{}}}})]}"
sample_string2="{[[)]]}"
sample_string3="" 
sample_string4="{"

print(is_valid(sample_string))
print(is_valid(sample_string2))
print(is_valid(sample_string3))
print(is_valid(sample_string4))
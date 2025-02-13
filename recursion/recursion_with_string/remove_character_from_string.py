string =  "thiszz is risszz" #Output = good morning
string_2 = "dragozn ball z" #Output = dragon ball

#base case => If length of string is zero
#recursive call => remove_character(s[1:])
#work => if s[0]=='z' or not if yes then remove

def remove_character(string, character):
    if len(string)==0 or string=="":
        return string
    
    small_ans=remove_character(string[1:], character)

    if string[0]==character:
        return small_ans
    else:
        return string[0]+small_ans
    
ans=remove_character(string,"z")
ans_1=remove_character(string_2,"z")
print(ans)
print(ans_1)
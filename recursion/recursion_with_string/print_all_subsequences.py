

def print_subsequences(string, takenSoFar):
    if (string=="" or len(string)==0):
        print(takenSoFar)
        return
    
    currentChar = string[0]
    smallInput=string[1:]

    print_subsequences(smallInput, takenSoFar+currentChar) #taken
    print_subsequences(smallInput, takenSoFar) #not-taken


    return

string = "a"
print_subsequences(string, "")
print("<<<<<<----DONE---->>>>>>")

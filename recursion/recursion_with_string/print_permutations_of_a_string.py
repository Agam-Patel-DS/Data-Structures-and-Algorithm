def print_permuatations(string, takenSoFar):
    if (len(string)==0):
        print(takenSoFar)
        return

    ourChar=string[0]
    smallInput = string[1:]

    for i in range(0,len(takenSoFar)+1):
        print_permuatations(smallInput,takenSoFar[0:i]+ourChar+takenSoFar[i:])

    return


string = "abc"
print_permuatations(string, "")
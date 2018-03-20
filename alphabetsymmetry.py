def solve(str):
    
    alphabet = list(enumerate('abcdefghijklmnopqrstuvwxyz'))

    counter = [0]*len(str)
    
    for n in range(len(str)):
        for index,letter in list(enumerate(str[n])):
            for i, x in alphabet:
                if letter.lower() == x and index == i:
                    counter[n] += 1

    return counter
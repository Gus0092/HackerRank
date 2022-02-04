#https://www.hackerrank.com/challenges/Pangrams/problem
#Dificuldade: Facil
import string
def pangrams(s):
    a = list(string.ascii_lowercase)
    x = True
    for i in a:
        if i not in s.lower():
            x=False
    if x:
        return ("pangram")
    else:
        
        return ("not pangram")
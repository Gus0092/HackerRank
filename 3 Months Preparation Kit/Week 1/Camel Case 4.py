#https://www.hackerrank.com/challenges/three-month-preparation-kit-camel-case/problem
import re
while True:
    try:
        s = input().rstrip()    
        sc, mcv, op = s.split(";")
        if sc == "S":
            if mcv == "M":
                    cap = op[:-2]
                   
                    s = re.sub(r"(\w)([A-Z])", r"\1 \2", cap)

                    print(s.lower())
                
            if mcv == "C":
                cap = op
                s = re.sub(r"(\w)([A-Z])",r"\1 \2", cap)
                print(s.lower())
                
            if mcv == "V":
                cap = op
                s = re.sub("(\w)([A-Z])",r"\1 \2",cap)
                print(s.lower())
                
        if sc == "C":
            if mcv == "M":
                cap = op.title()
                s = re.sub(r" ", r"", cap)
                q = s[:1].lower() + s[1:]
                print(q+"()")
            if mcv == "C":
              cap = op.title()
              s = re.sub(" ", "", cap)
              
              print(s)
            if mcv == "V":
                cap = op.title()
                s = re.sub(" ", "", cap)
                q = s[:1].lower() + s[1:]
                print(q)
            
    except EOFError:
        break

#https://www.hackerrank.com/challenges/Time-Conversion/problem
def timeConversion(s):
    if s.endswith("AM"):
        s=s.replace("AM","")
        if s.startswith("12"):
            x=s.split(":")
            x[0]="00"
            s=":".join(x)
        return s
    if s.endswith("PM"):
        s=s.replace("PM","")
        if s.startswith("12"):
            return s
        else:
            x=s.split(":")
            x[0]=str(int(x[0])+12)
            s=":".join(x)
            return s
#1
def delspace(a):
    b=a.split()
    a=' '.join(b)
    return a
a="ffgdfg       gqfgqg        egwefgwe       wfgwfhg"
a=delspace(a)
print(a)
#2
def arifmetica(a):
    a=a.split()
    
#3
def wordN(a):
    b=a.split()
    l=list(b)
    return len(l)
s="hello how are you?"
n=wordN(s)
print(n)
#4
def zamenaGlasnih(a):
    b="aeouiyAEOUIY"
    res=""
    for elem in a:
        if elem in b:
            res+="*"
        else:
            res+=elem
    return res
s="hello how are you?"
s=zamenaGlasnih(s)
print(s)
#5
def deleteN(a,n):
        b=a.split()
        l = []
        for elem in b:
            if len(elem)>=n:
                l.append(elem)
        l=' '.join(l)
        print(l)
a="gwghw w ewg fffds fvqg fg fgh"
n=3
deleteN(a,n)
                
        

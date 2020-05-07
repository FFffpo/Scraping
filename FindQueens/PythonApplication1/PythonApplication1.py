import random
N=int(input('enter N \n'))
cb=[x for x in range(N)]
def check(cb):
    for i in range(N):
        for j in range(i+1,N):
            if abs(cb[i]-cb[j])==abs(i-j):
               return False
    return True

def finderrs(cb):
    errs=0
    for i in range(N):
        for j in range(i+1,N):
             if abs(cb[i]-cb[j])==abs(i-j):
                 errs+=1
    return errs

def find1(cb):
    while not check(cb):
         x1=random.randint(0,N-1)
         x2=random.randint(0,N-1)
         while x1==x2:
             x2=random.randint(0,N-1)
         cb[x1],cb[x2]=cb[x2],cb[x1]
    return cb

def find2(cb):
    errs1=finderrs(cb)
    while not errs1==0:
         x1=random.randint(0,N-1)
         x2=random.randint(0,N-1)
         while x1==x2:
             x2=random.randint(0,N-1)
         cb[x1],cb[x2]=cb[x2],cb[x1]
         errs2=finderrs(cb)
         if errs2>=errs1:
             cb[x1],cb[x2]=cb[x2],cb[x1]
         errs1=min(errs1,errs2)
    return cb

def print_it(cb):
    for i in range(N):
        print('[]'*cb[i]+'Q '+'[]'*(N-cb[i]-1))

way=int(input('enter way(1 or 2) \n'))
if way==1: find1(cb)
if way==2: find2(cb)
else: print('None')
print_it(cb)
    
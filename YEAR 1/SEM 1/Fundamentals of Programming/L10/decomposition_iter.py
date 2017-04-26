from copy import deepcopy
def isPrime(x):
    if(x<2):
        return False
    if(x==2):
        return True
    for i in range(2,x):
        if(x%i==0):
            return False
    return True
 
def backtracking(nr):
    stack=[]
    stack.append([nr,[]])
    while( len(stack)!=0 ):
        x=stack[ len(stack)-1 ]
        stack.pop()
        nr=x[0]
        sol=x[1]
        if( nr==0 ):
            print(sol)
            continue
        for i in range(2,nr+1):
            if( isPrime(i) == True ):
                sol.append(i)
                stack.append([nr-i,deepcopy(sol)])
                sol.pop()
 
 
print(backtracking(7))

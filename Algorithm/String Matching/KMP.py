#KMP AlGORITHM IN PYTHON
#T(n): O(n+m) and Space Complexity is O(m) where m is length of pattern to be matcheds


def prefix_table(P):
    i,j=1,0
    F=[None]*len(P)
    F[0]=0
    
    while(i<len(P)):
        if(P[i]==P[j]):  #if string match 
            F[i]=j+1
            i=i+1
            j=j+1
        elif(j>0):    #if not match and j greater than 0
            j=F[j-1]
        else:
            F[i]=0       #if not match and j equal to 0
            i=i+1
    return F

def KMP(T,P):    #T=Text String , P=Pattern String, F=Prefix Array
    i,j=0,0
    F=prefix_table(P)

    while i<len(T):
        if T[i] == P[j]:
            if j == len(P)-1:
                return i-j
            else:
                j=j+1
                i=i+1
        elif j>0:
            j=F[j-1]
        else:
            i=i+1
    return -1

'''
#driver function
P="zakir"
T="saifizakirisgreat"
ans=KMP(T,P)
print("Pattern found at index ",ans)
if ans != -1:
      for i in range(ans,ans+len(P)):
          print(T[i],end="")
''


        
        

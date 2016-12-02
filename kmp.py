#-*-coding=utf-8-*-
#/usr/bin/env python
"kmp算法实现"

#构建next表

def BuildNext(P):
    Next = [0]*len(P)#next表长和字符串长度相同
    Next[0] = -1             #假想通配符P[-1]
    j,t = 0,-1                    #已知next[0],推导至next[len(P)-1]
    while j < len(P)-1:
        if 0 > t or P[j]==P[t]:
            j+=1
            t+=1
            Next[j]=t
        else:
            t=Next[t]#理解为模式串的自匹配，在t处失配
    return Next

def match(S,P):
    Next = BuildNext(P)
    m,n = len(S),len(P)
    i,j = 0,0
    while i<m and j<n:
        if 0 > j or S[i]==P[j]:
            i+=1;j+=1
        else:
            j = Next[j]
    if j==n:return True
    else:return False

if __name__ == "__main__":
    S ="BBC ABCDAB ABCDABCDABDE"
    P ="BDE "
    print match(S,P)
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 11:08:15 2020

@author: macbookvanille
"""

#Vanille Bourre
#vanille.bourre@poltechnique.edu

    
def sub_list(arr,i,j):
    x=j-i
    C= [0] * x
    m=0
    for n in range (i,j):
        C[m] = arr[n]
        m+=1
    return C
    
    
def test_ex1():
    lst1 = [1,3,2,4,5,3,8]
    print("Sub_list: ", sub_list(lst1,2,5))

    
if __name__ == "__main__":
    test_ex1()


def append_lists(A,B,C):
    C=[0]*(len(A)+len(B))
    for n in range (0,len(A)):
        C[n] = A[n]
    for m in range (0,len(B)):
        C[len(A)+m]= B[m]
    return C
    

def test_ex2():
    lst1 = [1,3,2,4,3,8]
    lst2 = [7,6,5]
    print("Append_lists: ", append_lists(lst1,lst2,3))

    
if __name__ == "__main__":
    test_ex2()
    
def merge(A,B,C):
    C=[0]*(len(A)+len(B))
    m=0
    n=0
    a=0
    if len(A)<len(B):
        P= B
        D= A
    else:
        P=A
        D=B
    while n+m < len(C)-1:
       if P[n]< D[m]:            
            C[a] = P[n]
            a+=1
            n+=1
            print(C)
       else:
            C[a] = D[m]
            m+=1
            a+=1
            print(C)
    if m < len(D):
        for x in range (m,len(D)):
            C[a] = D[x]
            a+=1
            print(C)
    return C
    
    
def test_ex3():
    lst1 = [1,2,4,6]
    lst2 = [5,7]
    print("Merge: ", merge(lst1,lst2,10))

if __name__ == "__main__":
    test_ex3()
    
def merge_sort(arr):
    n=len(arr)
    if n>1:
       m= int(n/2)
       B= arr[0:m]
       C= arr[m+1:n]
       print(B,C)
       B.sort
       C.sort
       merge(B,C,arr)
    return arr

def test_ex4():
    lst1 = [1,4,2,6,3,8]
    print("Merge_sort: ", merge_sort(lst1))

if __name__ == "__main__":
    test_ex4()
    
def partition_full(arr):
    p=arr[0]
    for n in range(1,len(arr)):
        if arr[n]< p:
            c = arr[n]
            print(p)
            print(c)
            print(arr)
            arr[0],c= c,arr[0]
            print(p)
            print(c)
            print(arr[0])
        else:
           # arr[n],arr[-1]= arr[-1],arr[n]
            print(p)
            print(arr[n])
            print(arr[-1])
    return arr

def test_ex5():
    lst1 = [5,2,10,4]
    print("partitionfull: ", partition_full(lst1))

if __name__ == "__main__":
    test_ex5()




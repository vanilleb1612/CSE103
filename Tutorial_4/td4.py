#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 13:48:22 2020

@author: macbookvanille
"""

def selectsort(arr):
    """Input: list arr of numbers
    Result: arr sorted in ascending order
    """
    n = len(arr)
    for i in range(0,n-1):
        # Maintain arr[0..i] sorted
        minptr = i
        for j in range(i+1,n):
            # Find position of smallest element in arr[i..n-1]
            if arr[j] < arr[minptr]:
                minptr = j
        arr[i],arr[minptr] =arr[minptr],arr[i] # Swap values

def sub_list(arr,i,j):
    """ Input: list arr, 0<=i<=j<=len(arr)
    Output: arr[i:j] (arr[i...j-1])
    """
    n = j-i
    res = [0]*n
    for k in range(n):
        res[k] = arr[i+k]
    return res

def merge(A,B,C):
    """Input: lists A and B of numbers in ascending order,
    list C of length len(A)+len(B)
    Result: C list of numbers from A and B in ascending order
    """
    n = len(A)
    m = len(B)
    a = b = c = 0
    while a < n and b < m:
        if A[a] <= B[b]:
            C[c] = A[a]
            a += 1
        else:
            C[c] = B[b]
            b += 1
        c += 1
    for i in range(b,m):
        C[c] = B[i]
        c += 1
    for i in range(a,n):
        C[c] = A[i]
        c += 1

def merge_sort(arr):
    """Input: list arr of numbers
    Result: arr sorted in place in ascending order
    """
    n = len(arr)
    if n>1:
        m = n//2
        left = sub_list(arr,0,m)
        right = sub_list(arr,m,n)
        merge_sort(left)
        merge_sort(right)
        merge(left,right,arr)
 
import time
import random
def rlist(n):
    return [random.randrange(0,n) for x in range(n)]
    
        
def compare(n):
    t=[]
    a = rlist(n)
    t0 = time.time()
    selectsort(a)
    t1 = time.time()
    t.append(t1-t0)
    print("selectsort took this many seconds {:.6f}".format(t1-t0))
    t0 = time.time()
    merge_sort(a)
    t1 = time.time()
    t.append(t1-t0)
    return t
    print("merge_sort took this many seconds {:.6f}".format(t1-t0))


def create_matrix(n):
    m = [[0 for x in range(n)] for y in range(n)]
    for a in range (0,n):
        m[a] = rlist(n)
        a+=1
    return m

def matrix_mult(X,Y):
    result = [[0 for x in range(len(X))] for y in range(len(X))]
    for a in range(len(X)):
        for i in range (len(Y[0])):
            for k in range (len(Y)):
                result[a][i] += X[a][k] * Y[k][i]
    return result

def timematrix(n):
    M1 = create_matrix(n)
    M2 = create_matrix(n)
    t0= time.time()
    matrix_mult(M1,M2)
    t1 =time.time()
    return t1-t0

#The size of matrices to have the calculation time below 1 second is 113

def Fibonacci(n):
    if n== 1 or n==0:
        return n
    else:
        return Fibonacci(n-1)+ Fibonacci(n-2)

def timeFibonacci(n):
    t0=time.time()
    Fibonacci(n)
    t1=time.time()
    return t1-t0
#The time reaches 1 second at n= 25.
# After 25, the algorithm takes way more time to compute the values.

def fib_tab(n,T):
    if n<2:
        return n
    elif T[n]==None:
            v= fib_tab(n-1,T)
            w= fib_tab(n-2,T)
            T[n] =v+w
    return T[n]
                                    
                     
                     
def fib_table(n):
    tab ==[None]*(n+1)
    return fib_tab(n,tab)
    
    
def fib_ac_rec(n,u,v):
    a = 1
    b = 1
    fib=[a, b]
    while b < n:
        a, b = b, a+b
        fib.append(b)
    return fib[n-1]

def divrem(m,n):
    q=0
    r=m
    while r>=n:
        q=q+1
        r=r-n
    return (q,r)
print(divrem(10,4))

def partition_full(A):
    # The inout list A is not empty
    #Output: List A ranked around x
    #r always positive and smaller than len(A)
    l = 1
    r = len(A)
    x = A[0]
    #all 0<=c<l:A[c]<= x and all r<c< len(A) A[c] >x with l <= r
    while l<r:
        if A[l] <= x:
            l += 1
        else:
            A[l],A[r-1] = A[r-1],A[l]
            r -= 1
    # all 0<=c<l: A[c]<=x and if all c, r<=c<len(A): A[i]>x
    A[0],A[r-1] = A[r-1],A[0]
    # x=A[r-1]
    #for c, 0<=c<r: A[c]<=x and for all c, r<=c<len(A): A[c]>x



if __name__ == "__main__":
    compare(100)
    timematrix(113)
    timeFibonacci(25)
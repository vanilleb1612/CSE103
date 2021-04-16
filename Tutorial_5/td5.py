#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 15:50:39 2020

@author: macbookvanille
"""

#Vanille Bourre
#vanille.bourre@gmail.com

#For this tutorial, n is the length of the list A.

def list_sum(A):
#Input: list A of numbers
#Output: sum of all elements in the list
    x=0
    #x is equal to the sum of elements in A[0:0]
    for i in range (0,len(A)): # 0<=i<len(A)
        #At the beginning of iteration l, x is equal to the sum of the numbers from A[0:l] 
        x+=A[i]
        #x is equal to the sum of the numbers from A[0:i] (same as A[0:l+1]) 
    return x
    #x is the sum of all numbers in A[0:n-1]


def test_ex1():
      assert list_sum([]) == 0, "Ex1.1 Should be 0"
      assert list_sum([1]) == 1, "Ex1.2 Should be 1"
      assert list_sum([1,2,3]) == 6, "Ex1.3 Should be 6"
      
############################################################################## 
      
def bin_to_dec(A):
#Input: list A of binary digits
#Output: decimal number represented by the binary number A
    x=0
    for i in range(0,len(A)): #0<=i<len(A)
        y=len(A)-1-i
        x+=2**(i)*A[y]
    return x

# The complexity of my algorithm bin_to_dec is: linear ,Θ(n) 

def test_ex2():
    assert bin_to_dec([]) == 0, "Ex2.1 Should be 0"
    assert bin_to_dec([0,1,1]) == 3, "Ex2.2 Should be 3"
    assert bin_to_dec([1,1,1,0,1,0]) == 58, "Ex2.3 Should be 58"
    
############################################################################## 

def second_largest_position(A):
#Input: list A of numbers of length>1, without duplications
#Output: the position of the second largest element in A
   x=0 #second largest number in A[0:0]
   y=0 #largest number in A[0:0]
   p=0 #position of second largest number in A[0:0]
   f=0 #position of largest number in A[0:0]
   for i in range(0,len(A)):
       if A[i]>x and A[i]>y:
           x=y #largest number in A[0:i-1] becomes second largest number in A[0:i]
           p=f #position of largest number in A[0:i-1] becomes position of second largest number in A[0:i]
           y=A[i] #largest number in A[0:i]
           f=i #position of largest number in A[0:i]
       if A[i]>x and A[i]<y:
           x=A[i] #second largest number in A[0:i]
           p=i #position of second largest number in A[0:i]
   return p #position of second largest number in A[0:n-1]

# The complexity of my algorithm second_largest_position is: linear ,Θ(n) 

def test_ex3():
    assert second_largest_position([]) == 0, "Ex3.1 Should be 0"
    assert second_largest_position([5,2,6,1,7,9]) == 4, "Ex3.2 Should be 4"
    assert second_largest_position([1,2,3,4]) == 2, "Ex3.3 Should be 3"
    
############################################################################## 

def distinct(A):
#input:list A of numbers
#Output: True if all elements in A are distinct, False if there are duplications
    if len(A)==0:
        return True
    for x in range(0,len(A)):
        for i in range (A[x+1],len(A)):
            if A[x] == A[i]:
                return False
            else:
                return True

# The complexity of my algorithm distinct is: quadratic ,Θ(n**2) 
                
def test_ex4():
    assert distinct([]) == True, "Ex4.1 Should be True"
    assert distinct([2,4,5,2]) == False, "Ex4.2 Should be False"
    assert distinct([5,2,6,1,7,9]) == True, "Ex4.3 Should be True"
    
############################################################################## 
    
def partition(A,i,j):
    """ Input: non-empty list A, 0<=i<=j<=len(A)
        Output: sublist A[i..j-1] partitioned
    """
    l = i+1
    r = j
    x = A[i]
    while l<r:
        if A[l] <= x:
            l += 1
        else:
            A[l],A[r-1] = A[r-1],A[l]
            r -= 1
    A[i],A[r-1] = A[r-1],A[i]
    return r-1     
##############################################################################
# def Parentheses2(n):
#     results = [[]]
#     nopen = [[0]]
#     nclosed = [[0]]
#     for i in range(2 * n):
#         results.append([])
#         nopen.append([])
#         nclosed.append([])
#         for j in range(len(results[i])):
#             r = results[i][j]
#             if nopen[i][j] < n:
#                 results[i].append(r + ",1")
#                 nopen[i].append(nopen[i][j]+1)
#                 nclosed[i].append(nclosed[i][j])
#             if nclosed[i][j] < nopen[i][j]:
#                 results[i].append(r + ",-1")
#                 nopen[i].append(nopen[i][j])
#                 nclosed[i].append(nclosed[i][j] + 1)
#     return results[-2]

def generate1(n):
    if n==1:
        Z =[ [1],[-1]]
    elif n > 1:
        if n%2 ==0:
            Z=[1]*(n/2)+(n//2)*[-1]
        elif n%2==1:
            Z= [[[1]*(n//2)+[-1]*((n//2)+1)],[[1]*((n//2)+1)+[-1]*(n//2)]]
    return Z        

def Generate(A):
    if len(A)==1:
        return [A]
    else:
        Output=[]
        for i in A:
            SubList=list(A)  
            SubList.remove(i)  
            for SubPermutation in Generate(SubList):
                Output.append([i]+SubPermutation)
        return Output

def enumerate(n):
    a = [0]*n
    Generate(a,0)

#two different functions to test if the list is balanced.    
def test(A):
    a =list_sum(A)
    if a==0:
        return 'balanced'
    return 'unbalanced'

def test1(A):
    o=1
    c=-1
    l=0
    for i in range(0,len(A)):
        if A[i] == o:
            l+=1
        elif A[i] == c:
            l-=1
    if l==0:
        return 'balanced'
    return 'unbalanced'

   
def generate_well_bracketed(n):
    results = [["1"]]
    nopen = [[1]]
    nclosed = [[0]]
    for i in range(n):
        results.append([])
        nopen.append([])
        nclosed.append([])
        for j in range(len(results[i])):
            r = results[i][j]
            if nopen[i][j] < n/2:
                results[i+1].append(r + ",1")
                nopen[i+1].append(nopen[i][j]+1)
                nclosed[i+1].append(nclosed[i][j])
            if nclosed[i][j] < nopen[i][j]:
                results[i+1].append(r + ",-1")
                nopen[i+1].append(nopen[i][j])
                nclosed[i+1].append(nclosed[i][j] + 1)
    return results[-2]


def test_ex6():
    assert generate_well_bracketed(2) == ['1,-1'], "Ex6.1 Should be [1, -1]"
    assert generate_well_bracketed(4) == ['1,1,-1,-1', '1,-1,1,-1'], "Ex6.2 Should be ['1,1,-1,-1', '1,-1,1,-1']"
# =============================================================================

if __name__ == "__main__":
      #test_ex1()
      #test_ex2()
      #test_ex3()
      #test_ex4()
      # test_ex5()
      #test_ex6()
      print("All tests passed!")
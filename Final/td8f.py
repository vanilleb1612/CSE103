#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 19:22:53 2020

@author: macbookvanille
"""
"""""""""""""""question 1"""""""""""
"""""This function will spot the number that is missing its pair"""""
def missing_number(arr):
    if len(arr) == 1:
        return arr[0]
    #The case where the array is one number is treater first to avoid a problem when computing
    i, j, k = 0, len(arr)-1 , len(arr)//2
    #The variables established will allow us to narrow down the search through the array.
    while True:
        before, after = arr[k-1], arr[k+1]
        if  arr[k]==before:
            i = k+1
            k = (j-i)//2      
            #When the number in the middle is the same as the one to its left, the number not paired is logivally to the right part of the array.
        elif after == arr[k]:
            j = k-1
            k = (j-i) // 2
            #When the number in the middle is the same as the one to its right, the number not paired is logivally to the left part of the array.
        else:
            return arr[k]
        #If the number is not equal to its left of right, as the list is sorted it is the unpaired number.
        
def test_q1():
    assert(missing_number([1,1,2,3,3]) == 2)
    assert(missing_number([4]) == 4)
    assert(missing_number([2,2,3,3,4]) == 4)
    assert(missing_number([6,6,7,8,8]) == 7)
    print("Algorithm missing_number works")

"""""""""""""""question 2"""""""""""
"""""This function will merge and sort the two sorted lists together"""""

def finish_sorting(arr, i, j,k):
    while i < j and j < k:
        if arr[i] < arr[j]:
            i+= 1
        else:   
            last = arr[j]
            prev = arr[i]
            for x in range(i, j):
                tmp = arr[x+1]
                arr[x+1] = prev
                prev  = tmp
            arr[i + 1] = last
            arr[i], arr[i+1] = arr[i+1],arr[i]
            j += 1
            i += 2
    return arr


def test_q2():
    assert(finish_sorting([2,1],0,1,2) == [1,2]);
    assert(finish_sorting([0,2,4,6,1,3,5,7],0,4,8) == [0,1,2,3,4,5,6,7]);
    assert(finish_sorting([3,4,5,0,1,2],0,3,6) == [0,1,2,3,4,5]);
    assert(finish_sorting([0,2,4,6,1,3,5,7,8],0,4,9) == [0,1,2,3,4,5,6,7,8]);
    print("Algorithm finish_sorting works")
    
"""""""""""""""question 3"""""""""""
"""""This function allow us to find the shortest paths from s to each node"""""
def short_paths(G, n, s):
    dists = [inf] * n
    dists[0] = 0
    for edge in G:
        if edge[0] == s:
            tmp = edge[2] + shorth_paths(G, n, edge[1])
            if tmp < dists[edge[1]]:
                dists[edge[1]] = tmp

def test_q3():
    g1 = [(0, 1, 5), (1, 2, 3), (0, 2, 4), (2, 3, 10)]

    g2 = [(0, 1, -1), (0, 2, 4), (1, 2, 3), (1, 3, 2), (1, 4, 2), (3, 2, 5), (3, 1, 1), (4, 3, -3)]

    g3 = [(0, 1, 12), (1, 0, -3), (1, 2, 2), (2, 3, 11), (2, 3, 9), (3, 4, 4), (4, 3, -1), (4, 5, -2), (5, 1, 1), (5, 2, -5), (0, 5, 8)]

    assert (short_paths(g1, 4, 0) == [0, 5, 4, 14])
    assert (short_paths(g2, 5, 0) == [0, -1, 2, -2, 1])
    assert (short_paths(g3, 6, 0) == [0, 9, 3, 12, 16, 8])
    print("Algorithm short_paths works")
    
"""""""""""""""question 4"""""""""""
"""""This function will give all the combinations of weights possible"""""
def possible_weights(w):
    if w == []:
        return [0] # if there are not weights there is no combination( will make sure the algorithm runs for every case)
    total = 0
    n = len(w)
    for i in range(n):
        total += w[i]
    rst = [0] * (total + 1) # First, we do not use any weight so the list is of 0s.
    rst[0] = 1 #It is possible to not use any of the weights.
    sums = []
    for i in range(n):
        for j in range(len(sums)):
            if w[i] + sums[j] not in sums:
                #cover allm possibilities while avoiding repetition
                sums += [w[i] + sums[j]]
                rst[w[i] + sums[j]] = 1
        if w[i] not in sums:
            sums += [w[i]]
            rst[w[i]] = 1
    return rst

def test_q4():
    assert(possible_weights([1,3]) == [1,1,0,1,1])
    assert(possible_weights([1,2,7]) == [1,1,1,1,0,0,0,1,1,1,1])
    assert(possible_weights([5,5]) == [1,0,0,0,0,1,0,0,0,0,1])
    print("Algorithm possible_weights works")


def final_test():
    test_q1()
    test_q2()
    test_q3()
    test_q4()
    print("""  DONE""")
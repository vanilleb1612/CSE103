#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 16:11:00 2020

@author: macbookvanille
"""

########context and objectives##########


def build_graph(A,n): 
    M = [[0]*n for _ in range(n)]
    for i in range(len(A)):
        x,y = A[i][0],A[i][1]
        M[x][y] = 1
    return M
#
def print_matrix(M):
   for i in range(len(M)):
       for j in range (len(M)):
           print ("{:3}".format(M[i][j],end =" "))
       print()
# First graph:    
edges1 = build_graph([(0,1),(1,2),(2,3),(3,4)],5)
print_matrix(edges1)

#Second graph:
edges2= build_graph([(1,0),(2,1),(3,2),(4,3)],5)    
print_matrix(edges2)
#Third graph:
edges3= build_graph([(0,1),(1,2),(2,3),(3,4),(4,0)],5)
print_matrix(edges3)


def trans_closure3(P):
    """input: a square matrix of boolean entries (0/1) representing an adjacency matrix
    Modifies the input P and computes a transitive closure of the corresponding graph
    """
    size = len(P)
    for n in range(size):
        for i in range(size):
            for j in range(size):
                P[i][j] = P[i][j] or (P[i][n] and P[n][j])

def test_warshall(A,n):
    p = build_graph(A,n)
    trans_closure3(p)
    return p

print(test_warshall(edges1,5))
print(test_warshall(edges2,5))
print(test_warshall(edges3,5))

##3
def trans_closure4(P):
    s = len(P)
    for n in range(0,s):
        for i in range(s):
            if P[i][n]:
                for j in range(s):
                    P[i][j] = P[i][j] or (P[i][n] and P[n][j])
                    
g = build_graph([(i,i+1) for i in range(4)],400)

import math
from math import inf

def empty_graph(n):
    mat = [0]*n
    for i in range(n):
            mat[i] = [INF]*n
    for k in range(n):
        mat[k][k] = 0
    return mat
    

def shortest_path(M):
    n = len(M)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                M[i][j] = min(M[i][j],M[i][k]+M[k][j])
 
               
def test_ex4(p):
    shortest_path(p)
    return p

def build_weighted_graph(A,n):
    M = empty_graph(n)
    for c in A:
        x = c[0]
        y = c[1]
        v = c[2]
        M[x][y] = v
    return M

build_weighted_graph([(0,1,3),(1,2,2),(2,3,4),(3,0,1)],inf,0,4)
 
build_weighted_graph([(0,1,3),(1,2,2),(2,3,4),(3,0,1),(3,1,3)],inf,0,4)
 
build_weighted_graph([(0,1,5),(1,3,2),(3,0,6),(2,1,7),(3,2,2),(2,4,2)],inf,0,5)

def longest_path(P):
    n = len(P)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                P[i][j]= max(P[i][j],P[i][k]+P[k][j])
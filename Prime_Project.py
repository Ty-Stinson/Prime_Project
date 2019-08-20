# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 20:10:41 2018

@author: Ty Stinson.
Hello, this is the Prime Project. This program allows us to explore the beauty of prime numbers.
Just press play to open up an interactive menu.
"""


import math
import turtle as t
from turtle import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
import math 




#Calculates the greatest common denominator between two integers
def GCD(a,b):
    r = a % b
    if(r != 0):
        return GCD(b,r)
    else:
        return b
    
  
#Generates the set of prime number within the range given then returns a sorted list
def prime(n):
    primes = set()
    composites = set()
    count = 2
    while(count <= n):
        if count not in composites:
            primes.add(count)
            i = count
            while(count * i <= n):
                multiple = count * i
                if multiple not in composites:
                    composites.add(multiple)
                i +=1 
        if count == 2:
            count +=1
        else:
            count += 2
    return sorted(primes)

    
#Tests the primality of an integer using a trial division               
def trialdivision(n):
    factors = []
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            if i in prime(n):
                factors.append(i)
    if(len(factors)==0):
        print("This number is a prime")
    else:
        print("This composite number has the following prime factors")
        print(factors)
        
 #Performs the factorization of an integer using trial division   
def factorization(n):
    factors = []
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            if i in prime(n):
                factors.append(i)
    if(len(factors)==0):
        print("This number is a prime")
    else:
        print("This composite number has the following prime factors")
        print(factors)

#Tests the primality of an integer using the Sieve of Eratosthenes
def primalitysieve(n):
    primes = prime(n)
    if n in primes:
        print("This number is a prime")
    else:
        print("This number is a composite")
            
        
def distribution(n):
    end1 = 0
    end3 = 0 
    end5 = 0
    end7 = 0
    end9 = 0
    end1to1 = 0
    end1to3 = 0
    end1to5 = 0
    end1to7 = 0
    end1to9 = 0
    end3to1 = 0
    end3to3 = 0
    end3to5 = 0
    end3to7 = 0
    end3to9 = 0
    end5to1 = 0
    end5to3 = 0
    end5to5 = 0
    end5to7 = 0
    end5to9 = 0
    end7to1 = 0
    end7to3 = 0
    end7to5 = 0
    end7to7 = 0
    end7to9 = 0
    end9to1 = 0
    end9to3 = 0
    end9to5 = 0
    end9to7 = 0
    end9to9 = 0
    twinprime = 0
    twinprimelist  = []
    primeaxis = []
    rangeaxis = []
    count = 1
    
    primes = prime(n)
    primes = prime(n)
    
    #This part of the program analyzes the distribution of primes
    for i  in range(len(primes)):
        primename = str(primes[i])
        if primename[-1] == '1':
            end1+=1
            if i+1 < len(primes):
                nextprimename = str(primes[i+1])
                if nextprimename[-1] == '1':
                    end1to1+=1
                if nextprimename[-1] == '3':
                    end1to3+=1
                if nextprimename[-1] == '5':
                    end1to5+=1
                if nextprimename[-1] == '7':
                    end1to7+=1
                if nextprimename[-1] == '9':
                    end1to9+=1
        if primename[-1] == '3':
            end3+=1
            if i+1 < len(primes):
                nextprimename = str(primes[i+1])
                if nextprimename[-1] == '1':
                    end3to1+=1
                if nextprimename[-1] == '3':
                    end3to3+=1
                if nextprimename[-1] == '5':
                    end3to5+=1
                if nextprimename[-1] == '7':
                    end3to7+=1
                if nextprimename[-1] == '9':
                    end3to9+=1
        if primename[-1] == '5':
            end5+=1
            if i+1 < len(primes):
                nextprimename = str(primes[i+1])
                if nextprimename[-1] == '1':
                    end5to1+=1
                if nextprimename[-1] == '3':
                    end5to3+=1
                if nextprimename[-1] == '5':
                    end5to5+=1
                if nextprimename[-1] == '7':
                    end5to7+=1
                if nextprimename[-1] == '9':
                    end5to9+=1
                    
        if primename[-1] == '7':
            end7+=1
            if i+1 < len(primes):
                nextprimename = str(primes[i+1])
                if nextprimename[-1] == '1':
                    end7to1+=1
                if nextprimename[-1] == '3':
                    end7to3+=1
                if nextprimename[-1] == '5':
                    end7to5+=1
                if nextprimename[-1] == '7':
                    end7to7+=1
                if nextprimename[-1] == '9':
                    end7to9+=1
                
            
                
                
        if primename[-1] == '9':
            end9+=1
            if i+1 < len(primes):
                nextprimename = str(primes[i+1])
                if nextprimename[-1] == '1':
                    end9to1+=1
                if nextprimename[-1] == '3':
                    end9to3+=1
                if nextprimename[-1] == '5':
                    end9to5+=1
                if nextprimename[-1] == '7':
                    end9to7+=1
                if nextprimename[-1] == '9':
                    end9to9+=1
       
        #This portion of the method calculates the twin primes in a given range.
        if primes[i] != 2:
            if i+1 < len(primes):
               
                if primes[i+1] == primes[i]+2:
                    twinprime+=1
                    pair = []
                    pair.append(primes[i])
                    pair.append(primes[i+1])
                    twinprimelist.append(pair)
                    
    print("Within this range there are " + str(twinprime) + " pairs of twin primes")
    print("These are the twin primes: " + str(twinprimelist))
    # This part of the function generates graph showing how it scales
    while(count <= 100000):
        rangeaxis.append(count)
        primecount = prime(count)
        primeaxis.append(len(primecount))
        count= count+100
    plt.scatter(rangeaxis,primeaxis)
    plt.xlabel("Range")
    plt.ylabel("Amount of Prime")
    plt.title("The Amount of Prime vs Range")
    plt.show()
        
    print("end1" + " " + str(end1/len(primes)))
    print("end1to1" + " " + str(end1to1/len(primes)))
    print("end1to3" + " " +str(end1to3/len(primes)))
    print("end1to5" + " " + str(end1to5/len(primes)))
    print("end1to7" + " " + str(end1to7/len(primes)))
    print("end1to9" + " " + str(end1to9/len(primes)))
    
    print("end3" + " " + str(end3/len(primes)))
    print("end3to1" + " " + str(end3to1/len(primes)))
    print("end3to3" + " " +str(end3to3/len(primes)))
    print("end3to5" + " " + str(end3to5/len(primes)))
    print("end3to7" + " " + str(end3to7/len(primes)))
    print("end3to9" + " " + str(end3to9/len(primes)))
    
    print("end5" + " " + str(end5/len(primes)))
    print("end5to1" + " " + str(end5to1/len(primes)))
    print("end5to3" + " " +str(end5to3/len(primes)))
    print("end5to5" + " " + str(end5to5/len(primes)))
    print("end5to7" + " " + str(end5to7/len(primes)))
    print("end5to9" + " " + str(end5to9/len(primes)))
         
    print("end7" + " " + str(end7/len(primes)))
    print("end7to1" + " " + str(end7to1/len(primes)))
    print("end7to3" + " " +str(end7to3/len(primes)))
    print("end7to5" + " " + str(end7to5/len(primes)))
    print("end7to7" + " " + str(end7to7/len(primes)))
    print("end7to9" + " " + str(end7to9/len(primes)))
    
    print("end9" + " " + str(end9/len(primes)))
    print("end9to1" + " " + str(end9to1/len(primes)))
    print("end9to3" + " " + str(end9to3/len(primes)))
    print("end9to5" + " " + str(end9to5/len(primes)))
    print("end9to7" + " " + str(end9to7/len(primes)))
    print("end9to9" + " " + str(end9to9/len(primes)))
        
 # This method is used to draw the squares for the visualization   
def draw_square(n):
    t.left(n % 360)
    
    t.forward(n)
    t.left(90)
    t.forward(n)
    t.left(90)
    t.forward(n)
    t.left(90)
    t.forward(n)
    t.left(90)
    
    primename = str(n)
    t.colormode(255)
    t.bgcolor(0,0,0)
    if primename[-1] == '1':
        t.pencolor(233,150,122)
    if primename[-1] == '2':
        t.pencolor(240,255,255)
    if primename[-1] == '3':
        t.pencolor(139,0 ,139)
    if primename[-1] == '5':
        t.pencolor(0,255,255)
    if primename[-1] == '7':
        t.pencolor(220,20,60)
    if primename[-1] == '9':
        t.pencolor(145,44,238)


def visualizer(n):
    t.clear()
    t.reset()
    primes = prime(n)
    for i in range(n):
        draw_square(primes[i])


def menu():
    print("The Prime Project: ")
    print("1.Find the Greatest Common Denominator")
    print("2. Generate Prime Numbers")
    print("3. Primality Test Using Trial Division") 
    print("4. Primality Test Using Sieve of Eratosthenes.")
    print("5. Prime Factorization")
    print("6. Prime Distribution and Twin Primes")
    print("7. Prime Visualization")
    
    
    choice = input("What would you like to do?")
    if choice == '1':
        integer1 = int(input("Enter the an integer: "))
        integer2 = int(input("Enter another integer: "))
        print(GCD(integer1, integer2))
        menu()
    if choice == '2':
        integer1 = int(input("Enter the range you want: "))
        print(prime(integer1))
        print("There are " + str(len(prime(integer1))) + " prime numbers in this range.")
        menu()
    if choice == '3':
        integer1 = int(input("Enter an integer: "))
        trialdivision(integer1)
        menu()
    if choice == '4':
        integer1 = int(input("Enter an integer: "))
        primalitysieve(integer1)
        menu()
    if choice == '5':
        integer1 = int(input("Enter an integer: "))
        factorization(integer1)
        menu()
    if choice == '6':
        integer1 = int(input("Enter an integer: "))
        distribution(integer1)
        menu()
        
    if choice == '7':
        integer1 = int(input("Enter an integer: "))
        visualizer(integer1)
        menu()

print("Welcome to the Prime Project.")
print("This program allows us to explore the beauty of prime numbers.")
print("Just enter the number associated with a choice on the number so use the program.")
print("And keep in mind that the visualization opens up a new window")
print("Thanks for using my program!")
menu()


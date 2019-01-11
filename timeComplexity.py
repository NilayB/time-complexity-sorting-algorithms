# PYTHON Program to compare time complexity of sorting algorithms

import numpy as np
import time
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(1000000)

#-------------------------------------------------------------------------------
#		INSERTION SORT

def insertionSort(myList01):
	for i in range(1, len(myList01)):
		j = i-1
		temp = myList01[i]
		
		while(j >= 0 and temp < myList01[j]):
			myList01[j+1] = myList01[j]
			j = j-1
			
		myList01[j+1] = temp
		
	return(myList01)

#-------------------------------------------------------------------------------
#		BUBBLE SORT

def bubbleSort(myList01):
	flag = 1
	for i in range(0, len(myList01)):
		if(flag == 1):
			flag = 0
		
			for j in range(0, len(myList01)-i-1):
				if(myList01[j] > myList01[j+1]):
					temp = myList01[j]
					myList01[j] = myList01[j+1]
					myList01[j+1] = temp
					flag = 1
		else:
			break
			
	return(myList01)
	
#-------------------------------------------------------------------------------
#		SELECTION SORT

def selectionSort(myList01):
	for i in range(0, len(myList01)):
		min_index = i
		
		for j in range (i+1, len(myList01)):
			if(myList01[j] < myList01[min_index]):
				min_index = j
		myList01[i] = myList01[min_index]
	return(myList01)

#-------------------------------------------------------------------------------
#		MERGE SORT
def merge(myList03, low, mid, high):
    n1 = mid - low + 1
    n2 = high - mid
 
    L = [0] * (n1)
    R = [0] * (n2)
 
    for i in range(0 , n1):
        L[i] = myList03[low + i]
 
    for j in range(0 , n2):
        R[j] = myList03[mid + 1 + j]
 
    i = 0
    j = 0
    k = low
 
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            myList03[k] = L[i]
            i += 1
        else:
            myList03[k] = R[j]
            j += 1
        k += 1
 
    
    while i < n1:
        myList03[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        myList03[k] = R[j]
        j += 1
        k += 1
 

def mergeSort(myList03,low,high):
    if low < high:
        mid = int((low+(high-1))/2)
        mergeSort(myList03, low, mid)
        mergeSort(myList03, mid+1, high)
        merge(myList03, low, mid, high)	

#-------------------------------------------------------------------------------
#		QUICK SORT

def partition(myList02,low,high):
    i = ( low-1 )
    pivot = myList02[high]
 
    for j in range(low , high):
 
        if   myList02[j] <= pivot:   
            i = i+1
            myList02[i],myList02[j] = myList02[j],myList02[i]

    myList02[i+1],myList02[high] = myList02[high],myList02[i+1]
    return ( i+1 )
 
def quickSort(myList02,low,high):
    if low < high:
        pi = partition(myList02,low,high)
        quickSort(myList02, low, pi-1)
        quickSort(myList02, pi+1, high)

#-------------------------------------------------------------------------------
# Printing random List created 

randomList = np.random.random_integers(1,1000000000, size=1000000)
print(len(randomList))
print(randomList)

#-------------------------------------------------------------------------------
# list for storing time required for each algorithm for different number of 
# inputs

insertionSortTime = []
bubbleSortTime = []
selectionSortTime = []
mergeSortTime = []
quickSortTime = []

#-------------------------------------------------------------------------------
# calculating time taken for each sort using different number of inputs

sizes = [10**i for i in range(1,5)]
for i in sizes:
	randomList = np.random.random_integers(1, 1000000000, size=i)
	
	
	startTime = time.time()
	#quickSort(randomList, 0, len(randomList)-1)
	quickList = np.sort(randomList, kind = 'quicksort')
	runTime = time.time() - startTime
	quickSortTime.append(runTime)
	
	
	startTime = time.time()
	#mergeSort(randomList, 0, len(randomList)-1)
	mergeList = np.sort(randomList, kind = 'mergesort')
	runTime = time.time() - startTime
	mergeSortTime.append(runTime)
	
	
	startTime = time.time()
	bubbleList = bubbleSort(randomList)
	runTime = time.time() - startTime
	bubbleSortTime.append(runTime)
	
	startTime = time.time()
	selectionList = selectionSort(randomList)
	runTime = time.time() - startTime
	selectionSortTime.append(runTime)
	
	startTime = time.time()
	insertionList = insertionSort(randomList)
	runTime = time.time() - startTime
	insertionSortTime.append(runTime)
	
	
	#plt.figure(figsize=(12,5))


print("Time for different no. of inputs to the sorting algorithms")
print("Insertion Sort:", insertionSortTime)
print("Selection Sort:", selectionSortTime)
print("Bubble Sort:", bubbleSortTime)
print("Merge Sort:", mergeSortTime)
print("Quick Sort:", quickSortTime)


#-------------------------------------------------------------------------------
# Python functions to draw the graphs

plt.subplot(1,2,1)
plt.plot(sizes, insertionSortTime, marker='x', c='b', label = 'Insertionsort')
plt.plot(sizes, bubbleSortTime, marker='x', c='r', label = 'Bubblesort')
plt.plot(sizes, selectionSortTime, marker='x', c='g', label = 'Selectionsort')
plt.plot(sizes, mergeSortTime, marker='x', c='y', label = 'Mergesort')
plt.plot(sizes, quickSortTime, marker='x', c='black', label = 'Quicksort')
plt.xscale('log')
plt.yscale('log')
plt.xlabel("size of unsorted list - log scale")
plt.ylabel("seconds of computation - log scale")
plt.legend(loc=2)
plt.grid()
plt.title("Quicksort vs Mergesort vs Selectionsort vs Bubblesort vs Insertionsort")

plt.subplot(1,2,2)
plt.plot(sizes, insertionSortTime, marker='x', c='b', label = 'Insertionsort')
plt.plot(sizes, bubbleSortTime, marker='x', c='r', label = 'Bubblesort')
plt.plot(sizes, selectionSortTime, marker='x', c='g', label = 'Selectionsort')
plt.plot(sizes, mergeSortTime, marker='x', c='y', label = 'Mergesort')
plt.plot(sizes, quickSortTime, marker='x', c='black', label = 'Quicksort')
plt.xlabel("size of unsorted list")
plt.ylabel("seconds of computation")
plt.legend(loc=2)
plt.grid()
plt.title("Quicksort vs Mergesort vs Selectionsort vs Bubblesort vs Insertionsort")

plt.show()

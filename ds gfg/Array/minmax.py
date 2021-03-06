def findMinAndMax(A):
 
    max = min = A[0]
 
    for i in range(1, len(A)):
 

        if A[i] > max:
            max = A[i]
 

        elif A[i] < min:
            min = A[i]
 
    print("The minimum element in the list is", min)
    print("The maximum element in the list is", max)
 
 
if name == 'main':
 
    A = [1000, 11, 445, 1, 330, 3000]
 
    findMinAndMax(A)
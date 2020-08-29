'''pairs
You will be given an array of integers and a target value. Determine the number of pairs of array elements that have a difference equal to a target value.
For example, given an array of [1, 2, 3, 4] and a target value of 1, we have three values meeting the condition: 2-1=1,3-2=1 , and4-3=1 .'''

def pair(k,arr):
  count=0
  arr=set(arr)
  for i in arr:
    if (i+k) in arr:
      count+=1
  return(count)    
  
    

def make_squares(arr):
  squares = []
  positiveIndex = 0
  for i, a in enumerate(arr) :
    if a < 0 :
      positiveIndex += 1
  start = positiveIndex-1
  end = positiveIndex
  if positiveIndex == 0 : # all positive
    return [a*a for a in arr]
  else :
    while start >= 0 and end < len(arr) :
      print(start,end)
      if arr[start]*arr[start] <= arr[end]*arr[end] :
        squares.append(arr[start]*arr[start])
        start-=1
      else :
        squares.append(arr[end]*arr[end])
        end+=1
  
    while start >= 0 :
      squares.append(arr[start]*arr[start])
      start-=1
    while end < len(arr): 
      squares.append(arr[end]*arr[end])
      end+=1
  # TODO: Write your code here
  return squares

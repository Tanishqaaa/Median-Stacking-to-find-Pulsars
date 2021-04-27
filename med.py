import numpy as np
def median_bins(list,B):
  list=np.asarray(list)
  mean=np.mean(list)
  std_dev=np.std(list)
  
  left_bin=0
  bins=np.zeros(B)
  bin_width = 2*std_dev/B
  for i in list:
    if i<mean-std_dev:
      left_bin+=1
    elif i < mean + std_dev:
      bin = int((i - (mean - std_dev))/bin_width)
      bins[bin] += 1
  return mean, std_dev, left_bin, bins
#second function

def median_approx(list,B):
  mean,std_dev,left_bin,bins=median_bins(list,B)
  N=len(list)
  mid=(N+1)/2
  
  total=0
  total+=left_bin
  for b, bincount in enumerate(bins):
    total += bincount
    if total >= mid:
      # Stop when the cumulative count exceeds the midpoint
      break

  width = 2*std_dev/B
  median = mean - std_dev + width*(b + 0.5)
  return median
    
  
    
# You can use this to test your functions.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your functions with the first example in the question.
  print(median_bins([1, 1, 3, 2, 2, 6], 3))
  print(median_approx([1, 1, 3, 2, 2, 6], 3))

  # Run your functions with the second example in the question.
  print(median_bins([1, 5, 7, 7, 3, 6, 1, 1], 4))
  print(median_approx([1, 5, 7, 7, 3, 6, 1, 1], 4))

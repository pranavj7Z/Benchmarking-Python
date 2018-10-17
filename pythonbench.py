
#in this we will see an example of benchmarking in python

# Question: With Numpy, what’s the best way to compute the inner product of a vector of size 10 with each row in a matrix of size (5, 10)? *


#these are the methods to 

###########################################################################################################
#method 1
import numpy as np
import timeit # used for calculating total time taken for execution
import numpy as np
def test():
      vector1 = np.arange(10)
      matrix1 = np.arange(50).reshape(5,10)
      np.dot( matrix1,vector1)
 
if __name__ == '__main__':
     import timeit
     print(timeit.timeit("test()", setup="from __main__ import test"))

 #output is 3.399879871001758 in seconds

##########################################################################################################
#method 2
import numpy as np
import timeit # used for calculating total time taken for execution
def test():
     vector1 = np.arange(10)
     matrix1 = np.arange(50).reshape(5,10)
     np.sum(matrix1*vector1,axis=1)

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test"))


 #output is 8.311565101997985 in seconds

############################################################################################################
#method 3
import numpy as np
import timeit # used for calculating total time taken for execution
def test():
      vector1 = np.arange(10)
      matrix1 = np.arange(50).reshape(5,10)
      np.array([np.dot(row,vector1) for row in matrix1])
 
if __name__ == '__main__':
     import timeit
     print(timeit.timeit("test()", setup="from __main__ import test"))
 

 #output is 12.19150627199997 in seconds

############################################################################################################
# from the above programs we are able to benchmark the best among the 3 programs.
# We conclude the best method is method 1 by looking at the time in seconds.



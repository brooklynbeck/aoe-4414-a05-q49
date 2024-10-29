# full_ops.py
#
# Usage: python3 full_ops.py c_in n_wv
# Determines output shape and operation count of a fully connected layer
# Equations from AOE 4414 class at Virginia Tech
# Parameters:
# c_in: input channel count
# n_wv: number of weight vectors
#
# Output:
# Prints the channel height and width of the output, and the number of additions multiplications and divisions performed
#
# Written by Brooklyn Beck
#
# import Python modules
import math # math module
import sys # argv
# "constants"
# helper functions
# initialize script arguments
c_in = float('nan') # input channel count
n_wv = float('nan') # number of weight vectors
# parse script arguments
if len(sys.argv)==3:
  c_in = float(sys.argv[1])
  n_wv = float(sys.argv[2])
else:
  print(\
  'Usage: '\
  'python3 python3 full_ops.py c_in n_wv'\
  )
  exit()
# main script below

c_out = n_wv
h_out = 1
w_out = 1

adds = n_wv*c_in
muls = n_wv*c_in
divs = 0

# print outputs
print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed

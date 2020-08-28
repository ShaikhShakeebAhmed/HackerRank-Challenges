import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
  Desc = sorted(ar,reverse=True)
  TallestCandle = Desc[0]
  res = [temp for temp in Desc if temp == TallestCandle]
  return(len(res))



if True:
  result = birthdayCakeCandles([3,2,1,3])
  print(str(result))
  
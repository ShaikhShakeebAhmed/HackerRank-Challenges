#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
  lengthOfTheString = len(s)
  amOrPm = s[lengthOfTheString -2 : lengthOfTheString]
  if amOrPm == 'PM':
    if int(s[0:2]) == 12:
      return(s[0: lengthOfTheString -2])
    else:
      converted = int(s[0:2]) + 12
      return(str(converted)+ s[2: lengthOfTheString -2])
  else:
    if int(s[0:2]) == 12:
      return('00'+ s[2: lengthOfTheString -2])
    else:
      return(s[0: lengthOfTheString -2])

 
 
if True:
    result = timeConversion('12:45:54PM')
    print(result)

    

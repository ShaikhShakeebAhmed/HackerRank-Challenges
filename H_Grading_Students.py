def gradingStudents(grades):
  newGrades = []
  myHashSet = set([n for n in range(1,101) if n % 5 == 0])
  for x in grades:
    if x >= 38:
      firstStep = round(x/5)
      SecondStep = firstStep * 5
      print(firstStep , SecondStep)
      #print(x + 2)
      if SecondStep in myHashSet:
        if x >= SecondStep-3:
          if SecondStep >= x:
            newGrades.append(SecondStep)
          else:
            newGrades.append(x)
      else:
        newGrades.append(x)
    else:
      newGrades.append(x)
      
  del newGrades[0]
  return (newGrades)
      



    
 
  
  





if True:
  #arr_count = int(input())
  #arr = list(map(int, .rstrip().split()))
  #print(input())
  result = gradingStudents([4,
73,
67,
38,
33,])
#   result = gradingStudents([44,
# 84,
# 94,
# 21,
# 0,
# 18,
# 100,
# 18,
# 62,
# 30,
# 61,
# 53,
# 0,
# 43,
# 2,
# 29,
# 53,
# 61,
# 40,
# 14,
# 4,
# 29,
# 98,
# 37,
# 23,
# 46,
# 9,
# 79,
# 62,
# 20,
# 38,
# 51,
# 99,
# 59,
# 47,
# 4,
# 86,
# 61,
# 68,
# 17,
# 45,
# 6,
# 1,
# 95,
# 95])
  print(result)
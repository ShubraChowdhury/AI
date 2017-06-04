# -*- coding: utf-8 -*-
"""
Created on Fri May 12 08:11:13 2017

@author: shubra
"""

"""
[A, B, C, D]
        then the neighbors will include [A, B, D, C], [A, C, B, D], [B, A, C, D],
        and [D, B, C, A].
"""
 
#test_cities = [('DC', (11, 1)), ('SF', (0, 0)), ('PHX', (2, -3)), ('LA', (0, -4))]
test_cities =['A', 'B', 'C','D']
print("Length :-",len(test_cities), "\t Cities :",test_cities ,"\n")
p= test_cities
cit =[]
import copy
 
for i in range(0,len(test_cities)):
#    print(test_cities[i])
    p= copy.deepcopy(test_cities)
  
   
    if i == 0 :
#        print(i," -->" , test_cities[i])
        k = len(test_cities)-1
        j= 0
        p[k],p[j] = test_cities[j],test_cities[k]
   
#    print("test_cities ",test_cities)   
    if i != 0 :
#        print(i," -->", test_cities[i])
        k = i-1
        j = i
        p[k],p[j] = test_cities[j],test_cities[k]
       
 
    cit.append(p)
    print(p)
print(cit)
 

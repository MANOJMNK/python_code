list1=[1,2,3,4,5]
new_list=[]
for i in list1:
    if(i<=5):
        new_list.append(i*2)
print new_list
print "----------------"
new_list=[i*2 for i in list1]
print new_list
print "-----------------"
new_list=[i*2 for i in list1 if i<5]
print new_list

#Assignment

words=['abc','def','ghi']
upper_word=[i.upper() for i in words]
print upper_word
print"----------------------"
numbers=[1,2,3,4,5]
sqr_numbers=[i**2 for i in numbers]
print sqr_numbers

#square root
import math
sqrt=[int(math.sqrt(i)) for i in sqr_numbers]
print sqrt


#dictionary comprehension

list2=[1,2,3,7]
dictionary={i:i*i for i in list2}
print dictionary

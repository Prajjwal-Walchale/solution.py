#find_more_than_average(): Find and return the percentage of students who have scored more than the average mark of the class.
#generate_frequency(): Find how many students have scored the same marks. For example, how many have scored 0, how many have scored 1, how many have scored 3….how many have scored 25. The result should be populated in a list and returned.
#sort_marks(): Sort the marks in the increasing order from 0 to 25. The sorted values should be populated in a list and returned.#

#Sample Input	                                     Expected Output
#list_of_marks = (12,18,25,24,2,5,18,20,20,21)	   70.0 
#                                                  [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 2, 1, 0, 0, 1, 1]
#                                                  [2, 5, 12, 18, 18, 20, 20, 21, 24, 25]


list_of_marks=(12,18,25,24,2,5,18,20,20,21)
def find_more_than_average():
    global list_of_marks
    marks=0
    count=0
    for x in list_of_marks:
        marks+=x
    average=marks/len(list_of_marks)
    for x in list_of_marks:
        if x> average:
           count+=1
    percentage=(count*100)/len(list_of_marks)
    return percentage
def sort_marks():
    global list_of_marks
    list_of_marks=sorted(list_of_marks)
    return list_of_marks
def generate_frequency():
    freq=[]
    global list_of_marks
    for x in range(26):
        count=0
        for y in list_of_marks:
              
           if x == y:
                 
              count+=1
         freq.append(count)
     
    return freq
  
  print(find_more_than_average())
  print(generate_frequency())
  print(sort_marks())
    
    
    

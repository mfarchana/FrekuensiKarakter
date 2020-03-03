from collections import Counter 
  
document_text = open('/Users/farch/Desktop/aan.txt', 'r')
data_set = document_text.read()
  
# split() returns list of all the words in the string 
split_it = data_set.split() 
  
# Pass the split_it list to instance of Counter class. 
Counter = Counter(split_it) 
  
# most_common() produces k frequently encountered 
# input values and their respective counts. 
most_occur = Counter.most_common(7) 
  
print(most_occur) 
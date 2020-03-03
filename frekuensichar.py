document_text = open('/Users/farch/Desktop/aan.txt', 'r')
input_string = document_text.read()
frequencies = {} 
  
for char in input_string: 
   if char in frequencies: 
      frequencies[char] += 1
   else: 
      frequencies[char] = 1

# Show Output
print ("Per char frequency in '{}' is :\n {}".format(input_string, str(frequencies)))
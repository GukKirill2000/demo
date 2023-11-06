# Initialize an empty list 'a'
a = []

# Populate the list 'a' with numbers from 0 to 4
for i in range(5):
  a.append(i)

# Initialize an empty list 'b'
b = []

# Iterate over the length of list 'a'
for i in range(len(a)):
  # Convert the number to lowercase (which will cause an error because numbers don't have a lowercase) and append ' I' to it
  x = a[i].lower()+' I'

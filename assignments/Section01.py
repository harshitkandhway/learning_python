print('Hello World')

# assignment 01
remainder = 15%4
print('The remainder is : '+str(remainder))

# assignment 02
print("We have {0} small boxes, {1} large boxes, {2} medium boxes".format(10,12,12))

# assignment 03
chars="<<<>>>"
word = "Hello World"
result = chars[:3] + word + chars[3:]
print(result)

# assignment 04
word1 = "Vehicle"
word2 = "Robot"
result = word1[1:]+word2[:1]+word2[2:]
print(result)

# assignment 05
chars = "<[<||>]>"
word = "mirror"
size = len(chars)
idx = int(size/2)
result = chars[:idx] + word + chars[idx:]
print(result)

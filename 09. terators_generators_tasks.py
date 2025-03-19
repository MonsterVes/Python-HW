# ---------------------------------- Task 1 ---------------------------------- #
"""DESCRIPTION:
Write an EvensIterator class, such that its objects can be used in for loops, iterating over the even numbers in specified [start, end] range (both inclusive).
"""


### YOUR CODE HERE
# class EvensIterator:
#     def __init__(self, start, end):
#         self.current = start
#         self.end = end

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         while self.current <= self.end:

#             self.current += 1
#             if (self.current-1)%2 == 0:

#                 return self.current - 1
#         raise StopIteration



# for x in EvensIterator(1,20):
#     print(x, end =", ")

### TEST:
# for x in EvensRange(1,10):
#     print(x, end=",")

### EXPECTED OUTPUT
# 2,4,6,8,10,


# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
Write a generator function (evens_generator), such that will yield an even number
in specified [start, end] range (both inclusive).
"""


### YOUR CODE HERE

# def evens_generator(start, end):
#     current = start
#     while current <= end:
#         if current%2 == 0:
#             yield current
#         current +=1

# # print(list(evens_generator(1,10)))
# for x in evens_generator(1,10):
#     print(x, end = ", ")

### TEST:
# for x in evens_generator(1,10):
#     print(x, end=",")

### EXPECTED OUTPUT
# 2,4,6,8,10,


# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
Define a generator function which will yield all Cyrillic Upper Letters, starting from 'А', to 'Я'
Tip: you can get a letter form its code, using the chr() built-in function, as shown in next examples:
print( chr(1040) )
# 'А''

print( chr(1041) )
# 'Б'

print( chr(1071) )
# 'Я'
"""


### YOUR CODE HERE
# def cyrillic_generator():
#     start = 1040
#     end = 1071
#     while start <= end:
#         yield chr(start)
#         start += 1

# for char in cyrillic_generator():
#     print(char, end = ", ")


# TEST:
# for l in cyrilic_letter_generator():
#     print(l, end=",")

### EXPECTED OUTPUT:
# А,Б,В,Г,Д,Е,Ж,З,И,Й,К,Л,М,Н,О,П,Р,С,Т,У,Ф,Х,Ц,Ч,Ш,Щ,Ъ,Ы,Ь,Э,Ю,Я,

# ---------------------------------- Task 4 ---------------------------------- #
""" DESCRIPTION:
Create both a generator function (words_from_sentence) and an iterator class (WordsFromSentence) that produces words from a sentence. 
Both should split the input sentence by spaces and return each word
one at a time when iterated over.
Your implementation should handle empty sentences properly.

"""


### YOUR CODE HERE

# class WordsFromSentence:
#     def __init__(self, sentence):
#         self.sentence = sentence.split(" ")
#         self.idx = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.idx < (len(self.sentence)):
#             word = self.sentence[self.idx]
#             self.idx += 1
#             return word
#         else:
#             raise StopIteration
        

# print("Test with iterator class:")     
# for w in WordsFromSentence("This is a test"):
#     print(w)

# def words_from_sentence(sentence):
#     words = sentence.split(" ")
#     for word in words:
#         yield word

# def words_from_sentence(sentence):
#     words = sentence.split(" ")
#     idx = 0
#     while idx < (len(words)):
#         yield words[idx]
#         idx += 1
    

# print(list(words_from_sentence("This is a test")))

# print("Test with generator function:")
# for w in words_from_sentence("This is a test"):
#     print(w)
    


# # TEST case 1: Using the iterator class
# print("Test with iterator class:")
# for w in WordsFromSentence("this is a test"):
#     print(w)

# # TEST case 2: Using the generator function
# print("\nTest with generator function:")
# for w in words_from_sentence("this is a test"):
#     print(w)

### EXPECTED OUTPUT:
# Test with iterator class:
# this
# is
# a
# test
#
# Test with generator function:
# this
# is
# a
# test


# ---------------------------------- Task 5 ---------------------------------- #
""" DESCRIPTION:
Write an iterator for Fibonacci sequence

"""


""" Fibonacci for number"""

# class FibonacchiSequence:
#     def __init__(self, number):
#         self.number = number
#         self.a = 0
#         self.b = 1

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.b <= self.number:
#             self.a, self.b = self.b, self.a + self.b
#             return self.a
#         else:
#             raise StopIteration
    
# # print(list(FibonacchiSequence(30)))

# fibonacci = FibonacchiSequence(30)
# for number in fibonacci:
#     print(number, end = ", ")


""" Fibonacci for lenght"""


# class FibonacchiSequence2:
#     def __init__(self, lenght):
#         self.lenght = lenght
#         self.a = 0
#         self.b = 1
#         self.start = 0

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.start <= self.lenght:
#             self.a, self.b = self.b, self.a + self.b
#             self.start += 1
#             return self.a
#         else:
#             raise StopIteration
    
# # print(list(FibonacchiSequence2(30)))

# fibonacci = FibonacchiSequence2(30)
# for number in fibonacci:
#     print(number, end = ", ")


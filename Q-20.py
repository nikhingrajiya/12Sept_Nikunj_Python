word_list = input("enter a list of words separated by spaces:").split()

longest_word=max(word_list,key=len)

length_of_longest_word= len(longest_word)

print("the longest word is:",longest_word)
print("its length is:",length_of_longest_word)
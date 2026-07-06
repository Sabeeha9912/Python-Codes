# word count
paragraph = input("Enter a paragraph: ")
paragraph = paragraph.lower()
words = paragraph.split()   # Split paragraph into words
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print("\nTotal number of words:", len(words))   # Display total number of words
print("\nWord frequency in the paragraph:")   # Display repeated words
for word, count in word_count.items():
    print(f"{word}: {count}")

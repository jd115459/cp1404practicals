"""
Word Occurrences
Estimate: 25mins
Actual: 20mins
"""

text = input("Enter text: ")

word_to_count = {}
words = text.split()
for word in words:
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1

max_length = max(len(word) for word in word_to_count)

for word in sorted(word_to_count):
    print(f"{word:{max_length}}: {word_to_count[word]}")

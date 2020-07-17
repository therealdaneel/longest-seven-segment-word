import re


letters = ["a", "A", "b", "c", "C", "d", "E",
		   "F", "G", "H", "h", "I", "J", "L",
		   "n", "O", "o", "P", "q", "r", "S",
		   "t", "U", "u", "y"]

with open("words.txt", "r") as f:
	lines = [i.strip("\n") for i in f.readlines()]


expression = r"([abcdefhhijlnopqrstuy]+)"
test = re.compile(expression, re.IGNORECASE)
final_list = []
for word in lines:
	search = test.search(word)
	if search:
		if len(search.group(1)) == len(word):
			final_list.append(word)

final_list = sorted(final_list, key=lambda item: len(item), reverse=True)
print(final_list[0])
print(len(final_list[0]))
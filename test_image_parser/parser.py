import re
from cloud_connection import get_words_from_image, get_from_test_data


#words = get_words_from_image()
words = get_from_test_data()


def get_price(words):
	key_words = ["итог", "итого", "сумма", "цена", "всего", "оплата", "оплате", "total", "summ"]
	for i in range(len(words)):
		for key_word in key_words:
			line = words[i].description.lower()
			if (key_word in line):
				candidate_str = line
				if (i < len(words) - 1):
					candidate_str += " " + words[i + 1].description
				if (i < len(words) - 2):
					candidate_str += " " + words[i + 2].description

				newstr = ''.join((ch if ch in '0123456789.-e' else ' ') for ch in candidate_str)
				listOfNumbers = [float(i) for i in newstr.split() if re.match("^\d+?\.\d+?$", i)]
				if (len(listOfNumbers) > 0):
					print(candidate_str)
					return abs(listOfNumbers[0])
	return -1

print("Price: ")
print(get_price(words))
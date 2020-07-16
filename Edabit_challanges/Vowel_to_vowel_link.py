import re

def vowel_links(txt):
	return bool(re.search('[aeiou] [aeiou]', txt))
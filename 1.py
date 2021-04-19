import re
from tols import *

jp='color.json'



js=openjs(jp)

word=[
	'win8',
	'1',
	'2',
	'3',
	'4',
	'5',
	'6',
	'7',
	'8',
	'9',
	'0',
	'green',
	'blue',
	'red',
	'gray',
	'gold',
	'brown',
	'pale',
	'orange',
	'medium',
	'white',
	'dark',
	'black',
	'yellow',
	'purple',
	'pink',
	'olive',
	'light',
	'sky',
	'flower',
	'turquoise',
	'slate',
	'lavender',
	'magenta',
	'old',
	'rose',
	'violet',
	'wood',
	'burly',
	'peach',
	'sea',
	'lemon',
]

for i in js:
	l=list()
	for j in js[i]:
		for k in word:
			j=j.replace(k,' '+k+' ')
		while '  ' in j:
			j=j.replace('  ',' ')
		while j.startswith(' '):
			j=j[1:]
		while j.endswith(' '):
			j=j[:-1]
		l.append(j)
	js[i]=l


sve('color.json',js)
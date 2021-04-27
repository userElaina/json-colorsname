import os
import json

PTH=os.path.abspath(os.path.dirname(__file__))+'/color.json'

colorsname=json.loads(open(PTH,'rb').read())

print('import',__name__,'succ')

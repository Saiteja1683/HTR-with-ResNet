import os
import json
with open('labels.json') as f:
  data = json.load(f)
  for i in data:
	if os.path.isfile(i):
		#print('exist')
		continue
	else:
		print(i)

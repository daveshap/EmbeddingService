import requests
from pprint import pprint
from time import time


#payload = ['This is a sentence', 'this is a second sentence']
payload = ['Reduce suffering.', 'Increase prosperity.', 'Increase understanding.']
#payload = 'The fat cat hit the bat and the rat'
start = time()
response = requests.request(method='POST', url='http://127.0.0.1:999', json=payload)
end = time()
pprint(response.json())
print('Total time:', end - start)
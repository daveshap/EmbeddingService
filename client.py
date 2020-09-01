import requests
from pprint import pprint
from time import time


payload = ['This is a sentence', 'this is a second sentence']
start = time()
response = requests.request(method='POST', url='http://127.0.0.1:999', json=payload)
end = time()
pprint(response.json())
print('Total time:', end - start)
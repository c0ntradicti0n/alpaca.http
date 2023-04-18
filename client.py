import sys
from pprint import pprint

import requests
import time



def instruct(instruction):
    data = {'prompt': instruction}

    response = requests.post('http://127.0.0.1:5432/prompt', data=data)
    prompt_id = response.content.decode("utf8").strip()

    status_code = 202
    while status_code == 202:
        response = requests.get(f'http://127.0.0.1:5432/prompt/{prompt_id}')
        status_code = response.status_code
        if status_code == 200:
            break
        else:
            time.sleep(1)
    return response.json()


pprint(instruct(sys.argv[1]))

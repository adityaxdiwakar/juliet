import time
import json
import string
import random

def id_generator(size=22, chars=string.ascii_lowercase + string.digits + string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


count = 1
while True:
    fields = ["company", "size", "colors", "current_location"]
    responses = {}

    print(f"\nNow starting item {count}...\n")

    for field in fields:
        response = input(f"Next field [{field}] value: ")
        if field == "current_location": 
            responses.update({
                field: {
                    "location": response,
                    "time": int(time.time())
                }
            })
        responses.update({
            field: response
        })
        
    responses.update({"id": id_generator()})
    print(responses)

    f_content = json.load(
        open("bin/ff.json", "r")
    )
    f_content.append(responses)
    json.dump(
        f_content,
        open("bin/ff.json", "w"),
        indent = 4
    )

    count += 1

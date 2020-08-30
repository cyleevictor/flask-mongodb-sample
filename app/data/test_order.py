import json


class TestOrder():
    name = "hello"
    description = "something to note"


order1 = TestOrder()
order1.name = "hey"
order1.description = "What's up"

json_string = json.dumps(order1.__dict__)
print(json_string)

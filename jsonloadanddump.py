#JSON is a syntax for storing and exchanging data.
#It is text written with JavaScript object notation.
#parse JSON with a Python program

#JSON string to Python dictionary
import json
det_json = '{"name":"ABCD", "age":35, "address":"ADG123"}'
parse_json = json.loads(det_json) #Here parse_json is a JSON object.
print(parse_json["address"])

#Python object to JSON string

x = {
  "name": "John",
  "age": 30,
  "address":"ADG123"
}
y = json.dumps(x) #converted to JSON
print(y)








#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json 

# with open('test.json') as f:
#     data = json.load(f)

# print(type(data))
# print(data)
# print(data['name'])
# print(data['age'])
 
# s = '{"name":"Amy", "age":20, "married":false, "city":"New York", "languages": ["English", "French"]}'
s = '{"prompt": "<prompt text>", "completion": "<ideal generated text>"}'
data = json.loads(s)

# with open('test.json') as f:
# data = json.loads(f)

print(type(data))
print(data)
print(data['prompt'])
print(data['completion'])
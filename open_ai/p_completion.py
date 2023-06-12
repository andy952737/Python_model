import subprocess
import os
import json
import openai

def load_api_key(secrets_file="secrets.json"):
    with open(secrets_file) as f:
        secrets = json.load(f)
    return secrets["OPENAI_API_KEY"]

# def load_test_data(datas_file="p_test.json"):
#     with open(datas_file) as f:
#         datas = json.load(f)
#     return datas["prompt"] 

api_key = load_api_key()
get_open_api_key = openai.api_key = api_key
# # print(get_open_api_key)

# data = load_test_data()
# print(data)

with open('p_test.json', 'r') as file:
    data = json.load(file)

for i,obj in enumerate(data, start=1):
    # 處理每個 JSON 物件
    prompt = obj['prompt']
    completion = obj['completion']
    print(f"Number: {i}")
    print(f"prompt: {prompt}")
    print(f"completion: {completion}")

# Completion 
# Old: openai.api_key_path = os.environ["api-key"]
openai.api_key_path = os.getenv(get_open_api_key)
completion = openai.Completion.create(	
  model="text-davinci-003",
  prompt="Say this is a test",
  max_tokens=7,
  temperature=0
)  
print(completion)
# {
#   "id": "cmpl-uqkvlQyYK7bGYrRHQ0eXlWi7",
#   "object": "text_completion",
#   "created": 1589478378,
#   "model": "text-davinci-003",
#   "choices": [
#     {
#       "text": "\n\nThis is indeed a test",
#       "index": 0,
#       "logprobs": null,
#       "finish_reason": "length"
#     }
#   ],
#   "usage": {
#     "prompt_tokens": 5,
#     "completion_tokens": 7,
#     "total_tokens": 12
#   }
# }

# ChatGPT
# openai.api_key_path = os.getenv(get_open_api_key)
# completion = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "user", "content": "Hello!"}
#   ]
# )
# print(completion.choices[0].message)

# 執行指令並捕獲輸出
# result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
# text = "Hello, 愛看房咖啡"
# result_say = subprocess.run(['say', text])
# result_say = subprocess.run(['say', completion.choices[0].message])

# 印出指令執行結果
# print(result.stdout)
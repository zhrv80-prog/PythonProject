import requests

def function(*args, **kwargs):
    print(f"Позиционные: {args}")
    print(f"Именованные: {kwargs}")

function(1, 2, 3, name="Анна", age=25)
# Позиционные: (1, 2, 3)
# Именованные: {'name': 'Анна', 'age': 25}

# add = lambda x, y: x + y
# print(add(1, 2))
#
# say_hello = lambda: "Hello!"
# print(say_hello())

# response = requests.get("http://httpbin.org//basic-auth/user/password", auth=("user", "password"))
#
# print(response.status_code)
# print(response.text)

# r = requests.request("CREATE", "http://my-api-example.herokuapp.com/api/info/about")
# print(r.headers)

# data = {
#     "title": "this is my title",
#     "body": "this is body text for this test request",
#     "userId": 1
# }
#
# headers = {
#     "Content-Type": "application/json; charset=UTF-8"
# }
#
# g = requests.get('https://jsonplaceholder.typicode.com/posts/1')
# p = requests.post(
#     'https://jsonplaceholder.typicode.com/posts',
#     headers=headers,
#     json=data)
# s = g.status_code
# h = g.headers['Content-Type']
# e = g.encoding
# j = g.json()
#
# # for key, value in g.headers.items():
# #     print(key, '=>', value)
#
# # print(s)
# # print(h)
# # print(e)
# # print(j)
#
# print(p.json())
#
#

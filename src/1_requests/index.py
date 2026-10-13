import requests

ya = "https://yandex.ru"
large = "https://habrastorage.org/r/w1560/getpro/habr/post_images/753/224/111/753224111d9c766c7e6040411e6a5cf9.jpg"
upload = "https://httpbin.org/anything"

proxy = {"http": "localhost:8080"}

r = requests.get(large, proxies=proxy, verify=False, stream=True)

with open("index.jpg", "rb") as f:
    requests.post(upload, data=f)


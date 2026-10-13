import os

from script import connect

PASSWORD = os.getenv("PASSWORD")

result = connect("PASSWORD")

print(result)

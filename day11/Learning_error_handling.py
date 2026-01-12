
import os

#setup a file path
BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, "data.txt")

try:
    with open("data.txt", "r") as file:
        data = file.read()   
except FileNotFoundError:
    print("The file is not found")
except PermissionError:
    print("Permission denied")
except ValueError:
    print("Value conversion error")


try:
    num = int("abc")
except ValueError:
    print("There is a value error")

try:
    file = open("missiing.txt")
except FileNotFoundError:
    print("The file not found")

    
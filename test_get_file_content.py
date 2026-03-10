from functions.get_file_content import get_file_content

print("Test 1: main.py")
print(get_file_content("calculator", "main.py"))
print()

print("Test 2: pkg/calculator.py")
print(get_file_content("calculator", "pkg/calculator.py"))
print()

print("Test 3: /bin/cat")
print(get_file_content("calculator", "/bin/cat"))
print()

print("Test 4: pkg/does_not_exist.py")
print(get_file_content("calculator", "pkg/does_not_exist.py"))
print()

print("Test 5: lorem.txt")
print(get_file_content("calculator", "lorem.txt"))
print()
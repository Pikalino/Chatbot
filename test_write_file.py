from functions.write_file import write_file

print(write_file("calculator", "lorem.txt", "lorem ipsum dolor sit amet!!"))
print(write_file("calculator", "pkg/newfile.txt", "lorem ipsum dolor sit amet"))
print(write_file("calculator", "/tmp/test.txt", "this should not be allowed"))
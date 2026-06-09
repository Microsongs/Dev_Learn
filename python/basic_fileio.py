# File Write
with open("server_status.txt", "w") as file:
    file.write("Web01: Running\n")
    file.write("DB01: Stopped\n")
    file.write("Cache01: Running\n")

# file Read
with open("server_status.txt", "r") as file:
    content = file.read()

print(content)


with open("server_check.txt", "w") as file:
    file.write("Web01: OK\n")
    file.write("DB01: FAIL\n")
    file.write("Cache01: OK\n")

with open("server_check.txt", "r") as file:
    for line in file:
        print(line.strip())

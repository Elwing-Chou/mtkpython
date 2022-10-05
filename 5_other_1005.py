import subprocess

command = ["ls", "-al"]
result = subprocess.run(command)
print(result)

# command = "dir"
# result = subprocess.run(command, shell=True)
# print(result)
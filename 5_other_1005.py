import subprocess

command = ["ls", "-al"]
result = subprocess.run(command)
print(result)

# command = "dir"
# result = subprocess.run(command, shell=True)
# print(result)

command = ["/usr/local/bin/python3.9",
           "test.py"]

with open("out.txt", "w") as f1, \
     open("err.txt", "w") as f2:
    subprocess.run(command, stdout=f1, stderr=f2)
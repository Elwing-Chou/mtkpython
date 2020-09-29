import subprocess
# dir
cmd = "ls -al"
result = subprocess.run(cmd, shell=True)
print(result)

cmd = ["ls", "-al"]
result = subprocess.run(cmd, shell=False)
print(result)

with open("log.txt", "w") as f:
    subprocess.run(cmd, shell=False, stdout=f)
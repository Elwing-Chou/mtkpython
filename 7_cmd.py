import subprocess
# shell=True: 字串 "ls -al"
# shell=False: ["ls", "-al"]
# shell=True : "dir"
# Popen->communicate [adb-like]
commands = ["ls", "-al"]
# run("dir, shell=True)
with open("logs.txt", "w") as f:
    result = subprocess.run(commands, stdout=f, shell=False)
print(result)
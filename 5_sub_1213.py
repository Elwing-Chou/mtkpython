import subprocess

# subprocess.run("dir", shell=True)

with open("out.txt", "w") as f1, open("err.txt", "w") as f2:
    command = ["ls", "-al"]
    result = subprocess.run(command, shell=False, stdout=f1, stderr=f2)
    print(result)
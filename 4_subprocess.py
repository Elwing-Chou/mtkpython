import subprocess

# shell=True: 字串 "ls -al;rm -rf"
# shell=False: List ["命令", "參數", "參數"] ["ls", "-al", "rm"]

# subprocess.run("dir", shell=True)
result = subprocess.run(["ls", "-al"])
print(result)

with open("out.txt", "w") as f1, open("err.txt", "w") as f2:
    result = subprocess.run(["ls", "-al"], stdout=f1, stderr=f2)
    print(result)

with open("out.txt", "w") as f1, open("err.txt", "w") as f2:
    result = subprocess.run(["pip", "install", "RandomWords"], stdout=f1, stderr=f2)
    print(result)

subprocess.run(["python", "3_gui_1227.py"])
import subprocess

# shell = True: 帶入一個字串(忠實執行)
# shell = False: 帶入一個List(2個以後都是參數)
# run("dir", shell=True)
cmd = ["ls", "-al"]
with open("logs.txt", "w") as f:
    result = subprocess.run(cmd, shell=False, stdout=f)
    print(result)
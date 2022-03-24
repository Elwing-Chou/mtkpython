import subprocess

# run: shell->要不要從shell執行這個指令
# win: dir就一定要shell=True
# linux/mac: ls -al shell=False
# 萬不得已不要shell=True
# shell=True, command="ls -al&rm -rf"
# shell=False, command=["命令", "參數"]
# ["ls", "-al", "rm -rf"
# C:\\
command = [r"/usr/local/bin/python3.9",
           "-m",
           "pip",
           "install",
           "--trusted-host=pypi.org --trusted-host=files.pythonhosted.org --trusted-host=pypi.python.org",
           "sqlalchemy==1.3.0"]
result = subprocess.run(command)
print(result)

command = [r"/usr/local/bin/python3.9",
            "test.py"]
with open("out.txt", "w") as f1, open("err.txt", "w") as f2:
    result = subprocess.run(command, stdout=f1, stderr=f2)
    print(result)
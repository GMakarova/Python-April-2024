import subprocess
import os

terraform_directory = ""
os.chdir(terraform_directory)

subprocess.run(["terraform", "init"], check=True)
subprocess.run(["terraform", "plan"], check=True)
subprocess.run(["terraform", "apply", "-auto-approve"], check=True)

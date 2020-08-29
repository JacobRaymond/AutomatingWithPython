import subprocess

#Print "Hello World" (from example.py) five times.
for i in range(0,5):
    subprocess.check_call(["python3", "example.py"])

# Can run "python3 Terminal.py" in Terminal to execute.
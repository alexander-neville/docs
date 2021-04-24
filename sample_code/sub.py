import subprocess

#subprocess.run('ls -la', shell=True)
#output = subprocess.run(['ls', '-la'])
#output = subprocess.run(['ls', '-la'], capture_output=True)
#print(type(output))
#print(output.returncode)
#print(output.stdout.decode())

output = subprocess.run(['ls', '-la'], capture_output=True, text=True)
print(output.stdout)

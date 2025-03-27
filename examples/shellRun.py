import swaglib

command = swaglib.shellRun("echo hello from swaglib!")

print(command.strip())
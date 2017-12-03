cmd = ["ls", "cat", "w"]
cmd.append("mkdir")
print(cmd)

cmd2 = ["file", "echo", "curl"]
cmd.extend(cmd2)
print(cmd)

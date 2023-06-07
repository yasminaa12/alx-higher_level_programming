#!/usr/bin/python3
output = ""
for r in range(ord('a'), ord('z')+1):
    if chr(r) not in ['q', 'e']:
        output += "{}".format(chr(r))

print(output, end="")

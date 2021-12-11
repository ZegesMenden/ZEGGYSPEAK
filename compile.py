# operations for ZEGGYSPEAK

# ZEGGYSPEAK operates on a list of empty integers that is 1000 spaces wide

# the language operates by having a "pointer" to any one of these 1000 spaces.
# the pointer start at address zero, and can move to any valid address via zeggy operations
# when the pointer is at any address, it can perform operations on the current memort at the address
# things like iteration, reading, writing, etc.

# timing

# zeggy <ms> - delay for x ms where x is the input parameter, defaults to 1 if no input is given

# arithmatic operations

# zegGy <x> - iterate current block by x, defaults to 1
# zeGgy <x> - iterate current block by -x, defaults to -1

# movement commands 

# Zeggy <x> - move -x integers in memory space (move to the "left" x memory spaces)
# zeggY <x> - move x integers in memory space (move to the "right" x memory spaces)

# IO commands

# zEGGy <no_params> - read the CLI for a number and write it to the current address
# zEggy <x> - write the current address to the CLI, set x to 1 to print as a string instead of an integer

# commands

print("initializing zeggyspeak commands...")

def zeggy(arg): # sleep millis
    return f'sleep({arg/1000})\n'

def zegGy(arg): # iterate up
    return f'mem[cpos] += {arg}\n'

def zeGgy(arg): # iterate down
    return f'mem[cpos] -= {arg}\n'

def Zeggy(arg): # move right
    return f'''cpos -= {arg}
if cpos < 0:
    cpos = 0\n'''

def zeggY(arg): # move left
    return f'''cpos += {arg}
if cpos >= 999:
    cpos = 999\n'''

def zEGGy(arg):
    return f'''inp = input()
if inp.isalpha():
    mem[cpos] = chr(inp[0])
else:
    mem[cpos] = int(inp)\n'''

def zEggy(arg):
    if arg == 1:
        return f'print(chr(mem[cpos]))\n'
    else:
        return f'print(mem[cpos])\n'

def ZEGGY(arg):
    if arg < 10:
        return f'mem{arg} = mem[cpos]\n'
    else:
        return f'mem0 = mem[cpos]\n'

def ZEGGy(arg):
    if arg < 10:
        return f'mem[cpos] = mem{arg}\n'
    else:
        return f'mem[cpos] = mem0\n'

def ZegGy(arg):
    if arg < 10:
        return f'mem[cpos] += mem{arg}\n'
    else:
        return f'mem[cpos] += mem0\n'

def ZeGgy(arg):
    if arg < 10:
        return f'mem[cpos] -= mem{arg}\n'
    else:
        return f'mem[cpos] -= mem0\n'

def ZEggy(arg):
    return f'mem[cpos] = 0\n'

def zeGGY(arg):
    return f'''if mem[cpos] != 0:
cpos = {arg}
'''

print("commands initialized")

output = ""

startup_code = '''from time import sleep
mem = [0 for x in range(1000)]
cpos = 0
mem1 = 0
mem2 = 0
mem3 = 0
mem4 = 0
mem5 = 0
mem6 = 0
mem7 = 0
mem8 = 0
mem9 = 0
mem0 = 0
'''
output += startup_code

# open the file
f = open("main.zs", "r")

print("parsing ZEGGYSPEAK operations")

for line in f:

    line_split = line.split(' ')
    if len(line_split) > 2:
        op = line_split[0]
        if line_split[1] == '' or line_split[1].isalpha():
            arg = 0
        else:
            arg = int(line_split[1])
        
        if op == "zeggy":
            output += zeggy(arg)
        elif op == "zegGy":
            output += zegGy(arg)
        elif op == "zeGgy":
            output += zeGgy(arg)
        elif op == "Zeggy":
            output += Zeggy(arg)
        elif op == "zeggY":
            output += zeggY(arg)
        elif op == "zEGGy":
            output += zEGGy(arg)
        elif op == "zEggy":
            output += zEggy(arg)
        elif op == "ZEGGY":
            output += ZEGGY(arg)
        elif op == "ZEGGy":
            output += ZEGGy(arg)
        elif op == "ZegGy":
            output += ZegGy(arg)
        elif op == "ZeGgy":
            output += ZeGgy(arg)
        elif op == "ZEggy":
            output += ZEggy(arg)
        # elif op == "":
        #     output += (arg)
        
        else:
            output += '\n'
    else:
        output += '\n'
    
print("parsed!")

f.close()

print("closing main.zs")

f = open("output.py", "w")
print("writing output code...")
f.write(output)
print("code written!")
f.close()
print("output.py closed, compiling complete!")
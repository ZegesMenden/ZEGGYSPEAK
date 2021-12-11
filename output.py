from time import sleep
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
inp = input()
if inp.isalpha():
    mem[cpos] = chr(inp[0])
else:
    mem[cpos] = int(inp)

mem[cpos] = 0

inp = input()
if inp.isalpha():
    mem[cpos] = chr(inp[0])
else:
    mem[cpos] = int(inp)
mem1 = mem[cpos]

mem[cpos] = 0
inp = input()
if inp.isalpha():
    mem[cpos] = chr(inp[0])
else:
    mem[cpos] = int(inp)


mem[cpos] = mem0

cpos -= 1
if cpos < 0:
    cpos = 0
mem[cpos] = mem1

cpos += 1
if cpos >= 999:
    cpos = 999
mem0 = mem[cpos]

cpos -= 1
if cpos < 0:
    cpos = 0
mem[cpos] += mem0

print(mem[cpos])

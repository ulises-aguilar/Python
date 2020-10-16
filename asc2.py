for i in range (32,127):
	c = chr(i)
print("[", i, "=",c, "]", end="")
if (i % 7 == 0):
	print()

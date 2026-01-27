def chop(t):
	del t[0]
	del t[-1]

fruits = ["Apple","Bannana","Strawberry","Orange","Pear"]
chop(fruits)
print("Fruits:",fruits)
def middle(t):
	t = t[0:]
	del t[0]
	del t[-1]
	return t

fruits = ["Apple","Bannana","Strawberry","Orange","Pear"]
new_fruits = middle(fruits)
print("New Fruit:", new_fruits)

# リストa 内の位置 (x,y) に大きさ (w,h) の矩形を描く。
def drawrect(a, x, y, w, h):
    for px in range(x, x+w):
        a[px][y] = 1
        a[px][y+h-1] = 1
    for py in range(y, y+h):
        a[x][py] = 1
        a[x+w-1][py] = 1
    return


canvas = [[0]*10 for i in range(10)]
drawrect(canvas, 0, 0, 10, 10)
drawrect(canvas, 2, 3, 6, 4)
for line in canvas:
    print(line)

# List (mutable)
print("List")
list_a = [1, 2, 3, 4]
for list_a_it in list_a:
    print(list_a_it)

# Tuple (imutable)
print("Tuple")
tuple_a = (1, 2, 3, 4)
for tuple_a_it in tuple_a:
    print(tuple_a_it)

# Dictionary
print("Dictionary")
dict_a = {"abc": 1, "def": 2, "ghi": 1}
for dict_a_it in dict_a:
    print(dict_a_it)
    print(dict_a[dict_a_it])

# Set
print("Set")
set_a = {"abc", "def", "ghi"}
for set_a_it in set_a:
    print(set_a_it)

# Function
print("Function")


def add(x, y):
    return x+y


print(add(1, 2))

# Exception
print("Exception")
try:
    print("a" / 5)
except Exception as e:
    print("Exception occured!")

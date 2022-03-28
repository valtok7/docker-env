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

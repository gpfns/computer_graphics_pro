from math import sqrt, cos, sin


def bf_ld(x1, y1, x2, y2):
    m = (y2 - y1) / (x2 - x1)
    c = y1 - m * x1
    l1 = []

    def cal_y(x):
        return m * x + c

    for i in range(x1, x2 + 1):
        l1.append((i, round(cal_y(i))))
    return(l1)


def dda_bia(x1, y1, x2, y2):
    dy = y2 - y1
    dx = x2 - x1
    l1 = []
    steps = max(dx, dy)
    x_inc = round(dx / steps, 2)
    y_inc = round(dy / steps, 2)
    x = x1
    y = y1
    l1.append((x1, y1))
    for i in range(steps):
        x = round(x + x_inc, 2)
        y = round(y + y_inc, 2)
        l1.append((round(x), round(y)))
    return(l1)


def bresenham_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx
    cl = 2 * dy
    cu = 2 * (dy - dx)
    x, y = x1, y1
    l1 = [(x, y)]
    for i in range(x1, x2):
        if d <= 0:
            d += cl
            x += 1
        else:
            d += cu
            x += 1
            y += 1
        l1.append((x, y))


def sc_circle_drawing(r):
    l1 = []
    for i in range(r + 1):
        l1.append((i, round(sqrt(r * r - i * i))))
    return(l1)


def sc_circle_drawing_deg(r):
    l2 = []
    for i in range(90):
        l2.append((round(r * cos(i)), round(r * sin(i))))
    return(l2)


def mp_circle(r):
    x = 0
    y = r
    d = 5 / 4 - r
    l1 = [(x, y)]
    while x < y:
        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1
        l1.append((x, y))
    return(l1)


def mp_circle_int(r):
    x = 0
    y = r
    d = 1 - r
    l1 = [(x, y)]
    while x < y:
        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1
        l1.append((x, y))
    return(l1)


def ellipse_drawing_algo(a, b):
    p1 = b ** 2 - a ** 2 * b + 0.25 * a ** 2
    x, y = 0, b
    l1 = []
    dx = 2 * b ** 2 * x
    dy = 2 * a ** 2 * y
    while dx < dy:
        l1.append((x, y))
        if p1 < 0:
            x += 1
            dx += 2 * b ** 2
            p1 += dx + b ** 2
        else:
            x += 1
            y -= 1
            dx += 2 * b ** 2
            dy -= 2 * a ** 2
            p1 += dx - dy + b ** 2
    p2 = b ** 2 * (x + 0.5) ** 2 + a ** 2 * (y - 1) ** 2 - (a * b) ** 2
    while y >= 0:
        l1.append((x, y))
        if p2 > 0:
            y -= 1
            dy -= 2 * a ** 2
            p2 += a ** 2 - dy
        else:
            x += 1
            y -= 1
            dx += a * b ** 2
            dy -= 2 * a ** 2
            p2 += dx - dy + a ** 2
    return(l1)

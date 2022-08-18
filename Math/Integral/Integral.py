def metodeRiemanTengah(fx, h, x1, x2):
    xh = abs(x1-x2)/h

    x = x1
    result = 0
    for i in range(h):
        result += xh*(fx((x+(x+xh))/2))
        x += xh

    return result

print(metodeRiemanTengah(lambda x:1/x, 4, 1, 2))


def metodeTrapesium(fx, h, x1, x2):
    xh = abs(x1-x2)/h

    x = x1
    result = 0
    for i in range(h):
        result += xh*(fx(x) + fx(x+xh))/2
        x += xh

    return result

print(metodeTrapesium(lambda x:1/x, 4, 1, 2))
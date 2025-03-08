def triangle(a, b, c):
    if a == b == c:
        return 'equilateral'
    elif a==b or b==c or c==a:
        return 'isosceles'
    else:
        return 'scalene'
#Joshua A Goldstein

#10/13/22

#Area of a rectangular prism calculator


def areacalc(legnth, width):
    return legnth * width


'''
legnth = 4
width = 3
height = 9


'''

def userwidth():

def userheight():
def userlegnth():


area = areacalc(legnth, width)

print("The area is: ",area)


def rectangle_area(side1, side2):
    return side1 * side2
def surfacearea(height, length, width):
    top = rectangle_area(length, width)
    bottom = rectangle_area(length, width)
    front = rectangle_area(height, length)
    back = rectangle_area(height, length)
    left = rectangle_area(height, width)
    right = rectangle_area(height, width)
    total = (top + bottom + front + back + left + right)
    return total



totalArea = surfacearea(height, legnth, width)
print (totalArea)
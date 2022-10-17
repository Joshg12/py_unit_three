#Joshua A Goldstein

#10/13/22

#Area of a rectangular prism calculator

'''
def areacalc(legnth, width):
    return legnth * width



legnth = 4
width = 3
height = 9
area = areacalc(legnth, width)

print("The area is: ",area)


'''
def userwidth():
    userwidth = int(input("What is the width of your rectangular prism?"))
    return userwidth
def userheight():
    userheight = int(input("What is the height of your rectangular prism"))
    return userheight
def userlegnth():
    userlegnth = int(input("What is the legnth of your rectangular prism?"))
    return userlegnth



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
    print(total)
    return total

userheight()
userlegnth()
userwidth()
surfacearea(userheight, userlegnth, userwidth)



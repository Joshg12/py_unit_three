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
#This code takes user input for the width, legnth, and height.


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

#This code defines the area and surface area.

def main():
    the_height = userheight()
    the_legnth = userlegnth()
    the_width = userwidth()
    total = surfacearea(the_height, the_legnth, the_width)
    print("The total is",total)

main()

#This code prints the user's total surface area.


def unit_test(self):
    import sys
    from io import StringIO

    saved_stdout = sys.stdout
    try:
        out = StringIO()
        sys.stdout = out
        output = out.getvalue().strip()
        assert output == "Total Area"
    finally:
        sys.stdout = saved_stdout

#This is the unit test
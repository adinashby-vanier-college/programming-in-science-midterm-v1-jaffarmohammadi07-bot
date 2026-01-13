import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):

    area_of_circle = math.pi * radius**2

    return(round(area_of_circle, 2))
print(area_of_circle(5))

# Q2: Hollow Right Triangle
def hollow_right_triangle(n):
    result = ""

    if n < 4:
        return("The triangle height should be at least 4.")
    
    else:

        for i in range(n):
            if i == 0 or i == 0 + 1 or i == n - 1:
                for k in range(i + 1):
                    result += "*"
                result += "\n"

            else:
                result += "*"
                for j in range(i - 1):
                    result += " "
                result += "*"

                result += "\n"
        
    return result.rstrip()
print(hollow_right_triangle(3))

def hollow_right_triangle(n):
    result = ""

    if n < 4:
        return("The triangle height should be at least 4.")
    
    else:

        for i in range(n):
            if i == 0 or i == 0 + 1 or i == n - 1:
                for k in range(i + 1):
                    result += "*"
                result += "\n"

            else:
                result += "*"
                for j in range(i - 1):
                    result += " "
                result += "*"

                result += "\n"
        
    return result.rstrip()
print(hollow_right_triangle(4))

def hollow_right_triangle(n):
    result = ""

    if n < 4:
        return("The triangle height should be at least 4.")
    
    else:

        for i in range(n):
            if i == 0 or i == 0 + 1 or i == n - 1:
                for k in range(i + 1):
                    result += "*"
                result += "\n"

            else:
                result += "*"
                for j in range(i - 1):
                    result += " "
                result += "*"

                result += "\n"
        
    return result.rstrip()
print(hollow_right_triangle(5))

# Q3: Inverted Pyramid
def inverted_pyramid(n):
    result = ""

    if n < 3:
        return("The pyramid height should be at least 3.")

    else:

        for i in range(n - 1, -1, -1):
            for j in range(n - i - 1):
                result += " "
            for k in range(2 * i + 1):
                result += "*"
            result += "\n"

    return result.rstrip()

print(inverted_pyramid(3))

def inverted_pyramid(n):
    result = ""

    if n < 3:
        return("The pyramid height should be at least 3.")

    else:

        for i in range(n - 1, -1, -1):
            for j in range(n - i - 1):
                result += " "
            for k in range(2 * i + 1):
                result += "*"
            result += "\n"

    return result.rstrip()

print(inverted_pyramid(4))

def inverted_pyramid(n):
    result = ""

    if n < 3:
        return("The pyramid height should be at least 3.")

    else:

        for i in range(n - 1, -1, -1):
            for j in range(n - i - 1):
                result += " "
            for k in range(2 * i + 1):
                result += "*"
            result += "\n"

    return result.rstrip()

print(inverted_pyramid(5))
    

# ----------------------------------------------------------------
print(area_of_circle(5))
print()

print(hollow_right_triangle(3))
print()

print(hollow_right_triangle(4))
print()

print(hollow_right_triangle(5))
print()

print(inverted_pyramid(3))
print()

print(inverted_pyramid(4))
print()

print(inverted_pyramid(5))
print()

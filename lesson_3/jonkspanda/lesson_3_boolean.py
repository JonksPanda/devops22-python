#Write a expression with Boolean Operations that:
#
#    result in True if any of x, y, z is True
#    result in True if all x, y, z is True
#    result in False if any of x, y, z is False
#    result in False if all of x, y, z is False
#    result in False if any of z, y, z is True
#    result in False if all of z, y, z is True

x = True
y = False
z = True

res = x or y or z
print(f"result in True if any of x, y, z is True: {res}")

res = x and y and z
print(f"result in True if all x, y, z is True: {res}")

res = not(not x or not y or not z)
print(f"result in False if any of x, y, z is False: {res}")

res = not(not x and not y and not z)
print(f"result in False if all of x, y, z is False: {res}")

res = not(x or y or z)
print(f"result in False if any of z, y, z is True: {res}")

res = not(x and y and z)
print(f"result in False if all of z, y, z is True: {res}")
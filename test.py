import math

dx = 200
dy = 4

print("Expect 359,  1,  181,  179")

print((math.atan2(dy, dx)*180/math.pi))
print((math.atan2(-dy, dx)*180/math.pi))
print((math.atan2(dy, -dx)*180/math.pi))
print((math.atan2(-dy, -dx)*180/math.pi))
print()

print((math.atan2(dy, dx)*180/math.pi) % 360)
print((math.atan2(-dy, dx)*180/math.pi) % 360)
print((math.atan2(dy, -dx)*180/math.pi) % 360)
print((math.atan2(-dy, -dx)*180/math.pi) % 360)


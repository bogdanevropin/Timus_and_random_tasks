import math

w, h = map(int, input().split())
center_mass_x = 0
center_mass_y = 0
moment_inertia_0 = 0
mass = 0
for y in range(h):
	for x, c in enumerate(input()):
		if c == 1:
			mass += 1
			center_mass_x += x
			center_mass_y += y
			moment_inertia_0 += x * x + y * y

center_mass_x = center_mass_x / mass
center_mass_y = center_mass_y / mass

moment_inertia = moment_inertia_0 - (center_mass_x * center_mass_x + center_mass_y * center_mass_y) * mass
magical_k = moment_inertia / (mass * mass)

if magical_k <= (1 / 6 + 1 / (2 * math.pi)) / 2:
	print("circle")
elif magical_k <= 1 / 6:
	print("square")
else:
	print("triangle")

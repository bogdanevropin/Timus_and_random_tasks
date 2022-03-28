import math

max_length = 1

pattern_centers_1 = [[0.5 + 3 ** (1 / 2) / 2 + 1, 0]]
pattern_centers_2 = [[0, 0.5 + 3 ** (1 / 2) / 2]]


vertical_pattern_step = 1 + 3 ** (1 / 2)
horizontal_pattern_step = 3 + 3 ** (1 / 2)

for vertical_num in range(-max_length, max_length):
    for horizontal_num in range(-max_length, max_length):
        pattern_centers_1.append([pattern_centers_1[0][0] + horizontal_pattern_step * horizontal_num,
                                  pattern_centers_1[0][1] + vertical_pattern_step * vertical_num])
        pattern_centers_2.append([pattern_centers_2[0][0] + horizontal_pattern_step * horizontal_num,
                                  pattern_centers_2[0][1] + vertical_pattern_step * vertical_num])

pattern_centers = pattern_centers_1 + pattern_centers_2

big_radius = 3 ** (1 / 2) / 2 + 0.5

pi: float = math.pi

web_centers = []

for center in pattern_centers:
    web_centers.append([center[0] + big_radius * math.cos(pi / 6),
                        center[1] + big_radius * math.sin(pi / 6)])
    web_centers.append([center[0],
                        center[1] + big_radius])
    web_centers.append([center[0] + big_radius * math.cos(5 * pi / 6),
                        center[1] + big_radius * math.sin(5 * pi / 6)])
    web_centers.append([center[0] + big_radius * math.cos(pi / 6),
                        center[1] - big_radius * math.sin(pi / 6)])
    web_centers.append([center[0],
                        center[1] - big_radius])
    web_centers.append([center[0] + big_radius * math.cos(5 * pi / 6),
                        center[1] - big_radius * math.sin(5 * pi / 6)])



def min_distance(x, y):
    distance = max_length
    for centers in web_centers:
        if ((centers[0] - x) ** 2 + (centers[1] - y) ** 2) ** (1 / 2) < distance:
            distance = ((centers[0] - x) ** 2 + (centers[1] - y) ** 2) ** (1 / 2)
    return distance

finall_x, finall_y = map(float, input().split())

finall_x = finall_x % horizontal_pattern_step
finall_y = finall_y % vertical_pattern_step


print(round(min_distance(finall_x, finall_y), 4))

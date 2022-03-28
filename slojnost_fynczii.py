first_line = input()
start_finish_func_t = tuple(float(item) for item in first_line.split(' '))
second_line = input()
f_data_t = list(float(item) for item in second_line.split(' '))

difficulty = 1
for n in range(len(f_data_t) - 2):
    if (f_data_t[n] < f_data_t[n+1] and f_data_t[n+1] > f_data_t[n+2]) or \
        (f_data_t[n] > f_data_t[n+1] and f_data_t[n+1] < f_data_t[n+2]):
            difficulty += 1
print(difficulty)
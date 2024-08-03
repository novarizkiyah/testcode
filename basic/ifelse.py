
num = [1, 2, 3, 4, 5, 6, -2, 4, 0, -3,-6,-4]

def pos(num):
    pose = [0]

    for number in num:
        if number > 0:
            pose.append(number)
    return pose
            

result = pos(num)
print(result)


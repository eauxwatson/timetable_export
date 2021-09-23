# You are now at the myd1 branch, which adopts the methods preferred by AsakiRain and BiDuang.

import time
import os
import json

# Initialize
if os.name == 'posix':
    clr = 'clear'
elif os.name == 'nt':
    clr = 'cls'
os.system(clr)  # 清屏就用这个啊啊啊!! windows, linux 都可以 :3
time.sleep(1)

ver = 0.1  # Remember to change every new version is released!

print("正在启动 Timetable Export, 请稍后...")
time.sleep(1)
os.system(clr)

# Check whether is the first time running and start a guide if is.
# --snip--

print("看来您已经准备好了, 那我们开始吧!")
time.sleep(1)

# Choose how many classes are there a day.
while True:
    try:
        classes_daily = int(input("在您的学校里, 一天最多会有几节课? "))
    except ValueError:
        print("非法参数. 请输入一个有效数字!")
        continue
    else:
        if classes_daily > 20:
            print("一天不能有超过20节课. 请输入一个有效数字!")
            continue
        else:
            break

# Recording class and its starting and ending time in time.json
time_dict = {}

for count in range(classes_daily):
    # loop for as many times as the number of classes daily.
    setting_now = f'class_{count}'

    def set_start_time():
        """
        Set the start time of a class.
        :return start_time: The start time of the class. (hh:mm, 24-hour time)
        :return num_start_time: The start time of the class without a ':'.
        :rtype start_time: str
        :rtype num_start_time: int
        """

        while True:
            start_time = input(f"请输入第{count+1}节课的上课时间. (hh:mm, 24-hour time) ")
            start_time_split = start_time.split(':')

            if len(start_time_split) != 2 or len(start_time_split[0]) != 2 or len(start_time_split[1]) != 2:
                print("请正确输入时间!")
                continue
            else:
                try:
                    num_start_time = int(''.join(start_time_split))
                except ValueError:
                    print("请正确输入时间!")
                    continue
                else:
                    if num_start_time > 2400:
                        print("不能在第二天上课. 请正确输入时间!")
                        continue
                    else:
                        break

        return start_time, num_start_time

    start_time, num_start_time = set_start_time()
    num_end_time = 0000
    while num_start_time <= num_end_time:
        print("不能在上一节课下课前开始上课. 请输入一个有效时间!")
        start_time, num_start_time = set_start_time()

    def set_end_time():
        """
        Set the end time of a class.
        :return end_time: The end time of the class. (hh:mm, 24-hour time)
        :return num_end_time: The end time of the class without a ':'.
        :rtype end_time: str
        :rtype num_end_time: int
        """

        while True:
            end_time = input(f"请输入第{count+1}节课的下课时间. (hh:mm, 24-hour time) ")
            end_time_split = end_time.split(':')

            if len(end_time_split) != 2 or len(end_time_split[0]) != 2 or len(end_time_split[1]) != 2:
                print("请正确输入时间!")
                continue
            else:
                try:
                    num_end_time = int(''.join(end_time_split))
                except ValueError:
                    print("请正确输入时间!")
                    continue
                else:
                    if num_end_time > 2400:
                        print("不能在第二天下课. 请正确输入时间!")
                        continue
                    else:
                        break

        return end_time, num_end_time
    end_time, num_end_time = set_end_time()
    while num_end_time <= num_start_time:
        print("不能在上一节课下课前开始上课. 请输入一个有效时间!")
        end_time, num_end_time = set_end_time()

    time_key = f'{start_time}, {end_time}'
    time_dict[setting_now] = time_key

time_dict_json = json.dumps(time_dict, indent=4)
with open('time.json', 'w') as f:
    json.dump(time_dict_json, f)

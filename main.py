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
            print("非法参数. 请输入一个有效数字!")
            continue
        else:
            break

# Set the starting and ending time for each class.
setting_now = 0


# 为以后的功能预留空间
class Class:
    """
    The class for all classes.
    """


# Create 'class' child classes and set the start and end time for each of it.
while setting_now < classes_daily:
    
    def set_start_time():
        """
        Set the start time of a class.

        :return start_time: The start time of the class. (hh:mm, 24-hour time)
        :return num_start_time: The start time of the class without a ':'.
        :rtype start_time: str
        :rtype num_start_time: int
        """
        
        while True:
            start_time = input(f"请输入第{setting_now+1}节课的上课时间. (hh:mm, 24-hour time) ")
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
            end_time = input(f"请输入第{setting_now+1}节课的下课时间. (hh:mm, 24-hour time) ")
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
                    if num_end_time >2400:
                        print("不能在第二天下课. 请正确输入时间!")
                        continue
                    else:
                        break
        
        return end_time, num_end_time

    end_time, num_end_time = set_end_time()
    while num_end_time <= num_start_time:
        print("不能在上一节课下课前开始上课. 请输入一个有效时间!")
        end_time, num_end_time = set_end_time()
    
    create_child_class = f"""
class Class{setting_now}(Class):
    '''
    A class of classes at the same time for every day.
    
    :param day_in_week: The day in a week when an instance of this class.
    :type day_in_week: int
    '''
        
    def __init__(self, day_in_week):
        self.start_time = '{start_time}'
        self.end_time = '{end_time}'
        self.day_in_week = day_in_week

Class{setting_now}_dict = {{
    'start_time': '{start_time}',
    'end_time': '{end_time}'
    }}

json_dump_dict = json.dumps(Class{setting_now}_dict, indent=4)
    """
    
    exec(create_child_class)

    # Save settings
    with open('settings.json', 'w') as f:
        json.dump(json_dump_dict, f) # Pylance is unable to detect the actually existing variable inside the string that is operated by exec() above and always reports a problem here, just ignore it.

    setting_now += 1
# While Loop Ends
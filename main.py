import time
import os
from updater import update
import json

# Initialize
if os.name == 'posix':
    clr = 'clear'
elif os.name == 'nt':
    clr = 'cls'
os.system(clr)  # 清屏就用这个啊啊啊!! windows, linux 都可以 :3
time.sleep(1)

ver = 0.1  # Remember to change every new version is released!

print("Launching Timetable Export, please wait...")
time.sleep(1)
os.system(clr)

# Check whether is the first time running and start a guide if is.
# --snip--

print("It looks that you are well-prepared, so let's get started.")
time.sleep(1)

# Choose how many classes are there a day.
while True:
    try:
        classes_daily = int(input("What's the maximum number of classes a day in your school? "))
    except ValueError:
        print("Illegal argument. Please enter a valid number!")
        continue
    else:
        if classes_daily > 20:
            print("Illegal argument. Please enter a valid number!")
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
            start_time = input(f"When does class {setting_now+1} start? (hh:mm, 24-hour time) ")
            start_time_split = start_time.split(':')
            
            if len(start_time_split) != 2:
                print("Please enter the time correctly!")
                continue
            else:
                try:
                    num_start_time = int(''.join(start_time_split))
                except ValueError:
                    print("Please enter the time correctly!")
                    continue
                else:
                    if num_start_time > 2400:
                        print("A class will not start the next day. Please enter the time correctly!")
                        continue
                    else:
                        break
        
        return start_time, num_start_time
    # TODO: 限制小时和分钟都必须为两位数

    start_time, num_start_time = set_start_time()
    num_end_time = 0000
    while num_start_time <= num_end_time:
        print("A class should not start before the last class ends. Please enter a valid time!")
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
            end_time = input(f"When does class {setting_now+1} end? (hh:mm, 24-hour time) ")
            end_time_split = end_time.split(':')
            
            if len(end_time_split) != 2:
                print("Please enter the time correctly!")
                continue
            else:
                try:
                    num_end_time = int(''.join(end_time_split))
                except ValueError:
                    print("Please enter the time correctly!")
                    continue
                else:
                    if num_end_time >2400:
                        print("A class will not end the next day. Please enter the time correctly!")
                        continue
                    else:
                        break
        
        return end_time, num_end_time
    # TODO: 限制小时和分钟都必须为两位数

    end_time, num_end_time = set_end_time()
    while num_end_time <= num_start_time:
        print("A class should not end before it starts. Please enter a valid time!")
        end_time, num_end_time = set_end_time()
    
    create_child_class = f"""
class Class{setting_now}(Class):
    '''
    A class of classes at the same time for every day.
    
    :param weekday: The day in a week when an instance of this class
    :type weekday: int
    '''
        
    def __init__(self, weekday):
        self.start_time = '{start_time}'
        self.end_time = '{end_time}'
        self.weekday = weekday
    """
    
    exec(create_child_class)
    setting_now += 1

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

image_good=mpimg.imread('/home/diego/Documents/HackOxford/Hack-Oxford/Web/Images/academic_brain.png')
image_anxious=mpimg.imread('/home/diego/Documents/HackOxford/Hack-Oxford/Web/Images/anxious_tired_brain.png')
image_slack=mpimg.imread('/home/diego/Documents/HackOxford/Hack-Oxford/Web/Images/slacking_brain.png')


results = ['studied_course', 'Background', 'interested', 'Hours_Study', 'Study_Materials','Alone_Study','Hours_Sleep','Soc_Activ','stressed_anx','Exp_GPA','Calc_GPA']



exp_gpa = results[-2]
calc_gpa = results[-1]

hours_study = results[4]




if exp_gpa < calc_gpa:
    print('Be Careful')

else:
    print('You are on good track')


if hours_study > 3:
    print('you study a lot')

elif: hours_sleep < 6
    print('you do not study too much')

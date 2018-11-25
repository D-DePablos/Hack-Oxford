import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from matplotlib import animation

case = random.sample([1,2,3], 1)[0]

if case == 1:
    with cbook.get_sample_data('/home/diego/Documents/HackOxford/Hack-Oxford/Web/Images/academic_brain.png') as file:
        image = plt.imread(file)
    suggestions = ['Congratulations!',  'You are on track.', 'Stay curious and try our StudyBuddy feature.']
elif case==2:
    with cbook.get_sample_data('/home/diego/Documents/HackOxford/Hack-Oxford/Web/Images/slacking_brain.png') as file:
        image = plt.imread(file)
    suggestions = ['You need to get more organised.',  'Check out #videos that can help you organise better.', 'Stay curious and try our StudyBuddy feature.']
elif case==3:
    with cbook.get_sample_data('/home/diego/Documents/HackOxford/Hack-Oxford/Web/Images/anxious_tired_brain.png') as file:
        image = plt.imread(file)
    suggestions = ['You should focus on your well-being first',  'Decrease stress levels, sleep more and engage.', 'Stay curious and try our StudyBuddy feature.']


fig, ax = plt.subplots()
figure = ax.imshow(image)


ims=[]
for iternum in [0,1,2]:
    title = plt.text(0.5,1.01,suggestions[iternum], ha="center",va="bottom",color=np.random.rand(3), transform=ax.transAxes, fontsize=12)
    ims.append([figure,title,])


animated = animation.ArtistAnimation(fig, ims, interval=5000, blit=False, repeat_delay=2000)


ax.axis('off')
plt.show()

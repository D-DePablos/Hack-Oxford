import pandas as pd
import numpy as np
import os


Questions = ['What course are you taking',
             'What is your background?',
             'How interested are you in this course?',
             'How many hours do you study this course per week for ?',
             'What study materials you use for the course?',
             'Have you done any practical work in the course?',
             'Do you prefer to study alone?',
             'How many hours of sleep per night do you usually have?',
             'What of the following social activities do you participate in?',
             'Have you been feeling stressed or unmotivated lately?',
             'Expected Grade in the course']

Answers = ['Linear Algebra:Probability and Statistics:Databases:Functional Programming:Biochemistry:Genetics:Organic Chemistry:English:Latin:Mandarin',
           'Mathematics:Computer Science:Biology:Chemistry:Languages:History',
           '0:1:2:3:4:5:6:7:8:9:10',
           '0:1:2:3:4:5:6:7:8:9:10+',
           'Lecture Slides:Notes:Books-Recommended:Books-Out Of Course:Internet Resources(Videos, Articles)',
           'Yes:No:NA:Prefer not to Say',
           'Yes:No',
           '0:1:2:3:4:5:6:7:8:9:10+',
           'Sports:Volunteering Work:Fishing:Modelling:Programming:Friend Circle in the University',
           'Yes:No',
           '1:2:3:4'
           ]


Ans_type = ['single','single', 'single', 'single', 'multiple', 'single',
            'single', 'single', 'multiple', 'single', 'single']


data = pd.DataFrame({'Questions': Questions,
                     'Answers': Answers,
                     'Ans_type': Ans_type})


data.to_csv('/home/diego/Documents/HackOxford/Hack-Oxford/data.csv')

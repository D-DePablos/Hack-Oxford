import pandas as pd
data=pd.read_csv("data.csv")
print (data.columns)

my_list=[]
import random
random.seed(2762)
f=open("generated_data.csv","w")
f.write("student_id,")
mlist=[]
for i,x in data.iterrows():
    q=x['Questions']
    mlist.append(x['Questions'])
questions=','.join(mlist)

f.write(questions)
f.write(',cgpa\n')

for k in range(0,5000):
    f.write(str(k))
    f.write(',')
    for i,x in data.iterrows():
        question=x['Questions']
        possible_answers=x['Answers']
        ans_type=x['Ans_type']
        possible_answers_list=possible_answers.split(':')
        if ans_type=='single':
            answer=random.sample(possible_answers_list,1)
        else:
            answer=random.sample(possible_answers_list, random.randint(1, len(possible_answers_list)))
        answer=':'.join(answer)
        f.write(answer+',')
    mylist=[1,1.5,2,2.5,3,3.5,4]
    cgpa=random.randint(0, len(mylist)-1)
    #print (cgpa)
    cgpa=mylist[cgpa]
    f.write(str(cgpa))
    f.write('\n')
f.close()





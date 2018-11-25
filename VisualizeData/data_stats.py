import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('/home/diego/Documents/HackOxford/Hack-Oxford/CreateData/generated_datav2.csv')
# Reduce Dataset

df = df.set_index("student_id", drop=False)
df.Hour_week[df.Hour_week == '10+'] = 10
df.Hour_week = pd.to_numeric(df.Hour_week)
df.Sleep_hours[df.Sleep_hours == '10+'] = 10
df.Sleep_hours = pd.to_numeric(df.Sleep_hours)
df.Practical_Work[df.Practical_Work.isna()] = 'Prefer not to Say'

# Count number of social activities student does
Empty = np.full(5000, 5000)
Truth_Table_Sports = pd.DataFrame({'Modelling': Empty,
                                   'Sports': Empty,
                                   'Friends': Empty,
                                   'Fishing': Empty,
                                   'Volunteer': Empty})


for index, data in enumerate(df.Soc_Activ):
    Truth_Table_Sports.Modelling[index] = data.count('Modelling')
    Truth_Table_Sports.Sports[index] = data.count('Sports')
    Truth_Table_Sports.Friends[index] = data.count(
        'Friend Circle in the University')
    Truth_Table_Sports.Fishing[index] = data.count('Fishing')
    Truth_Table_Sports.Volunteer[index] = data.count('Volunteering Work')
dfsp = df.join(Truth_Table_Sports)


# Stratify: Expected Grade and performance: Higher expectations?? Show Groups of students DONE

Undr = df.where(df.Curr_GPA > df.Exp_GPA)
Over = df.where(df.Curr_GPA < df.Exp_GPA)
Exact = df.where(np.sqrt((df.Curr_GPA - df.Exp_GPA)**2) < 1)
Undr = Undr[pd.notnull(Undr['student_id'])]
Over = Over[pd.notnull(Over['student_id'])]
Exact = Exact[pd.notnull(Exact['student_id'])]

# If they are under: WHY?

# Happiest people
Happy_Dataset = Exact[Exact.Hour_week <= 3]
Happy_Dataset = Happy_Dataset[Happy_Dataset.Curr_GPA >= 3]
Happy_Dataset = Happy_Dataset[Happy_Dataset.interested >= 5]
Happy_Dataset = Happy_Dataset[Happy_Dataset.Sleep_hours >= 6]
Happy_Dataset = Happy_Dataset[Happy_Dataset.stressed_anx == 'No']

# Most Sad People
Sad_Dataset = df[df.Hour_week >= 3]
Sad_Dataset = df[df.Curr_GPA < 3]
Sad_Dataset = df[df.interested <= 4]
Sad_Dataset = df[df.Sleep_hours <= 6]
Sad_Dataset = df[df.stressed_anx == 'Yes']


sns.set(style="whitegrid", palette="pastel", color_codes=True)

# Draw a nested violinplot and split the violins for easier comparison
sns.violinplot(x="Exp_GPA", y="Curr_GPA", hue="Alone_Study",
               split=True, inner="quart",
               palette={"Yes": "y", "No": "b"},
               data=Happy_Dataset)
sns.despine(left=True)


sns.violinplot(x="Exp_GPA", y="Curr_GPA", hue="Alone_Study",
               split=True, inner="quart",
               palette={"Yes": "y", "No": "b"},
               data=Sad_Dataset)


sns.relplot(x="Exp_GPA", y="Curr_GPA", hue="Background", size="Sleep_hours",
            sizes=(40,250), alpha=.5, palette="muted",
            height=6, data=Happy_Dataset)
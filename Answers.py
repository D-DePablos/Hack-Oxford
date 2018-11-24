import pandas as pd
import numpy as np


Questions = np.array('What is your Background?',
                    'How interested are you in this course?',
                    '',
                    '',
                    '',
                    '',
                    )
Answers = ['Mathematics, Computer Science, Philosophy',
           'C:D:E']


Ans_type = []


pd.DataFrame({'Questions': Questions,
              'Answers': Answers})

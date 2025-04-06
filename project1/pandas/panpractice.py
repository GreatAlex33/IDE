from IPython.display import display
import pandas as pd
student_data = pd.read_csv('data/students_performance.csv', sep=',')
#Каков балл по письму у студента под индексом 155?
#display(student_data.loc[155])
#Сколько суммарно пропущенных значений в таблице?
#display(student_data.describe(include='object'))
#Каков у студентов средний балл по математике?
#display(student_data['math score'].mean())
#Какая расовая группа является самой крупной в учебном заведении?
#display(student_data['race/ethnicity'].value_counts())
#Каков средний балл по чтению у студентов, которые посещали курсы подготовки к экзаменам?
#display(student_data[student_data['test preparation course'] == 'completed']['writing score'].mean())
#Сколько студентов получили 0 баллов по математике?
#display(student_data[student_data['math score'] == False].shape[0])
#Проверьте гипотезу: у студентов с оплачиваемым питанием средний балл по математике выше, чем у студентов с льготным питанием.
#display(student_data[student_data['lunch'] == 'standard']['math score'].mean())
#Каков процент студентов, родители которых имеют высшее образование уровня бакалавриата (bachelor's degree)?
#display(student_data['parental level of education'].value_counts(normalize=True))
#Насколько медианный балл по письму у студентов в расовой группе А отличается от среднего балла по письму у студентов в расовой группе C?
#GA_WS = student_data[student_data['race/ethnicity'] == 'group A']['writing score'].median()
#GC_WS = student_data[student_data['race/ethnicity'] == 'group C']['writing score'].mean()
#print(GA_WS - GC_WS)

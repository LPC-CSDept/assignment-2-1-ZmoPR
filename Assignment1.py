m_total = int(input('Number of Males: '))
f_total = int(input('Number of Females: '))
student_total = m_total + f_total

print('Total Number of Students:', student_total)

print('The number of Males and Females:', m_total,f_total)

m_perc = m_total / student_total 
m_perc = m_perc * 100
f_perc = f_total / student_total 
f_perc = f_perc * 100


print(f'The Percentage of Males and Females: \t {m_perc:.2f}% \t {f_perc:.2f}%')
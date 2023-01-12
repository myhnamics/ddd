subjects= { '진동공학':'A+','열전달':'A+', '기계설계':'A0'}
subject = '진동공학'
student = 'kim'
print(subjects[subject])

# old style
print('%s 학생의 %s 과목 성적은 %s'%(student, subject, subjects[subject]))
# modern style
print('{0} 학생의 {1} 과목 성적은 {2}입니다.'.format(student, subject, subjects[subject]))
# ultra modern style
print(f'{student} {subject} subject grade is {subjects[subject]} ')

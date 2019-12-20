"""
百分制成绩转等级制成绩
90分及以上: A
80~89分:   B
70~79分:   C
60~69分:   D
60分以下:   E

Version: 0.1
Author: 子梁
Date: 2019-12-19
"""
score = float(input('请输入分数:'))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('对应的等级是:', grade)
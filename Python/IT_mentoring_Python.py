# Example 1
width_of_the_rectangle = 10
height_of_the_rectangle = 5
area_of_the_rectangle = width_of_the_rectangle*height_of_the_rectangle

print('The area of the rectangle is ' + str(area_of_the_rectangle) + ' cm')

# Example 2 Sets
slavic_girls_who_code = {'PowerBi', 'SQL', 'Git', 'Google Analytics', 'Python'}
liza = {'Python', 'SQL', 'Javascript', 'Docker', 'React', 'Git'}

print('Common ' + '= ' + str(slavic_girls_who_code.intersection(liza)))
print('Only_slavic_girls_know ' + '= ' + str(slavic_girls_who_code.difference(liza)))
print('All_our_skills ' + '= ' + str(slavic_girls_who_code.union(liza)))

# common = set(slavic_girls_who_code)
# common.update(liza)
# only_slavic_girls_know = set(slavic_girls_who_code)
# only_slavic_girls_know.discard('SQL')
# only_slavic_girls_know.discard('Python')
# only_slavic_girls_know.discard('Git')
# only_slavic_girls_know.add('Azur')
# only_slavic_girls_know.add('Tableau')
# all_our_skills = set(slavic_girls_who_code)
# all_our_skills.update(liza)
# all_our_skills.update(only_slavic_girls_know)
#
# print('Common ' + '= ' + str(common))
# print('Only_slavic_girls_know ' + '= ' + str(only_slavic_girls_know))
# print('All_our_skills ' + '= ' + str(all_our_skills))

# Example 3 Slicing
month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
print('The summer_month are ' + str(month[5:8]) + ' and the not_summer_month are ' + str(month[:5]) + str(month[8:]))


# Example 4 For
customers = [44, 19, 18, 17, 25]
for i in customers:
    if i >= 18:
        print('You can buy alcohol')
    else:
        print('You cannot buy alcohol')

# Example 5
A = int(input()) #it is recommended to sleep A hours
B = int(input()) #do not sleep more than B hours
H = int(input()) #Anya sleeps now
if A > B:
    print('Error! The number A must be less than or equal to B.')
elif H > B:
    print('Пересып')
elif H < A:
    print('Недосып')
else:
    print('Это нормально')


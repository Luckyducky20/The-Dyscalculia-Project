

from math import floor
import stdarray

Words = stdarray.create1D(10, 'none')
complete = stdarray.create1D(10, 'none')

complete = ['', 'teens', 'Twenty', 'Thirty', 'Fourty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'onehundred']

Words[0] = ('')
Words[1] = ('-One')
Words[2] = ('-Two')
Words[3] = ('-Three')
Words[4] = ('-Four')
Words[5] = ('-Five')
Words[6] = ('-Six')
Words[7] = ('-Seven')
Words[8] = ('-Eight')
Words[9] = ('-Nine')


def tens(number):
    
    #number -= 1
    returnable = floor(number / 10)
    #print()

    return complete[returnable]

for i in range(100):
    print("Words[{}] = ('{}{}');".format(i, tens(i), Words[((i+1) % 10) - 1]))



'''
for i in range(12):
    print('Months[{}] = ""'.format(i))
'''
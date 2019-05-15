from datetime import date
num = int(date.today().strftime('%j'))
#Checking if it's after Dec 01
if num > 335:
    print ('Happy Holidays!')
else:
   print ('Bah humbug.')

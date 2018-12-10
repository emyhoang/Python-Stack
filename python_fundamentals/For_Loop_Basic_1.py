# # # 1.Basic - Print all the numbers/integers from 0 to 150.
def print():
  for i in range (0, 151):
      print(i)
print()

# # 2.Multiples of Five - Print all the multiples of 5 from 5 to 1,000,000.
def multiples_of_five():
  for i in range(5,1000000,5):
      print(i)
multiples_of_five()

# # # 3.Counting, the Dojo Way - Print integers 1 to 100.  If divisible by 5, 
# # # print "Coding" instead. If by 10, also print " Dojo".
def divisible_by():
  for i in range(1,101):
    if i%5!=0:
        print(i)
    else: 
        print("Coding")
    if i%10==0:
      print("Dojo")
divisible_by()

# # # 4.Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and 
# # # print the final sum.
def sum_odd():
  sum=0
  for i in range(500000):
      if i%2 == 1:
        sum+=i
        print(sum)
sum_odd()

# # # # # 5.Countdown by Fours - Print positive numbers starting at 2018, counting 
# # # # down by fours (exclude 0).
def count_down_by_fours():
  for i in range (2018, 1, -4):
      print(i)
count_down_by_fours()


# # # 6.Flexible Countdown - Based on earlier "Countdown by Fours", given lowNum, 
# # # highNum, mult, print multiples of mult from lowNum to highNum, using a 
# # # FOR loop.  For (2,9,3), print 3 6 9 (on successive lines)
def flexible_countdown(low,high, mult):
  for i in range(1, high):
      if mult * i > low and mult * i <= high: 
          print(mult * i )
flexible_countdown(2,9,3)


def outputs():
  my_list = [3,5,1,2]
  for i in my_list:
    print(i)
outputs()
# 3,5,1,2

def outputs():
  my_list = [3,5,1,2]
  for i in range(my_list):
      print(i)
outputs()
# error

def outputs():
  my_list = [3,5,1,2]
  for i in range(len(my_list)):
      print(i)
outputs()
#prints each index for the list
#0,1,2,3



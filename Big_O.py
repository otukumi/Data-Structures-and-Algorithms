1. #Let us say your expense for every month are listed below,
# 	1. January -  2200
#  	2. February - 2350
#     3. March - 2600
#     4. April - 2130
#     5. May - 2190
#
# Create a list to store these monthly expenses and using that find out,
#
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

#fuck shit just use simple line to make the time complexity small



'''my_dictionary={"January":2200,"February":2350,"March":2600,"April":2130,"May":2190}

extra=my_dictionary['February']-my_dictionary['January']

print(extra)

total_expenses=my_dictionary['February']+my_dictionary['January']+my_dictionary['March']
print(total_expenses)
for value in my_dictionary.values():
     if value==200:
         print('Yes')
     else:
        print('No')

new_item=my_dictionary['June']=1980

print(my_dictionary.values())'''




#QUESTION 2 SOLUTION

#You have a list of your favourite marvel super heros.
#heros=['spider man','thor','hulk','iron man','captain america']
'''1.Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)'''

heros=['spider man','thor','hulk','iron man','captain america']

# 1. find Length of the list

print(len(heros))

#2.Add 'black panther' at the end of this list

heros.append("black panther")
print(heros)

#3  You realize that you need to add 'black panther' after 'hulk',so remove it from the list first and then add it after 'hulk'

heros.remove('black panther') #
heros.insert(3,'black panther')
print(heros)

#4. Now you don't like thor and hulk because they get angry easily :)
   #So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   #Do that with one line of code.

heros[1:3]=["Doctor Strange"] # the last indices is not considered

print(heros)

#5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
dir(heros)
print(heros)

#Question 3

# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
my_list=[]
max_number=int(input("Enter the max number"))
for i in range(1,max_number):
    if i%2!=0:
      my_list.append(i)
print(my_list)
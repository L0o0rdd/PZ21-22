# storm_1 = ('Lightning')
# Union = ('and')
# storm_2 = ('Thunder')
# print(storm_1 + Union + storm_2)
#
# dog_do = ('woof!',)
# print(dog_do * 3)
#
# a = ()
# print(type(a))
#
# d1 = dict(Ivan="менеджер", Mark="инженер")
# print(d1)
# d2 = {"A1":"123","A2":"456"}
# print(d2)
# a = {'cat':'кошка', 'dog':'собака', 'bird':'птица', 'mouse':'мышь'}
#
# d2 = {"A1":"123","A2":"456"}
# "A1" in d2
# "A3" in d2
# False
#
# nums = {1: 'one', 2:'two', 3:'three'}
# person = {'name':'Tom', 1:[30, 15, 16], 2: 2.34, ('ad', 100): 'no'}
# for i in nums:
#    print(i)
# for i in nums:
#    print(nums[i])

nums = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
print(nums)
for i in range(1):
    del nums[1]
    del nums[2]
    print(nums)

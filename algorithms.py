# def print_1_255():
#     for i in range(1,256):
#         print(i)
# print print_1_255()
#
# # print odd
# def odd():
#     for i in range(1,256):
#         if i % 2 == 1:
#             print i
# print odd()

#sum
# def sum():
#     sum = 0
#     for i in range(0,256):
#         sum +=i
#         print i, sum
# print sum()

#print Array Values
# def iterate_array(list):
#     for i in list:
#         print i
# print iterate_array([3,6,7,8])

#print square(List)
def square(list):
    for i in range(len(list)):
        list[i]= list[i]*list[i]
    print list
square([2,3,4])




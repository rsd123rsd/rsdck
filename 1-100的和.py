# for _ in range(10):
#     print('hello')

# def test_return():
#     return 1.1,123
#
#
# x, y = test_return()
# print(x)
# print(y)

# def func(*args):
#     the_max=args[0]
#     the_min=args[0]
#     for i in args:
#         if i > the_max:
#             the_max=i
#         elif i < the_min:
#             the_min=i
#     return {'max':the_max,'min':the_min}
# res=func(1,20,3,40,5)
# print(res)

# 函数作为参数传递
# def test_func(compute):
#     result = compute(1,2)
#     print(result)
#
# def compute(x,y):
#     return x+y
# test_func(compute)

result = sum(i for i in range(1,101))
print(result)
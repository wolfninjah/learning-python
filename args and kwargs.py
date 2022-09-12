# def function_name_print(a, b, c):
#     print(a, b, c)
#
#
# function_name_print('Harry', 'Kamlesh', 'Rohan')

def funargs(normal, *args, **kwargs):
    print(type(args))
    print(normal)  # args is converted from list to tuple
    for item in args:
        print(item)
    for key, value in kwargs.items():  # kwargs
        print('\n', key, 'is', value)
        print(f"{key} is a {value}")


kw = {"Harry": 'Monitor', 'Kamlesh': 'Coordinator'}
normal = "Normal"
pro = ['Harry', 'Kamlesh', 'Rohan', 'Programmer']
funargs(normal, *pro, **kw)

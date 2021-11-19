import inspect
def pydoc(module_name):
    mod = __import__(module_name)
    print("All Entries of the module {}  are : {}".format(module_name,dir(mod)))
    print('*-*-*-*-*-*-*-Description-*-*-*-*-*-*-*')
    print(mod.__doc__)
    print('*-*-*-*-*-*-*-Functions-*-*-*-*-*-*-*')
    for i in inspect.getmembers(mod,lambda x:inspect.isfunction(x)):
        print(i)

mod_name = input("Enter module name :")
pydoc(mod_name)

from models import my_string

print(my_string)

    # def do_all(self, arg):
    #     """Prints all string representation of all instances"""
    #     args = arg.split()
    #     objs = storage.all()
    #     if not args:
    #         print([str(obj) for obj in objs.values()])
    #     else:
    #         class_name = args[0]
    #         if class_name in classes:
    #             for key, obj in objs.items():
    #                 if key.startswith(class_name):
    #                     print(str(obj))
    #         else:
    #             print("** class doesn't exist **")
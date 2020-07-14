def make_pizza(size, *topings):
    print("\nMaking a " + str(size)+
          "-inch pizza with the following toppings:")
    for topping in topings:
        print("- " + topping)

    


## 首先要穿件一个列表，其中包含一些需要打印的设计
#unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
#completed_models = []
#
## 模拟打印每个设计， 直到没有未打印的设计为止
## 打印每个设计后，都将其移动到列表 completed_models
#while unprinted_designs:
#    current_desing = unprinted_designs.pop()
#
#    # 模拟根据设计制作3D打印模型的过程
#    print("Printing model: " + current_desing)
#    completed_models.append(current_desing)
#
## 显示打印好的模型
#print("\nThe following models have been printed:")
#for completed_model in completed_models:
#    print(completed_model)

#def greet_users(names):
#    for name in names:
#        msg = "Hello, " + name.title() + "!"
#        print(msg)
#
#usernames= ['hannah', 'typ', 'margot']
#greet_users(usernames)


#def get_formatted_name(first_name, last_name):
#    full_name = first_name + ' ' + last_name
#    return full_name.title()
#
#while True:
#    print("\nPlease tell me name: ")
#    print("(enter 'q' at any time to quit)")
#    f_name = input("First name: ")
#    if f_name == 'q':
#        break
#    l_name = input("Last name: ")
#    if l_name == 'q':
#        break
#    formatted_name = get_formatted_name(f_name, l_name)
#    print("\nHello, " + formatted_name + "!")

#def bulid_person(first_name, last_name, age=''):
#    person = {'first': first_name, 'last': last_name}
#    if age:
#        person['age'] = age
#    return person
#
#musician = bulid_person('jimi', 'hendrix', age=88)
#print(musician)
#

#def get_formatted_name(first_name, last_name, middle_name=''):
#    if middle_name:
#        full_name = first_name + ' ' + middle_name + ' ' + last_name
#    else:
#        full_name = first_name + " " + last_name
#    return full_name.title()
#musician = get_formatted_name('jimi', 'hendrix')
#print(musician)
#musician = get_formatted_name('jimi', 'hooker', "lee")
#print(musician)
#

#def describe_pet(animal_type, pet_name):
#    """显示宠物名称"""
#    print("\nI have a " + animal_type + ".")
#    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#
##describe_pet("hamster", "harry")
#describe_pet()
#count = list(range(1,8))
#print(count)
#print(count[1:4])

#name = "Ling Qiao"
#message = "Hello" + " " + name.lower(), "would you liek to learn  some Python today"
#print(message)

name = input("enter your name:")
city = input("enter city name:")
print("{} is from {}".format(name, city))

change_name = input("Do you want to update your name, yes/no:")
change_city = input("Do you want to update city name, yes/no:")
# print(change_name)

if (change_name == "yes") and (change_city == "yes"):
    replace_name = name.replace(name, input("Enter your correct name:"))
    replace_city = city.replace(city, input("Enter your correct city name:"))
    # print("{} is from {}".format(replace_name,replace_city))
    name = replace_name
    city = replace_city

elif change_city == "yes":
    input = input("Enter your correct city name:")
    replace_city = city.replace(city, input)
    # print("{} is from {}".format(name,replace_city))
    replace_name = name
    city = replace_city

elif change_name == "yes":
    input = input("Enter your correct name:")
    replace_name = name.replace(name, input)
    # print("{} is from {}".format(replace_name,city))
    name = replace_name
    replace_city = city

else:
    print(f"Thank you {name} for using our services")
    exit()

print("name:{} city:{}".format(replace_name, replace_city))

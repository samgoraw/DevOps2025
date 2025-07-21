my_dict={"name": "Sam Gourav","age":"35","city":"Mumbai"}
print(my_dict)
print("Name: ",my_dict["name"])
my_dict['manager']="test manager"
# for loop
for key in list(my_dict):
    print(key, ": ",my_dict[key])
    my_dict.pop('age')
    print(my_dict)
    my_dict.popitem() #remove last item
    print(my_dict)
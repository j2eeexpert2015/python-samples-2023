def reverse_string(input):
    string_length = len(input)
    for count in range(string_length -1 ,-1,-1):
        print(input[count],end="")

def print_consecutive_letters(input):
    str_length = len(input)
    for i in range(str_length-1):
        if input[i]==input[i+1]:
            print(input[i])
            i = i+1
def print_letters_occurences(input):
    str_length = len(input)
    for i in range(str_length-1):
        if input[i]==input[i+1]:
            print(input[i])
            i = i+1

def print_common_items(list1,list2):
    for item in list1:
        if item in list2:
            print(item,end=" ")

def print_consecutive_item_v2():
    list =[1,1,2,2,3,1,1]
    dict={}
    value=None
    list_size = len(list)
    for i in range(0,list_size):
        item =list[i]
        if item in dict.keys():
            value = dict.get(item)+1
        else:
            value = 1
        dict.update({item:value})
        print(dict)
    for key,value in dict.items():
        if value > 1:
            print(key)
#reverse_string("12345678")
#print_consecutive_letters("aabbcdefgg")
list1 = [1,2,3,4,5]
list2 = [5,6,3,1]
#print_common_items(list1,list2)
print_consecutive_item_v2()




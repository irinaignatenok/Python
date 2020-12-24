
def count_obj(obj,l):
    count = 0
    for elem in l:
        if elem == obj:
            count += 1
    return count


def replace_letter(string, letter, letter_to_replace):
    new_string = ""
    for l in string:
        if l == letter_to_replace:
            new_string += letter
        else:
            new_string += l
    return new_string
# if __name__ ==
# print("Name of the first.py is:", __name__)
replaced = replace_letter("Hello world", "x", "o")
print("Hello world", replaced)

l = ["red", "red", "black", "white"]
red_in_l = count_obj("red", l)

print(f"red is in {l}: {red_in_l} times")

print("Name of the seconda.py is:", __name__)

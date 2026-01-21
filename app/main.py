def get_human_age(cat_age: int, dog_age: int) -> list:
    rules_cat  = [15, 9 , 4]
    rules_dog  = [15, 9 , 5]

    cat_human_age = 0
    cat = cat_age

    for r in rules_cat[:2]:
        if cat >= r:
            cat -= r
            cat_human_age += 1

    if cat >= rules_cat[2]:
        cat_human_age += cat // rules_cat[2]

    dog_human_age = 0
    dog = dog_age

    for r in rules_dog[:2]:
        if dog >= r:
            dog -= r
            dog_human_age += 1

    if dog >= rules_dog[2]:
        dog_human_age += dog // rules_dog[2]

    return [cat_human_age, dog_human_age]

print(get_human_age(0, 0))      # [0, 0]
print(get_human_age(14, 14))    # [0, 0]
print(get_human_age(15, 15))    # [1, 1]
print(get_human_age(23, 23))    # [1, 1]
print(get_human_age(24, 24))    # [2, 2]
print(get_human_age(28, 28))    # [3, 2]
print(get_human_age(100, 100))  # [21, 17]

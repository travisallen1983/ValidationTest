import random

list_one = []
list_two = []
list_three = []
list_four = []
list_five = []
list_six = []


def random_numbers(list_name):
    for i in range(0, 11):
        list_name.append(random.randint(0, 10))


def validated_columns(validatee_column, validator_column):
    validated_list = []
    validatee_list = []
    validator_list = []

    for column_value in validatee_column:
        validatee_list.append(column_value)

    for column_value in validator_column:
        validator_list.append(column_value)

    for i in range(0, len(validatee_list)):
        difference = validatee_list[i] - validator_list[i]
        validated_list.append("Difference of " + str(difference))

    return validated_list


def main():

    random_numbers(list_one)
    random_numbers(list_two)
    random_numbers(list_three)
    random_numbers(list_four)
    random_numbers(list_five)
    random_numbers(list_six)
    validated_list_1 = validated_columns(list_one, list_two)
    validated_list_2 = validated_columns(list_three, list_four)
    validated_list_3 = validated_columns(list_five, list_six)
    validated_list_4 = validated_columns(list_one, list_five)
    validated_list_5 = validated_columns(list_three, list_two)
    validated_list_6 = validated_columns(list_six, list_four)
    validated_df = [["List1:"] + validated_list_1, ["List2:"] + validated_list_2,
                    ["List3:"] + validated_list_3, ["List4:"] + validated_list_4,
                    ["List5:"] + validated_list_5, ["List6:"] + validated_list_6]
    for list in validated_df:
        print(list)

if __name__ == "__main__":
    main()

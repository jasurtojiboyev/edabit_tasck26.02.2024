def is_in_order_custom(input_string):
    for i in range(len(input_string) - 1):
        if input_string[i] > input_string[i + 1]:
            return False
    return True

input_str = "123"
result = is_in_order_custom(input_str)
print(result)
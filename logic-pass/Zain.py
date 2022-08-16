# Task 1
def task1(text):
    for i in text:
        text = text.replace(i, "")
    return text


Your_Input = input("Enter Your Text: ")
print("Results " + task1(Your_Input))


# Task 2
def task2(number1, number2):
    prime_Numbers = []
    for i in range(number1, number2):
        if i % 2 != 0:
            prime_Numbers.append(i)
    return prime_Numbers


Your_Number1 = int(input("Enter First Number: "))
Your_Number2 = int(input("Enter Last Number: "))
print("The List of Prime Numbers is : ", *task2(Your_Number1, Your_Number2))


# Task 3
def task3(text, character):
    count = 0
    for i in text:
        if i == character:
            count += 1
    return count


Your_Text = input("Enter Your Text: ")
Your_Character = input("Enter The character: ")
print("count of your character in your text is : ", task3(Your_Text, Your_Character))

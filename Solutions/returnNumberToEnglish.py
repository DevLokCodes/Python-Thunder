#
'''
    Problem task: Write a function that accepts a positive integer between 0 and 999 inclusive and returns a string representation of that integer written in English.
    Problem Link: https://edabit.com/challenge/mZqMnS3FsL2MPyFMg
'''


def NumToEnglish(num):
    num = str(num)
    if len(num) == 2:
        num = "0" + num

    resulted_string = ""
    initial_dict = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
                    9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
                    16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty",
                    40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety", 100: "hundred"}

    if int(num) in initial_dict.keys():
        return initial_dict.get(int(num))
    else:
        length_of_number = len(num)
        for i in range(length_of_number):

            if i == 0 and int(num[i]) > 0:
                resulted_string = str(initial_dict.get(int(num[i]))) + " " + str(initial_dict.get(100))
            elif i == 1 and int(num[1]) == 1:
                resulted_string = resulted_string + " " + str(initial_dict.get(int(num[1:3])))
            elif i == 1 and int(num[1]) > 1:
                resulted_string = resulted_string + " " + str(initial_dict.get(int(num[1]) * 10))
            elif i == 2 and int(num[1]) != 1 and int(num[i]) > 0:
                print(num[1])
                resulted_string = resulted_string + " " + str(initial_dict.get(int(num[i])))

    return resulted_string.strip()


def FormattingNumber(num):
    if len(num) == 2:
        num = "0" + num
    return num


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        Num = int(input())
        print(NumToEnglish(Num))

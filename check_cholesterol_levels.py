# By Kami Bigdely
# Decompose conditional
# Reference: https://www.healthline.com/health/high-cholesterol/levels-by-age

# Blood test analysis program
total_cholostrol = 70
ldl = 30
triglyceride = 120


def less_than_everything():
    if total_cholostrol < 200 and ldl < 100 and triglyceride < 150:
        return True
    else:
        return False


def average():
    if 200 < total_cholostrol > 240 or ldl > 160 or triglyceride >= 200:
        return True
    else:
        return False


def greater_than_everything():
    if 200 < total_cholostrol < 240 or 130 < ldl < 160 or 150 <= triglyceride < 200:
        return True
    else:
        return False


def print_greater():
    print('*** Borderline to moderately elevated ***')
    print("Start TLC diet")
    print("Under this meal plan, only 7 percent of your daily calories \nshould come from saturated fat.")
    print('Some foods help your digestive tract absorb less cholesterol. For example,\nyour doctor may encourage you to eat more:')
    print('oats, barley, and other whole grains.')
    print('fruits such as apples, pears, bananas, and oranges.')


def print_average():
    print('*** High cholestrol level ***')
    print('start taking pills such as statins')
    print('start TLC diet')


if less_than_everything():
    # good level
    print('*** Good level of cholestrol ***')
elif average():
    # High cholestrol level
    print_average()
elif greater_than_everything():
    # TLC_diet
    print_greater()
else:
    print('Error: unhandled case.')

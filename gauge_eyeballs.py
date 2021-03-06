# By Kami Bigdely
# Introduce explaining variable (alias extract variable)
# Reference: https://www.researchgate.net/publication/305768969_The_role_of_eye_characteristics_in_facial_beauty_likability_and_attractiveness
import math

# Background: You are a computer engineer trying to sift through many profiles to find your soulmate. Unfortunately, there are too many profiles and it's getting tedious. You write a python script to scrape profiles info (such as height, age, etc) and images (for image processing) to figure out automatically who is attractive to you.

# Here is a part of the script:
# assuming you have extracted the following info from the profile's image.

eye_size = 0.47    # [cm^2]
eye_width = 24.2   # [mm]
eye_height = 23.7  # [mm]

iris_width = 20.2  # [mm]
iris_height = 19.7  # [mm]


def right_eye_size():
    if eye_size > 0.45:
        return True
    else:
        return False


def other_right_eye_size():
    if eye_height/eye_width >= 0.59:
        return True
    else:
        return False


def right_iris_size():
    if (math.pi*iris_width/2*iris_height/2) / eye_size >= 0.69:
        return True
    else:
        return False


if right_eye_size() and right_iris_size() and other_right_eye_size():
    print("I’m sorry I wasn’t part of your past, can I make it up by being in your future?")

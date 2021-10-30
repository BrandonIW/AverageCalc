import re
from time import sleep
import termcolor
import pyfiglet

def calc_avg(votes,percent_1,percent_2,percent_3,percent_4,percent_5):
    votes = int(votes)
    one,two,three,four,five = (int(percent_1)*0.01)*votes, ((int(percent_2) * 0.01) * votes) * 2, \
                              ((int(percent_3) * 0.01) * votes) * 3, \
                              ((int(percent_4) * 0.01) * votes) * 4, \
                              ((int(percent_5) * 0.01) * votes) * 5

    return sum([one,two,three,four,five])/votes


def main():
    ascii = pyfiglet.figlet_format("Average Score Calculator", font="standard")
    print(termcolor.colored(ascii, color='green'))
    sleep(1)


    regex = re.compile(r'(\d){1,}')
    while True:
        num_votes = input("Input total number of votes: ")
        percent_1 = input("Input percentage for Not Creepy: ")
        percent_2 = input("Input percentage for Somewhat not Creepy: ")
        percent_3 = input("Input percentage for Neutral: ")
        percent_4 = input("Input percentage for Somewhat Creepy: ")
        percent_5 = input("Input percentage for Very Creepy: ")

        if regex.fullmatch(num_votes) and regex.fullmatch(percent_1) and regex.fullmatch(percent_2) and \
                regex.fullmatch(percent_3) and regex.fullmatch(percent_4) and regex.fullmatch(percent_5):

            return f"Average Score is: {calc_avg(num_votes,percent_1,percent_2,percent_3,percent_4,percent_5)}"

        print("Must enter numbers, dumbass...")
        sleep(1)


if __name__ == '__main__':
    print(main())
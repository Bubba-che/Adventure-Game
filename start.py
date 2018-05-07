from time import sleep

from columns.d import six
from death import dead
from prompt import prompt

 
def newGame():

    

    print(
        """

        THIS IS GOING TO BE A TITLE SCREEN

        """)

    string1 = """
    You find yourself at the entrance of an old home.
    The walls and windows are faded and dilapidated.

    A sign reads:
    """

    string2 = """
    \n
    \t‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡
    \t‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡
    \t‡‡‡‡                 ‡‡‡‡
    \t‡‡‡‡    Fuck you.    ‡‡‡‡
    \t‡‡‡‡                 ‡‡‡‡
    \t‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡
    \t‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡
    \t          ‡‡‡‡‡
    \t          ‡‡‡‡‡
    \t          ‡‡‡‡‡
    \t          ‡‡‡‡‡
    \n
    """

    for i in range(0, len(string1)):
        print(string1[i], end='', flush=True)
        #sleep(.01)
    
    sleep(2)

    for i in range(0, len(string2)):
        print(string2[i], end='', flush=True)
        #sleep(.01)

    string3 = "Do you enter?\n\n"

    for i in range(0, len(string3)):
        print(string3[i], end='', flush=True)
        #sleep(.04)

    while True:
        answer = prompt('feedback')

        yes = ['Yeah', 'yeah', 'Yes', 'yes', 'Ye', 'ye', 'Yup', 'yup', 'Ya', 'ya', 'Y', 'y']
        no = ['No', 'no', 'Nope', 'nope', 'Nah', 'nah', 'N', 'n']

        if answer in yes:
            six.enter()  #  Room D6
        elif answer in no:
            dead("\nYou run away like a little bitch.")
        else:
            print("\n    What?\n")
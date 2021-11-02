# Import necessary modules
import os, platform, time

# Factors to change
crawl_time_interval = 0.5
legs = ['/_/       /_/', '|_|       |_|', '\\_\\       \\_\\']

def body_neutral():
    """
    Prints an neutral terrapin body.
    """
    print('   ________')
    print('  /        \\')
    print(' /          \\---____')
    print('/____________\\__0_/')
    print(legs[1])


def body_happy():
    """
    Prints an angry terrapin body.
    """
    print('   ________')
    print('  /        \\')
    print(' /          \\---____')
    print('/____________\\__^_/')

def body_angry():
    """
    Prints an angry terrapin body.
    """
    print('   ________')
    print('  /        \\')
    print(' /          \\---^___')
    print('/____________\\__X_/')
    print(legs[1])


def os_compatability():
    """
    Checks which os the system is using and adjusts the clear screen function based on it.
    """
    if platform.system() == 'Windows':
        return os.system('cls')
    elif platform.system() in ('Darwin', 'Linux'):
        return os.system('clear')
    else:
        print('WTF?')

def motion():
    """
    Controls the motion of the terrapin based on user's input.
    """
    bool = input('Could you feed me some pellets? (yes/no)')
    if bool == 'yes':
        print('Thank you!')
        # Creates a happy terrapin which walks.
        body_happy()
        try:
            while bool == 'yes':
                for i in legs:
                    os_compatability()
                    body_happy()
                    print(i)
                    time.sleep(crawl_time_interval)
        except KeyboardInterrupt:
            print('I will rest for now. Goodbye! <3')

    elif bool == 'no':
        # Creates a disappointed terrapin.
        body_angry()
        time.sleep(1)
        print('You have disappointed me. Goodbye.')

    else:
        # Creates an angry terrapin.
        print('!!!!!!!!!!!!!!!!!!!!!!!!!')
        body_angry()
        time.sleep(1)
        print("You have failed to even type a proper response. I don't need your pellets. Goodbye!")

def main():
    """
    Runs the program.
    """
    body_neutral()
    time.sleep(1)
    print('Hello there! I am a little hungry.')
    time.sleep(1)
    print('I will perform some tricks if you feed me.')
    time.sleep(1)
    motion()

# Runs the main function
if __name__=='__main__':
    main()
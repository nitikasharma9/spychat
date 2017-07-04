from spydetails import spy, Spy, ChatMessage, friends
from steganography.steganography import Steganography
from datetime import datetime
from termcolor import colored

#older status messages
status_messages = ['Just install this amazing app', 'Searching for a new clue', 'Working without any fear' ,'Emotionally strong']
special=['sos', 'SOS', 'save', 'SAVE', 'help' , 'HELP' ]
#starting an app with a message
print "<----- Hello! What's up . Let's just start ----->"

#ask for an old user or create a new one
question = "Do you want to continue as " + colored(spy.salutation,'blue') + " " + colored(spy.name,'blue') + " (Y/N)? "
existing = raw_input(question)


def add_status():

    updated_status_message = None
    if spy.current_status_message != None:
        print 'Your current status message is %s : \n' %(spy.current_status_message)
    else:
        print colored('No status message currently','red')

    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set? ")


        if len(new_status_message) > 0:
            status_messages.append(new_status_message)
            updated_status_message = new_status_message
    elif default.upper() == 'Y':

        item_position = 1

        for message in status_messages:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages "))


        if len(status_messages) >= message_selection:
            updated_status_message = status_messages[message_selection - 1]
    else:
        print colored('The option you chose is not valid! Press either y or n.','red')

    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print 'No status is updated'

    return updated_status_message

def add_friend():

    new_friend = Spy('','',0,0.0)
    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")
    new_friend.name = new_friend.salutation + " " + new_friend.name
    new_friend.age = raw_input("Age?")
    new_friend.age = int(new_friend.age)
    new_friend.rating = raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 18 and new_friend.rating >= 3:
        friends.append(new_friend)
        print colored('Friend Added!','green')
    else:
        print colored('Sorry! entry is not valid. Spy with this detail cannot be added','red')

    return len(friends)

def select_a_friend():
    item_number = 0

    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number +1, friend.salutation, friend.name,friend.age, friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends")
    friend_choice_position = int(friend_choice) - 1
    return friend_choice_position

def send_message():

    friend_choice = select_a_friend()

    original_image = raw_input("What is the name of the image?")
    output_path = "output.jpg"
    text = raw_input("What do you want to say? ")
    Steganography.encode(original_image, output_path, text)

    new_chat = ChatMessage(text,True)
    friends[friend_choice].chats.append(new_chat)
    print colored("Your secret message image is ready to go!",'green')


def read_message():

    sender = select_a_friend()
    output_path = raw_input("What is the name of the file?")
    secret_text = Steganography.decode(output_path)
    new_chat = ChatMessage(secret_text,False)
    friends[sender].chats.append(new_chat)
    print colored("Your secret message has been saved!",'green')

def read_chat_history():

    read_for = select_a_friend()
    print '\n'

    for chat in friends[read_for].chats:
        time = chat.time.strftime("%d %B %Y")
        if chat.sent_by_me:
            print '[%s] %s: %s' % (time, 'You said:', chat.message)
        else:
            print '[%s] %s said: %s' % (time, friends[read_for].name, chat.message)


def start_chat(spy):
    spy.name = spy.salutation + " " + spy.name

    if spy.age > 18 and spy.age < 50:
        print colored("Authentication complete. Welcome ",'green') + colored(spy.name,'blue') + colored(" of age ",'green') \
              + colored(str(spy.age),'blue') + colored(" and rating of ",'green') + colored(str(spy.rating),'blue') + colored("  Welcome Onboard .",'green')\

        show_menu = True

        while show_menu:
            menu_choices = "What do you want to do . choose option? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    spy.current_status_message = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print colored('You have %d friends','blue') % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                else:
                    show_menu = False
    else:
        print colored('Sorry you are not of the correct age to be a spy','red')

if existing == "Y":
    start_chat(spy)
else:
    spy = Spy('','',0,0.0)
    spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: " )

    if len(spy.name) > 0:
        spy.salutation = raw_input("Should I call you Mr. or Ms.?:" )
        spy.age = raw_input("What is your age?")
        spy.age = int(spy.age)
        spy.rating = raw_input("What is your spy rating?")
        spy.rating = float(spy.rating)
        start_chat(spy)
    else:
        print colored('Please add a valid spy name','red')

from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('Nitika', 'Ms.', 20, 4.7)

friend_one = Spy('Chetan', 'Mr.', 25 , 4.1)
friend_two = Spy('Sakshi', 'Ms.', 19, 3.6)
friend_three = Spy('Mukesh', 'Mr.', 20, 4.95)
friend_four = Spy('Vaishali','Ms.',22, 4.99)


friends = [friend_one, friend_two, friend_three, friend_four]



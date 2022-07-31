
'''
Create a simple SocialNetwork object. You can post, add friends (that may be other Person objects), 
delete friends, and so on. What about even creating a Post objects so that you and other people can like and comment.

do i need to know graph theory for this? # probs not

what i need to do:

- Person class
 -> name - generate this from a list of names ✓
 -> age - generate this randomly ✓
 -> birthday - generate this randomly ✓
 -> username - how will i do this?
 -> profile-picture x
 -> account is private or public
 -> like post - should i connect this to the post class?
 -> comment on post - should i connect this to the post class?
 -> share post - should i connect this to the post class?

Have multiple social network apps (?)
 - features of the social network
  -> check if person has an account -> put it into a list ✓
  -> friends and friends list ✓
  -> posts
  -> send friend request ✓
  -> delete friends

Post class
  -> like and comment on the posts
  -> share
  -> picture, text, or video
'''

import random
from name import name_list

class Person():

  '''
    This is meant to represent just a regular person
  '''

  def __init__(self, name:str=None, age:int=None, birthday:int=None):

    self.name = name
    self.age = age
    self.birthday = birthday
    self.friend_list = []
    self.friend_request_inbox = [] # this is where the friend requests will be staying in

    if name == None:
      self.name = random.choice(name_list)

    if age == None:
      self.age = random.randint(1, 101)
  
  def __str__(self):
    return f"I am {self.name} and I am {self.age} years old."

class Post():

  def __init__(self, type_of_post:str):
    self.type_of_post = type_of_post

class SocialNetwork():

  accounts = [] # this is where the database will store the created accounts

  def __init__(self, name:str):
    self.name = name

  def create_account(self, user:Person):
    self.accounts.append(user)
    print(f"An account for {user.name} has been created!")

  def has_account(self, user:Person):
    if user not in self.accounts:
      print(f"{user.name} does not have an account!")
      return False
    print(f"{user.name} has an account!")
    return True

  def all_accounts(self):
    for account in self.accounts:
      print(account.name)

  def friend_list(self, user:Person): # shows the friend list of the user
    print(f"Here are your ({user.name}) friends:")
    for friend in user.friend_list:
      print(f" -{friend.name} #{user.friend_list.index(friend) + 1}")

  def delete_friend(self, user:Person):
    self.friend_list(user)
    user_index = int(input("Input the index of the person you'd remove as a friend: "))
    del user.friend_list[user_index - 1]
    return    

  def send_friend_request(self, user1:Person, user2:Person):
    # check if both users have an account
    if not self.has_account(user1) or not self.has_account(user2):
      print("No account detected for a user.")
      return False
    return user2.friend_request_inbox.append(user1) # this appends to the inbox of user2 the friend request of user1

  def show_friend_requests(self, user:Person):
    print(f"You currently have {len(user.friend_request_inbox)} friend requests.\nThey are:")
    for friend_request in user.friend_request_inbox:
      print(f" - {friend_request.name} #{user.friend_request_inbox.index(friend_request) + 1}")
    return

  def accept_friend_request(self, user:Person):
    self.show_friend_requests(user)
    user_index = int(input("Who would you accept their friend request?"))
    user.friend_request_inbox[user_index - 1].friend_list.append(user) # this adds the user who gave the friend request to the friend list of the user
    user.friend_list.append(user.friend_request_inbox[user_index - 1]) # this adds the user to the friend list of the user who gave the friend request
    del user.friend_request_inbox[user_index - 1]
    return

  def delete_friend_request(self, user:Person):
    self.show_friend_requests(user)
    user_index = int(input("Input the index of the person you'd remove the friend request of: "))
    del user.friend_request_inbox[user_index - 1]
    return
  
  def __str__(self):
    return f"We are {self.name} and we currently have {len(self.accounts)} user(s)!"

print("Testing")
print("=================================================================")

MukhaLibro = SocialNetwork("MukhaLibro")

person1 = Person()
person2 = Person()
person3 = Person()
person4 = Person()

MukhaLibro.create_account(person1)
print(MukhaLibro)
MukhaLibro.has_account(person1)
MukhaLibro.has_account(person2)
MukhaLibro.create_account(person2)
MukhaLibro.create_account(person3)
MukhaLibro.create_account(person4)

print(MukhaLibro)

MukhaLibro.all_accounts()
MukhaLibro.send_friend_request(person1, person2)
MukhaLibro.send_friend_request(person3, person2)
MukhaLibro.send_friend_request(person4, person2)
MukhaLibro.has_account(person4)
MukhaLibro.accept_friend_request(person2)
MukhaLibro.show_friend_requests(person2)
MukhaLibro.accept_friend_request(person2)
MukhaLibro.friend_list(person2)
MukhaLibro.friend_list(person1)
MukhaLibro.delete_friend(person2)
MukhaLibro.friend_list(person2)

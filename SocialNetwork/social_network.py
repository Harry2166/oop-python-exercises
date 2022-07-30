
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
  -> friends and friends list
  -> posts
  -> send friend request
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
      return
    print(f"{user.name} has an account!")

  def all_accounts(self):
    for account in self.accounts:
      print(account.name)
  
  def __str__(self):
    return f"We are {self.name} and we currently have {len(self.accounts)} user(s)!"

print("Testing")
print("=================================================================")

MukhaLibro = SocialNetwork("MukhaLibro")

person1 = Person()
person2 = Person()
MukhaLibro.create_account(person1)
print(MukhaLibro)
MukhaLibro.has_account(person1)
MukhaLibro.has_account(person2)
MukhaLibro.create_account(person2)
print(MukhaLibro)
MukhaLibro.all_accounts()

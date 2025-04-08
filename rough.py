from oops_project import chatbook

user1 = chatbook()
print(user1.id)

'''user2 = chatbook()
print(user2.id)

user3 = chatbook()
print(user3.id)'''

# Using Static Method directly from class rather than object
chatbook.set_id(10)
user2 = chatbook()
print(user2.id)

user3 = chatbook()
print(user3.id)

#user1.menu()

print(user1.get_name())

user1.set_name("Aniket")

print(user1.get_name())
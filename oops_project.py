class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.logged_in = False
        self.menu()


    def menu(self):
        user_input = input("""Welcome to chatbook! How would you like to proceed?
                           1.Press 1 to Sign Up
                           2.Press 2 to Sign In
                           3.press 3 to write a post
                           4.press 4 to messsage a friend
                           5.press any other key to exit 
                           """)
        
        if user_input == "1":
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        elif user_input == "5":
            pass
        else:
            exit()

object = chatbook()
class chatbook:

    __user_id = 0

    def __init__(self):
        self.id = chatbook.__user_id
        chatbook.__user_id += 1
        self.__name = "Default"
        self.username = ""
        self.password = ""
        self.logged_in = False
        
        #self.menu() 

    @staticmethod
    def get_user_id():
        return chatbook.__user_id
    
    @staticmethod
    def set_id(value):
        chatbook.__user_id = value

    def get_name(self):
        return self.__name
    
    def set_name(self, value):
        self.__name = value



    def menu(self):
        user_input = input("""Welcome to chatbook! How would you like to proceed?
                           1.Press 1 to Sign Up
                           2.Press 2 to Sign In
                           3.press 3 to write a post
                           4.press 4 to messsage a friend
                           5.press any other key to exit 
                           """)
        
        if user_input == "1":
            self.signup()

        elif user_input == "2":
            self.signin()

        elif user_input == "3":
            self.my_posts()

        elif user_input == "4":
            self.send_msg()

        else:
            exit()
        

    def signup(self):
        email  = input("Enter Your Email:")
        password = input("Enter Your Password:")

        self.username = email
        self.password = password
        print("You have successfully signed up!")
        print("\n")

        self.menu()

    def signin(self):
        if self.username =="" and self.password =="":
            print("Please sign up first")
        else:
            u_name = input("Enter Your Email:")
            pwd  = input("Enter Your Password:")

            if u_name == self.username and pwd == self.password:
                print("You have successfully signed in!")
                self.logged_in = True
            else:
                print("Invalid credentials, please try again")
            print("\n")
        self.menu()

    def my_posts(self):
        if self.logged_in == True:
            print("Post Your thoughts here")
        else:
            print("Please sign in first")
        print("\n")
        self.menu()

    def send_msg(self):
        if self.logged_in == True:
            text = input("Enter your message:")
            friend = input("Enter Your Friend Name:")
            print(f"Message sent to {friend} successfully")
        else:
            print("Please sign in first")
        print("\n")
        self.menu()

user1 = chatbook()
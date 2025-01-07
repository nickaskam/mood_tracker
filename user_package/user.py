import uuid

class User:
    def __init__(self, f_name, l_name, email):
        self.user_id = str(uuid.uuid4())
        self.first_name = f_name
        self.last_name = l_name
        self.email = email

    def return_user_id(self):
        return self.user_id
    
    def return_user_dict(self):
        return {self.user_id: 
                {
                    "first_name": self.first_name,
                    "last_name": self.last_name,
                    "email": self.email
                }}
    

if __name__ == "__main__":
    user_1 = User("Nick", "A", "nick@a.com")
    
    user1_id = user_1.return_user_id()
    print("User 1 ID:", user1_id)

    user_dict = user_1.return_user_dict()

    print("User 1:", str(user_dict))
    print("User 1 first name:", user_dict[user1_id]["first_name"])
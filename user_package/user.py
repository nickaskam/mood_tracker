import uuid

class User:
    """
    a class for a user that generates a user id and other 
    user variables
    """
    def __init__(self, f_name: str, l_name: str, email: str, goal: str = ""):
        self.user_id = str(uuid.uuid4())
        self.first_name = f_name
        self.last_name = l_name
        self.email = email
        self.goal = goal

    def return_user_id(self) -> str:
        return self.user_id
    
    def return_user_dict(self) -> dict:
        return {self.user_id: 
                {
                    "first_name": self.first_name,
                    "last_name": self.last_name,
                    "email": self.email, 
                    "goal": self.goal
                }}
    

if __name__ == "__main__":
    goal_text = "to improve"
    user_1 = User("Nick", "A", "nick@a.com", goal_text)
    
    user1_id = user_1.return_user_id()
    print("User 1 ID:", user1_id)

    user_dict = user_1.return_user_dict()

    print("User 1:", str(user_dict))
    print("User 1 first name:", user_dict[user1_id]["first_name"])
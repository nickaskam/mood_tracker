import uuid

class User:
    def __init__(self):
        self.user_id = str(uuid.uuid4())

    def return_user_id(self):
        return self.user_id
    

if __name__ == "__main__":
    user_1 = User()
    print("User 1 ID:", user_1.return_user_id())
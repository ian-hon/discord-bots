class User:
    users = {}

    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.coins = 0
        self.exp = 0
        self.tasks = []
        self.completed_tasks = []

    def get_tasks(self):
        if len(self.tasks) <= 0:
            return "You have no tasks!"
        else:
            return "\n".join([f"• {x.wording()}" for x in self.tasks])

    def profile(self):
        return f"""
        **Coins : {self.coins}**
        **Exp   : {self.exp}**
        **Tasks : {len(self.tasks)}**
        """

    def add_task(self, task):
        self.tasks.append(task)

    def update_user_tasks(self):
        if len(self.tasks) <= 0:
            return
        for x in self.tasks.copy():
            if x.completed:
                self.completed_tasks.append(x)
                self.tasks.remove(x)
                self.coins += x.coin_reward
                self.exp += x.exp_reward

    """Static section"""
    @staticmethod
    def update_user_data(user_id, current_username):  # Called everytime a message is sent (not by a bot)
        if user_id in [x.user_id for x in User.users.values()]:
            # Update the user's data (name, etc)
            user = User.users[user_id]
            user.username = current_username
        else:
            # Create new user and append to list
            User.users[user_id] = User(user_id, current_username)

    @staticmethod
    def update_progress(_user, _type, _amount):
        _collection = [x for x in _user.tasks if x.type == _type]
        for x in _collection:
            x.update_progress(_amount)
        _user.update_user_tasks()

    @staticmethod
    def save_data():
        print("Data saved!")

    @staticmethod
    def load_data():
        print("Data loaded!")

    @staticmethod
    def startup():  # Function called on startup
        User.load_data()
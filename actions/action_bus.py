class ActionBus:
    def __init__(self):
        pass

    def publish(self, action):
        print("Action published {0}", action)
        print(action.to_son())

bus = ActionBus()
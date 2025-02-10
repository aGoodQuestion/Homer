class Character:
    def __init__(self, name: str, description: str, alias: str = None):
        self.name = name
        self.alias = alias
        self.description = description
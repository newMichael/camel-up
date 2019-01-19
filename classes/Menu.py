class Menu():
    def __init__(self):
        self.back = False
        self.list = []
        self.callbacks = []
        self.validations = []

    def print_menu(self):
        for i in range(0, len(self.list)):
            print('[', i + 1, '] ', self.list[i])
        if self.back:
            print('[', len(self.list) + 1, '] Back')

    def add_menu_option(self, title, function):
        self.list.append(title)
        self.callbacks.append(function)
    
    def add_menu_options(self, options):
        for title, callback in options.items():
            self.list.append(title)
            self.callbacks.append(callback)

    def set_menu_back(self, has_back: bool):
        self.back = has_back
from .Menu import Menu

class ConsoleMenu():
    def __init__(self):
        self.prompt_complete = False
        self.last_command = ''
        self.menu_chain = []

    def prompt_user(self, prompt: str, menu: Menu):
        self.prompt_complete = False
        while self.prompt_complete == False:
            print(prompt)
            menu.print_menu()
            command = input("Choose an option >>> ")
            self.last_command = command
            self.handle_user_input(command, menu)
        # input is validated, call appropriate function
        menu.callbacks[int(command)- 1]()

    def handle_user_input(self, command, menu):
        input_valid = self.validate_user_input(command, menu)
        if input_valid: 
            self.prompt_complete = True

    def validate_user_input(self, command, menu):
        menu_size = len(menu.list) if menu.back else len(menu.list) + 1
        if not command.isnumeric(): 
            print('\r\nERROR: Not a number\r\n')
            return False
        elif int(command) < 1 or int(command) > menu_size: 
            print('\r\nERROR: Option Out of Range\r\n')
            return False
        else: return True

    
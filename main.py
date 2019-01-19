import sys
from classes.ConsoleMenu import ConsoleMenu
from classes.Menu import Menu
from classes.Game import Game

#console prompt functions
#these should be in their own file probably
def get_main_menu_prompt():
    return "~~~~ CAMEL UP ~~~~"
def get_player_count_prompt():
	return "How many players will be in this game?"
def get_game_intro_dialog(game):
	dialog = "You have started a new game!\r\n"
	dialog += "PLAYERS:\r\n"
	#for player in game.players:
	#	dialog+= player.get_name(), '\r\n'
	dialog += '\r\n A player has been randomly chosen to be the first player!\r\n'
	dialog += 'A player, start your turn...'
	return dialog

#init console and menus
console = ConsoleMenu()
main_menu = Menu()
player_count_menu = Menu()

#menu functions
def kill_script():
	sys.exit("kill_script called... game over.")
def show_player_count_menu():
	console.prompt_user(get_player_count_prompt(), player_count_menu)
def set_player_names():
	player_names = []
	player_count = int(player_count_menu.list[int(console.last_command) - 1])
	for player_number in range(1, player_count + 1):
		print("Enter a player name for Player", player_number)
		player_name = input(">>> ")
		player_names.append(player_name)
	play_game(player_names)
def play_game(player_names):
	game = Game(player_names)
	print(get_game_intro_dialog(game))
	while game.game_over == False:
		game.advance_game()


#add options to menus
main_menu.add_menu_options({
	'Start New Game': show_player_count_menu,
	'How To Play': kill_script
})
player_count_menu.add_menu_options({
	'2': set_player_names,
	'3': set_player_names,
	'4': set_player_names
})

#start console loop
#all the action starts here
console.prompt_user(get_main_menu_prompt(), main_menu)
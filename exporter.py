import sys
import os

def on_script_loaded():
    pass

def on_game_starting(game):
    pass

def on_game_started(game):
    pass

def on_game_stopped(game, elapsed_seconds):
    pass

def on_game_installed(game):
    pass

def on_game_uninstalled(game):
    pass

def menu_function():
    pass

def MultiplayerExport():
	incr = 0
	try:
		with open("Multiplayer_Games.txt", "w") as text_file:
			for game in PlayniteApi.Database.Games:
				str_features = []
				if game.Features:
					for feature in game.Features:
						str_features.append(feature.Name)
					if 'Multiplayer' in str_features:
						incr += 1
						text_file.write("%s\n" % game.Name)
		PlayniteApi.Dialogs.ShowMessage("%d exported in file:\n%s\Multiplayer_Games.txt" % (incr,os.path.abspath(os.getcwd())))
	except Exception as err:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		PlayniteApi.Dialogs.ShowMessage(str("line %s: %s\n%s" %(exc_tb.tb_lineno,game.Name,err)))
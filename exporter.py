import sys
import os


def MultiplayerExport():
    try:
        with open("Multiplayer_Games.csv", "w") as text_file:
            games_list = []
            for game in PlayniteApi.Database.Games:
                str_features = []
                if game.Features:
                    for feature in game.Features:
                        str_features.append(feature.Name)
                        if 'Multiplayer' in str_features:
                            gamename = game.Name.replace('_', ' ').lower()
                            # Don't reinsert if duplicate
                            if bool(gamename) and not any(d['name'] == gamename for d in games_list):
                                games_list.append({'name': gamename, 'activity': game.LastActivity})
            incr = 1
            for game_row in games_list:
                if incr < len(games_list):
                    end_of_file = "\n"
                else:
                    end_of_file = ""
                text_file.write("{0};{1}{2}".format(game_row['name'], game_row['activity'], end_of_file))
                incr += 1
        PlayniteApi.Dialogs.ShowMessage("{0} exported in file:\n{1}\\Multiplayer_Games.csv".format(len(games_list), os.path.abspath(os.getcwd())))
    except Exception as err:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        PlayniteApi.Dialogs.ShowErrorMessage(str("line %s: %s\n%s" % (exc_tb.tb_lineno, game.name, err)), 'Error')


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

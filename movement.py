from talon import Module, actions
from .clipboard import *

module = Module()

@module.capture(rule = '<user.letter>+ <number>')
def google_sheets_cell_location(m) -> str:
    '''A google sheets cell location'''
    location = ''
    for element in m:
        location += str(element)
    return location



@module.action_class
class Actions:
    def google_sheets_toggle_movement_tool():
        '''Activates the google sheets movement tool'''
        actions.key('ctrl-j')
    
    def google_sheets_go_to_cell(cell_location: str):
        '''Moves to the specified cell assuming that the movement tool is not currently active'''
        actions.user.google_sheets_toggle_movement_tool()
        actions.insert(cell_location)
        actions.key('enter')

    def google_sheets_go_to_row(number: int):
        '''Moves to the specified row'''
        actions.user.google_sheets_toggle_movement_tool()
        current_cell: str = get_selected_text_using_clipboard()
        current_column: str = get_column(current_cell)
        actions.insert(current_column + str(number))
        actions.key('enter')


def get_column(current_cell: str) -> str:
    row_start_index: int = 0
    for character in current_cell:
        if character.isdigit():
            break
        row_start_index += 1
    return current_cell[:row_start_index]

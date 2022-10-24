from talon import Module, actions

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



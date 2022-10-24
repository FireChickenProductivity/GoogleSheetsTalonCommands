from talon import Module, actions

module = Module()

@module.capture(rule = 'up|down|left|right')
def google_sheets_direction(m) -> str:
    '''A direction in which to perform a google sheets command'''
    return str(m[0])

selection_sleep_setting = module.setting(
    'google_sheets_selection_delay',
    type = float,
    default = 0.1,
    desc = 'How long to pause google sheets commands when selecting. Try increasing this if commands that use selecting are not working properly.'
)

def wait_selection_delay():
    actions.sleep(selection_sleep_setting.get())

@module.action_class
class Actions:
    def google_sheets_edit_cell():
        '''Starts editing the current cell'''
        actions.key('enter')
    
    def google_sheets_submit_cell_and_move_right():
        '''Submits the contents of the current cell and moves to the right instead of down'''
        actions.key('enter')
        actions.edit.up()
        actions.edit.right()
    
    def google_sheets_copy_amount_in_direction(amount: int, direction: str):
        '''Copies the contents of the current cell the specified number of times in the specified direction'''
        actions.edit.copy()
        wait_selection_delay()
        for i in range(amount):
            extend_selection_in_direction(direction)
        actions.edit.paste()

def extend_selection_in_direction(direction: str):
    if direction == 'up':
        actions.edit.extend_up()
    elif direction == 'down':
        actions.edit.extend_down()
    elif direction == 'left':
        actions.edit.extend_left()
    elif direction == 'right':
        actions.edit.extend_right()
    wait_selection_delay()
from talon import clip, Module, actions, settings

module = Module()
clipboard_sleep_setting_setting_name = 'google_sheets_clipboard_delay'
clipboard_sleep_setting = 'user.' + clipboard_sleep_setting_setting_name
module.setting(
    clipboard_sleep_setting_setting_name,
    type = float,
    default = 0.2,
    desc = 'How long to pause when using the clipboard with google sheets commands. Try increasing this if those commands are not working.'
)

def wait_long_enough_to_let_clipboard_revert_properly():
    actions.sleep(settings.get(clipboard_sleep_setting))

def get_selected_text_using_clipboard() -> str:
    with clip.revert():
        actions.edit.copy()
        wait_long_enough_to_let_clipboard_revert_properly()
        result = clip.text()
    return result

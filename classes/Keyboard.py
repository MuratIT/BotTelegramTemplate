from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


class EditKeyboard:
    @staticmethod
    def edit_item_list(lists: list, counts: int):
        buttons = list()
        for i in range(0, len(lists), counts):
            buttons.append(lists[i:i + counts])
        return buttons

    @staticmethod
    def edit_reply_keyboard_button(lists: list[str]):
        arr = list()
        for item in lists:
            arr.append(KeyboardButton(item))
        return arr

    @staticmethod
    def edit_inline_keyboard_button(lists: list[dict]):
        arr = list()

        for item in lists:
            callback_data = None if item.get('callback_data') is False or item.get('callback_data') is None \
                else item.get('callback_data')

            url = None if item.get('url') is False or item.get('url') is None else item.get('url')

            inline_btn = InlineKeyboardButton(item.get('title'), callback_data=callback_data, url=url)
            arr.append(inline_btn)

        return arr


class ReplyKeyboard(EditKeyboard):
    def __init__(self, row: int = 0):
        self.remove = ReplyKeyboardRemove()
        self.Keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        self.row = row

    def add(self, text_buttons_list: list):
        list_buttons = self.edit_reply_keyboard_button(text_buttons_list)
        if self.row != 0 and self.row != 1:
            list_buttons = self.edit_item_list(list_buttons, self.row)

        for buttons in list_buttons:
            self.Keyboard.row(*buttons)


class InlineKeyboard(EditKeyboard):
    def __init__(self, row=0):
        self.Keyboard = InlineKeyboardMarkup()
        self.row = row

    def add(self, dict_buttons_list: list):
        list_buttons = self.edit_inline_keyboard_button(dict_buttons_list)
        if self.row != 0 and self.row != 1:
            list_buttons = self.edit_item_list(list_buttons, self.row)

        for buttons in list_buttons:
            self.Keyboard.row(*buttons)


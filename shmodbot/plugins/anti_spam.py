# ShModBot - Moderational Telegram Bot tailored to a specific group.
# Copyright (C) 2019  Colin <https://github.com/ColinTheShark>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pyrogram import Message

from ..shmodbot import ShModBot
from ..utils import constants
from ..utils import sql_helper
from ..utils.constants import Filters

SPAM = 0


@ShModBot.on_message(
    Filters.chat(ShModBot.GROUP_ID)
    & (Filters.sticker | Filters.animation)
    & ~Filters.edited
    & ~Filters.admin
)
def anti_spam(bot: ShModBot, message: Message):
    """Zählt die gesendeten Sticker und Animationen im Chat, um bei zu vielen
    hintereinander selbige zu löschen.
    
    Args:
        bot (`ShModBot`): Der Bot selbst
        message (`Message`): Die Nachricht, die die Funktion ausgelöst hat
    """
    global SPAM
    if message.sticker and (
        message.sticker.set_name
        in sql_helper.check_banned_pack(message.sticker.set_name)
    ):
        message.delete()
    else:
        SPAM += 1
        if SPAM > 3:
            if SPAM > 5:
                message.reply_text(**constants.anti_spam())
                SPAM = 0
            message.delete()


@ShModBot.on_message(
    Filters.chat(ShModBot.GROUP_ID)
    & ~Filters.sticker
    & ~Filters.animation
    & ~Filters.edited
)
def reset_anti_spam(bot: ShModBot, message: Message):
    """Setzt den SPAM Zähler zurück, wenn eine Nachricht gesendet wurde, die kein
    Sticker oder eine Animation ist.
    
    Args:
        bot (`ShModBot`): Der Bot selbst
        message (`Message`): Die Nachricht, die die Funktion ausgelöst hat
    """
    global SPAM
    SPAM = 0
    message.continue_propagation()

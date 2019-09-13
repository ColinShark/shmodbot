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

from pyrogram import Filters, Message

from ..shmodbot import ShModBot
from ..utils import constants


@ShModBot.on_message(Filters.command(["help", "hilfe"]) & Filters.private)
def help_private(bot: ShModBot, message: Message):
    """Sends a message containing a helping text.
    
    Parameters:
        bot (`ShModBot`): The bot itself
        message (`Message`): The message triggering the handler
    """
    message.reply_text(**constants.help_private())


@ShModBot.on_message(
    Filters.command(["help", "hilfe"]) & Filters.chat(ShModBot.GROUP_ID)
)
def help_group(bot: ShModBot, message: Message):
    """Replies with a message explaining basic functionality, including an inline
    keyboard.
    
    Parameters:
        bot (`ShModBot`): The bot itself
        message (`Message`): The message triggering the handler
    """
    message.reply_text(**constants.help_group())

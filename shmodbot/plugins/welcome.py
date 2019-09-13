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

from loguru import logger
from pyrogram import Filters, Message, Emoji

from ..shmodbot import ShModBot
from ..utils import constants


@ShModBot.on_message(Filters.chat(ShModBot.GROUP_ID) & Filters.new_chat_members)
def welcome_new_members(bot: ShModBot, message: Message):
    """Greet new users with an animation and a bit of text.
    
    Parameters:
        bot (`ShModBot`): The bot itself
        message (`Message`): The message triggering the handler
    """
    message.reply_animation(**constants.welcome(message.new_chat_members))

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

from time import time, sleep

from pyrogram import ChatPermissions, Message

from ..shmodbot import ShModBot
from ..utils import constants
from ..utils.constants import Filters
from ..utils.interval import IntervalHelper


def timer(message: Message):
    """Interaction with the IntervalHelper modules to transform "7h" or "5d" to UNIX
    timestamps.
    
    Parameters:
        message (`Message`):
            The incoming message which values need to transformed.
    
    Returns:
        int: An UNIX timestamp in the future, or 0
    """
    if len(message.command) > 1:
        secs = IntervalHelper(message.command[1])
        return int(str(time()).split(".")[0]) + secs.to_secs()[0]
    else:
        return 0


@ShModBot.on_message(
    Filters.command("ban") & Filters.chat(ShModBot.GROUP_ID) & Filters.admin
)
def ban(bot: ShModBot, message: Message):
    """Bans a group member.
    
    Parameters:
        bot (`ShModBot`): The bot itself
        message (`Message`): The message triggering the handler
    """
    message.delete()
    try:
        bot.kick_chat_member(
            chat_id=message.chat.id,
            user_id=message.reply_to_message.from_user.id,
            until_date=timer(message),
        )
    except Exception as err:
        bot.send_message(ShModBot.ADMIN_GROUP_ID, f"`{err}`")


@ShModBot.on_message(
    Filters.command("unban") & Filters.chat(ShModBot.GROUP_ID) & Filters.admin
)
def unban(bot: ShModBot, message: Message):
    """Unbans a previously banned member.
    
    Parameters:
        bot (`ShModBot`): The bot itself
        message (`Message`): The message triggering the handler
    """
    try:
        message.delete()
        bot.unban_chat_member(
            chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id
        )
    except Exception as err:
        bot.send_message(ShModBot.ADMIN_GROUP_ID, f"`{err}`")


@ShModBot.on_message(
    Filters.command("mute") & Filters.chat(ShModBot.GROUP_ID) & Filters.admin
)
def mute(bot: ShModBot, message: Message):
    """Mutes a group member.
    
    Parameters:
        bot (`ShModBot`): The bot itself
        message (`Message`): The message triggering the handler
    """
    message.delete()
    try:
        bot.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=message.reply_to_message.from_user.id,
            permissions=ChatPermissions(),
            until_date=timer(message),
        )
    except Exception as err:
        bot.send_message(ShModBot.ADMIN_GROUP_ID, f"`{err}`")


@ShModBot.on_message(
    Filters.command("unmute") & Filters.chat(ShModBot.GROUP_ID) & Filters.admin
)
def unmute(bot: ShModBot, message: Message):
    """Removes a users mute.
    
    Parameters:
        bot (`ShModBot`): The bot itself
        message (`Message`): The message triggering the handler
    """
    message.delete()
    try:
        bot.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=message.reply_to_message.from_user.id,
            permissions=ChatPermissions(
                can_send_messages=True,
                can_send_media_messages=True,
                can_send_other_messages=True,
                can_add_web_page_previews=True,
                can_send_polls=True,
                can_change_info=True,
                can_invite_users=True,
                can_pin_messages=True,
            ),
        )
    except Exception as err:
        bot.send_message(ShModBot.ADMIN_GROUP_ID, f"`{err}`")


@ShModBot.on_message(
    Filters.command("kick") & Filters.chat(ShModBot.GROUP_ID) & Filters.admin
)
def kick(bot: ShModBot, message: Message):
    """Removes a group member from the group by banning and unbanning
    (that's how Telegram works).
    
    Parameters:
        bot (`ShModBot`): The bot itself
        message (`Message`): The message triggering the handler
    """
    message.delete()
    try:
        if message.reply_to_message.from_user.is_self:
            return
        bot.kick_chat_member(
            chat_id=message.chat.id,
            user_id=message.reply_to_message.from_user.id,
            until_date=0,
        )
        sleep(3)
        bot.unban_chat_member(
            chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id
        )
    except Exception as err:
        bot.send_message(ShModBot.ADMIN_GROUP_ID, f"`{err}`")

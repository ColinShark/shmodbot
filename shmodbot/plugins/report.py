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

from pyrogram import Filters, Emoji, Message

from ..shmodbot import ShModBot
from ..utils import constants


@ShModBot.on_message(Filters.command("report", "!"))
def report(bot: ShModBot, message: Message):
    if message.reply_to_message:
        message.reply_to_message.forward(ShModBot.ADMIN_GROUP_ID)
        bot.send_message(chat_id=ShModBot.ADMIN_GROUP_ID, **constants.report(message))

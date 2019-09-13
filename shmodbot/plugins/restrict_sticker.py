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

from sqlite3 import IntegrityError

from pyrogram import Message

from ..shmodbot import ShModBot
from ..utils import constants
from ..utils.constants import Filters
from ..utils import sql_helper


@ShModBot.on_message(
    Filters.command("ban_pack", "!")
    & Filters.chat([ShModBot.GROUP_ID, ShModBot.ADMIN_GROUP_ID])
    & Filters.admin
)
def ban_pack(bot: ShModBot, message: Message):
    message.delete()
    if not message.reply_to_message:
        return
    sql_helper.add_banned_pack(message.reply_to_message.sticker.set_name)


@ShModBot.on_message(
    Filters.command("banned_packs", "!") & Filters.chat(ShModBot.ADMIN_GROUP_ID)
)
def banned_packs(bot: ShModBot, message: Message):
    packs = sql_helper.get_banned_packs()
    message.reply_text(**constants.banned_packs(packs))


@ShModBot.on_message(
    Filters.command("unban_pack", "!")
    & Filters.chat(ShModBot.ADMIN_GROUP_ID)
    & Filters.admin
)
def unban_pack(bot: ShModBot, message: Message):
    message.delete()
    set_name = message.command[1]
    sql_helper.unban_pack(set_name)

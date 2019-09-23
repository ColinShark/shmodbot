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

from configparser import ConfigParser
from pathlib import Path

from loguru import logger
from pyrogram import Client


class ShModBot(Client):
    """The ShModBot class, inherited from Pyrogram's Client"""
    def __init__(self):
        """Initialized the ShModBot Class.
        
        Args:
            Client (Client): Pyrogram's Client class
        """
        name = self.__class__.__name__.lower()
        config_file = f"{name}.ini"

        config = ConfigParser()
        config.read(config_file)

        setattr(ShModBot, "GROUP_ID", int(config.get(name, "group_id")))
        setattr(ShModBot, "ADMIN_GROUP_ID", int(config.get(name, "admin_group_id")))
        setattr(ShModBot, "DATABASE", str(Path(__file__).parent.parent / f"{name}.db"))

        super().__init__(
            session_name=name,
            bot_token=config.get(name, "bot_token"),
            workers=8,
            workdir=".",
            config_file=config_file,
            plugins=dict(root=f"{name}/plugins"),
        )

    def start(self):
        """Starts the bot, sets up the database and saves the invite link."""
        from .utils import sql_helper

        sql_helper.startup()
        super().start()
        username = self.get_me().username
        logger.info(f"Bot started as {username}")

    def stop(self):
        """Stops the bot"""
        super().stop()
        logger.info("Bot stopped")

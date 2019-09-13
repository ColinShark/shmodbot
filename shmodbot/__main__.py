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

from sys import version_info

from loguru import logger

logger.add(
    sink="./logs/shmodbot.log",
    enqueue=True,
    rotation="1 week",
    retention="1 month",
    compression="gz",
    encoding="utf8",
)

if version_info[0] < 3 or version_info[1] < 6:
    logger.error("Python 3.6 or newer is required.")
    quit(1)

if __name__ == "__main__":
    from .shmodbot import ShModBot

    ShModBot().run()

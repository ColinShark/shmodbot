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

import sqlite3
from pathlib import Path

from ..shmodbot import ShModBot


def startup():
    with sqlite3.connect(ShModBot.DATABASE) as db:
        with open(str(Path(__file__).parent / "schema.sql"), "r") as schema:
            db.executescript(schema.read())


def set_invite_link(invite: str):
    with sqlite3.connect(ShModBot.DATABASE) as db:
        db.execute("DELETE FROM invite_link")
        db.execute("INSERT INTO invite_link VALUES (?)", (invite, ))


def get_invite_link() -> str:
    with sqlite3.connect(ShModBot.DATABASE) as db:
        r = db.execute("SELECT invite FROM invite_link")
        return r.fetchone()[0]


def add_banned_pack(set_name: str):
    with sqlite3.connect(ShModBot.DATABASE) as db:
        db.execute("INSERT INTO banned_packs VALUES (?)", (set_name.lower(),))


def get_banned_packs() -> list:
    with sqlite3.connect(ShModBot.DATABASE) as db:
        r = db.execute("SELECT set_name FROM banned_packs ORDER BY set_name")
        banned_packs = [x[0] for x in r]
        return banned_packs


def unban_pack(set_name: str):
    with sqlite3.connect(ShModBot.DATABASE) as db:
        db.execute("DELETE FROM banned_packs WHERE set_name=?", (set_name.lower(), ))


def check_banned_pack(set_name: str):
    with sqlite3.connect(ShModBot.DATABASE) as db:
        r = db.execute(
            "SELECT * FROM banned_packs WHERE set_name=?", (set_name.lower(),)
        )
        return [x[0] for x in r]

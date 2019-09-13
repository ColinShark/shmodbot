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

from pyrogram import Message, Emoji, Filters, InlineKeyboardMarkup, InlineKeyboardButton

from ..shmodbot import ShModBot

class Filters(Filters):
    """Eigene Klasse "Filters", vererbt von Pyrogram's "Filters" Klasse
    
    Args:
        Filters (class): Vererbte Klasse
    """
    admin = Filters.create(
        func=lambda _, msg: bool(
            msg._client.get_chat_member(msg.chat.id, msg.from_user.id).status
            in ("administrator", "creator")
        ),
        name="AdminFilter",
    )
    """Filter, um nur auf Administratoren zu reagieren."""


def start(message: Message, invite: str) -> dict:
    """Zum Formattieren einer Nachricht, wenn man den Bot startet.
    
    Args:
        message (`Message`): Die Nachricht, deren Inhalt zum Formattieren genutzt wird
        invite (`str`): Der aktuelle Einladungslink
    
    Returns:
        dict: Dictionary zum **mapping-formatting der zu sendenen Nachricht.
    """
    start_text = (
        "Hey {} {}\n".format(message.from_user.first_name, Emoji.WAVING_HAND)
        + "Ich bin ein Bot, der im Norden für Ordnung sorgt. Genauer gesagt bei den "
        + "Furs aus Schleswig-Holstein und Hamburg. Vielleicht willst du auch mal vorbeischauen :3"
    )
    start_keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="S-H und HH Furs beitreten", url=invite),
                InlineKeyboardButton(text="Mehr Infos", url="t.me/SHModBot?start=help"),
            ],
            [
                InlineKeyboardButton(
                    text=f"Ich bin Quelloffen {Emoji.OPEN_BOOK}",
                    url="https://github.com/ColinTheShark/shmodbot",
                )
            ],
        ]
    )
    return {"text": start_text, "reply_markup": start_keyboard, "parse_mode": None}


def help_private() -> dict:
    help_text = (
        "Ich bin ein Bot, der in der Gruppe der Furs aus Schleswig-Holstein und Hamburg "
        + "aushelfen soll. Aktuell gibt es hier noch nicht allzu viel Informationen, "
        + "aber die werde ich bestimmt bald haben.\n\n"
        + "Bis dahin bitte etwas Geduld.\n~Danke :3"
    )
    help_keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=f"{Emoji.CARD_INDEX_DIVIDERS} Sourcecode",
                    url="https://github.com/ColinTheShark/shmodbot",
                )
            ]
        ]
    )
    return {"text": help_text, "reply_markup": help_keyboard, "parse_mode": None}


def help_group() -> dict:
    help_text = (
        f"{Emoji.INFORMATION} **Information**\n"
        + "Ich bin ein Bot, um den Admins auszuhelfen. "
        + "Ausführliche Informationen gibt über die Buttons unten."
    )
    help_keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=f"{Emoji.INFORMATION} Ausführlichere Infos",
                    url="https://t.me/ShModBot?start=help",
                ),
                InlineKeyboardButton(
                    text=f"{Emoji.BLUE_BOOK} Quelltext",
                    url="https://github.com/ColinTheShark/shmodbot",
                ),
            ]
        ]
    )
    return {"text": help_text, "reply_markup": help_keyboard, "parse_mode": "markdown"}


def welcome(new_members: list):
    _animation = "CgADAgADdQUAAleAoUs9098bzMbkwBYE"
    _mention = '<a href="tg://user?id={id}">{name}</a>'
    mention = [_mention.format(id=x.id, name=x.first_name) for x in new_members]

    welcome_text = (
        "Herzlich Willkommen {}\n".format(", ".join(mention))
        + "Bitte mach dich mit den Regeln vertraut, bevor du dich beteiligst.\n"
        + "Viel Spaß wünsch' ich dir hier :3"
    )

    welcome_keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Regeln im Chat…", url="https://t.me/c/1116516214/204204"
                ),
                InlineKeyboardButton(
                    text="…und Online",
                    url="http://telegra.ph/S-H-und-HH-Chat-Regeln-und-Infos-04-04",
                ),
            ]
        ]
    )

    return {
        "animation": _animation,
        "caption": welcome_text,
        "reply_markup": welcome_keyboard,
        "parse_mode": "html",
    }


def rules() -> dict:
    rules_text = (
        Emoji.SCROLL
        + " **Regeln**\n"
        + "Wie überall anders gibt es auch hier ein paar Regeln. Kurz und knapp wären das:\n"
        + "◆ Keine 18+ Inhalte\n"
        + "◆ Kein Spam\n"
        + "    ◇ Nachrichten zusammenfassen\n"
        + "    ◇ Kein Ausgiebiges Roleplay\n"
        + "◆ Sei kein Arsch\n"
        + "Eine ausführlichere Übersicht findest du über die Buttons unten."
    )
    rules_keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Regeln im Chat…", url="https://t.me/c/1116516214/204204"
                ),
                InlineKeyboardButton(
                    text="…und Online",
                    url="http://telegra.ph/S-H-und-HH-Chat-Regeln-und-Infos-04-04",
                ),
            ]
        ]
    )
    return {
        "text": rules_text,
        "reply_markup": rules_keyboard,
        "parse_mode": "markdown",
    }


def anti_spam():
    antispam_text = "Zu viele Sticker/GIFs hintereinander. Bitte nicht damit spammen."
    return {"text": antispam_text, "parse_mode": None}


def banned_packs(packs: list):
    pack_text = "**Gesperrte Sticker:**\n"
    for pack in packs:
        pack_text += "[◆](https://t.me/addstickers/{0}) `{0}`\n".format(pack)
    return {"text": pack_text, "parse_mode": "markdown"}


def report(message: Message):
    reporter = '<a href="tg://user?id={id}">{name}</a>'.format(
        id=message.from_user.id, name=message.from_user.first_name
    )
    report_text = f"{Emoji.UP_ARROW} gemeldet von {reporter}"

    chat_id = str(message.chat.id).replace("-100", "")
    msg_link = f"https://t.me/c/{chat_id}/"

    report_keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=f"{Emoji.SPEECH_BALLOON} Nachricht",
                    url=msg_link + str(message.reply_to_message.message_id),
                ),
                InlineKeyboardButton(
                    text=f"{Emoji.WARNING} Meldung",
                    url=msg_link + str(message.message_id),
                ),
            ]
        ]
    )
    return {"text": report_text, "reply_markup": report_keyboard, "parse_mode": "html"}

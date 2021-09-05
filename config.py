"""
VideoPlayerBot, Telegram Video Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
import re
from dotenv import load_dotenv

load_dotenv()

class Config:
    ADMIN = os.environ.get("AUTH_USERS", "965221088")
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    ADMINS.append(1316963576)
    API_ID = int(os.environ.get("API_ID", "1317481"))
    CHAT_ID = int(os.environ.get("CHAT_ID", "-1001569239539"))
    API_HASH = os.environ.get("API_HASH", "e5f7a25123dca9d734516cde8ae4c374")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1982642172:AAFJQrZwaTksjt_Sc6Qsk5sWSFpIoQiAnzI")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "DTO_VideoPlayerBot")
    REPLY_MESSAGE = os.environ.get("REPLY_MESSAGE", "salam")
    if REPLY_MESSAGE:
        REPLY_MESSAGE = REPLY_MESSAGE
    else:
        REPLY_MESSAGE = None
    SESSION_STRING = os.environ.get("SESSION_STRING", "BACP-czJuZcXxhE0J0vCmWDk4Tyoi3fB0WbsTlDBKEPIOtAwhup0-RVfmHJRPNBMS_cRvI1U-1Rt_7zakMrr_hwjtaR4iFRQILctD_ED3UmB74izWqYjvV5gDbXCC2-afWRJV_jwZu2Wc6fMAEug1rM3c8E0cl4Lqa82MZ2nac0PmkcONm2T4Zp3F7zlfiqwvNAJnIhYF19f36_UoLnJiBoUHKyNDtRuUS9jsmW3iKPNS02dARZpIa09V41HvLh8f69MmczGlfDij7qN3wHanEIkZWwjNQ1o77rYJ-4HaePIKUctU2pnqHegHIYFWPHqtzfJUJjiK-rOAomGaHJcVszUY5wLWQA")

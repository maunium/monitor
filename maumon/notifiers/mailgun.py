# maumon - maunium.net monitoring system
# Copyright (C) 2018 Tulir Asokan
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import asyncio
import json
import os

from aiohttp import ClientSession, BasicAuth

targets = os.environ["MAILGUN_TARGETS"]
api_key = os.environ["MAILGUN_API_KEY"]
domain = os.environ["MAILGUN_SENDER_DOMAIN"]
sender = os.environ["MAILGUN_SENDER"]
endpoint = os.environ.get("MAILGUN_ENDPOINT", "api.mailgun.net")
http = ClientSession(loop=asyncio.get_event_loop())


async def send(title: str, body: str) -> None:
    await http.post(f"https://{endpoint}/api/v3/{domain}/messages", data=json.dumps({
        "from": sender,
        "to": targets,
        "subject": title,
        "text": body,
    }), auth=BasicAuth(login="api", password=api_key))

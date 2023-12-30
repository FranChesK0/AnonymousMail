import logging
from abc import ABC

import aiohttp

from models import Email, Message
from misc import Env, LoggerName, get_logger

logger: logging.Logger = get_logger(LoggerName.MAIN)


class Requests(ABC):
    @staticmethod
    async def get_domain_list() -> list[str]:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{Env.API}?action=getDomainList") as response:
                return await response.json()

    @staticmethod
    async def check_mailbox(login: str, domain: str) -> list[Email]:
        url: str = f"{Env.API}?action=getMessages&login={login}&domain={domain}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return [Email.model_validate(email) for email in await response.json()]

    @staticmethod
    async def fetch_single_message(login: str, domain: str, message_id: int) -> Message:
        url: str = f"{Env.API}?action=readMessage&login={login}&domain={domain}&id={message_id}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return Message.model_validate(await response.json())

    @staticmethod
    async def attachment_download(login: str, domain: str, message_id: int, file: str) -> None:
        url: str = f"{Env.API}?action=download&login={login}&domain={domain}&id={message_id}&file={file}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                pass

    @staticmethod
    async def delete_email(login: str, domain: str) -> None:
        data: dict = {
            "action": "deleteMailBox",
            "login": login,
            "domain": domain
        }
        async with aiohttp.ClientSession() as session:
            await session.post(Env.URL, data=data)
        logger.info(f"Email [{login}@{domain}] was deleted.")

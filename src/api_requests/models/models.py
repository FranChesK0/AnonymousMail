from __future__ import annotations

from pydantic import BaseModel, Field


class Email(BaseModel):
    id: int
    from_: str = Field(alias="from")
    subject: str
    date: str


class Message(BaseModel):
    id: int
    from_: str = Field(alias="from")
    subject: str
    date: str
    attachments: list[Attachment]
    body: str
    text_body: str = Field(alias="textBody")
    html_body: str = Field(alias="htmlBody")


class Attachment(BaseModel):
    file_name: str = Field(alias="filename")
    content_type: str = Field(alias="contentType")
    size: int

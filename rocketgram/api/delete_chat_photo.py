# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Union

from .request import Request


@dataclass(frozen=True)
class DeleteChatPhoto(Request):
    """\
    Represents DeleteChatPhoto request object:
    https://core.telegram.org/bots/api#deletechatphoto
    """

    method = "deleteChatPhoto"

    chat_id: Union[int, str]
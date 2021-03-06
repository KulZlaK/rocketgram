# Copyright (C) 2015-2020 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, List

from .request import Request
from .update_type import UpdateType
from .. import api


@dataclass(frozen=True)
class GetUpdates(Request):
    """\
    Represents GetUpdates request object:
    https://core.telegram.org/bots/api#getupdates
    """

    offset: Optional[int] = None
    limit: Optional[int] = None
    timeout: Optional[int] = None
    allowed_updates: Optional[List[UpdateType]] = None

    def parse_result(self, data) -> List['api.Update']:
        assert isinstance(data, list), "Should be list."
        return [api.Update.parse(r) for r in data]

    async def send2(self) -> List['api.Update']:
        res = await self._send()
        return res.result

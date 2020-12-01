import re
from typing import Dict

import aiohttp
from bs4 import BeautifulSoup

FINANCE_URL = "https://finance.naver.com/item/sise.nhn?code="


async def get_soup_object(url):
    async with aiohttp.ClientSession() as sess:
        async with sess.get(url) as res:
            return BeautifulSoup(await res.text(), "html.parser")


async def get_stock_status(code: str) -> Dict:
    soup = await get_soup_object(FINANCE_URL + code)

    title = soup.select("table.type2.type_tax > tbody > tr > th.title")
    data = soup.select("table.type2.type_tax > tbody > tr > td.num")

    result = {h.get_text(): float(re.sub("[^.0-9+-]", "", d.get_text())) for (h, d) in zip(title, data)}

    return result

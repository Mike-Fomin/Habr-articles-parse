import asyncio
from itertools import cycle

import aiohttp
from bs4 import BeautifulSoup

with open("proxy_http_ip.txt", "r") as prx_file:
    PROXY_LIST = list(map(str.strip, prx_file.readlines()))

category = "python"
category_url = f"https://habr.com/ru/hub/{category}/"


async def parse_category(cat_url, session, prx, page):
    response = await session.get(cat_url, proxy=f"http://{prx}")
    resp = await response.text()

    soup_art = BeautifulSoup(markup=resp, features="lxml")
    articles_block = soup_art.find_all("article", class_="tm-articles-list__item")
    title_block = list(map(lambda x: x.find("h2", class_="tm-title tm-title_h2"), articles_block))
    print(f"{page=} done!")
    return [(tl.text, f"https://habr.com{tl.find('a').get('href')}") for tl in title_block]


async def main():
    async with aiohttp.ClientSession() as session:
        response = await session.get(category_url)
        resp = await response.text()

        # get total pages
        soup = BeautifulSoup(markup=resp, features="lxml")
        pages = int(soup.find("div", class_="tm-pagination").find_all("a")[-2].text.strip())
        print(f"total number of {pages=}")

        # get async tasks
        tasks = []
        for page, proxy in zip(range(1, pages+1), cycle(PROXY_LIST)):
            task = asyncio.ensure_future(parse_category(f"{category_url}page{page}/", session, proxy, page))
            tasks.append(task)
            await asyncio.sleep(0.2)
        articles = await asyncio.gather(*tasks)

        # write results into file
        with open("habr_articles.txt", "w", encoding="utf-8") as file:
            i = 1
            for art in articles:
                for title, link in art:
                    file.write(f"{i}) {title} \n    {link}\n")
                    i += 1

if __name__ == "__main__":
    asyncio.run(main())


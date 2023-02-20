import asyncio

from crawler import Spider
from utils import save_to_file


async def main(master_dict):
    filewrite_tasks = []
    with open("index.txt", "w") as f:
        i = 0
        for url, content in master_dict.items():
            i += 1
            filewrite_tasks.append(asyncio.ensure_future(save_to_file(content, f"pages/{i}.html")))
            f.write(f"{i}.html - {url}\n")
    await asyncio.gather(*filewrite_tasks)


urls = []
with open("urls.txt", "r") as f:
    for line in f:
        urls.append(line)

spider = Spider(urls)

spider.run()

asyncio.run(main(spider.master_dict))

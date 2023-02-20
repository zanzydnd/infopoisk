# import requests
# from bs4 import BeautifulSoup
#
# if __name__ == '__main__':
#     url = 'https://2ch.hk/'
#     reqs = requests.get(url)
#     soup = BeautifulSoup(reqs.text, 'html.parser')
#
#     urls = []
#     for link in soup.find_all('a'):
#         urls.append(link.get('href'))
#
#     with open("urls2.txt", "w") as f:
#         for url in urls:
#             f.write(f"{url}\n")
#             # f.write(f"https://stackoverflow.com/questions/{i}\n")


set_ = set()
with open("urls.txt", "r") as f:
    for line in f:
        set_.add(line)

with open("urls.txt", "w") as f:
    for line in set_:
        f.write(line)
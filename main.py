
from dotenv import load_dotenv
import os
import argparse
import requests
from urllib.parse import urlparse


def is_bitlink(token: str, link: str) -> bool:
    parsed_link = urlparse(link)
    source_url = f'https://api-ssl.bitly.com/\
v4/bitlinks/{parsed_link.netloc}{parsed_link.path}'
    headers = {'Authorization': 'Bearer {}'.format(token)}
    response = requests.get(source_url, headers=headers)
    return response.ok


def count_clicks(token: str, link: str) -> str:
    parsed_link = urlparse(link)
    source_url = f'https://api-ssl.bitly.com/v4/bitlinks\
/{parsed_link.netloc}{parsed_link.path}/clicks/summary'
    headers = {'Authorization': 'Bearer {}'.format(token)}
    response = requests.get(source_url, headers=headers)
    response.raise_for_status()
    return response.json()['total_clicks']


def shorten_link(token: str, link: str) -> str:
    source_url = 'https://api-ssl.bitly.com/v4/bitlinks'
    headers = {'Authorization': 'Bearer {}'.format(token)}
    long_url = {'long_url': link}
    response = requests.post(
        source_url,
        json=long_url,
        headers=headers
    )
    response.raise_for_status()
    return response.json()['link']


def main():
    load_dotenv()
    token = os.environ['BITLY_API_KEY']

    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="long or shot url", type=str)
    args = parser.parse_args()
    user_url = args.url

    if is_bitlink(token, user_url):
        try:
            print(f'По вашей ссылке перешли: \
{count_clicks(token, user_url)} раз(а)')
        except requests.exceptions.HTTPError:
            print('Не удалось получить информацию по сссылке')
    else:
        try:
            print(f'Битлинк: {shorten_link(token, user_url)}')
        except requests.exceptions.HTTPError:
            print('Не удалось создать сссылку')


if __name__ == '__main__':
    main()

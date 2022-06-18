import requests
import json

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'Authorization': 'KakaoAK 7f51314eda8f6720d53ba1c2c8b944c0',
    'Connection': 'keep-alive',
    'KA': 'sdk/4.4.3 os/javascript lang/ko-KR device/Win32 origin/https%3A%2F%2Ftablog.neocities.org',
    'Origin': 'https://tablog.neocities.org',
    'Referer': 'https://tablog.neocities.org/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows"
}
def get_coord_by_query(query):
    url = f"https://dapi.kakao.com/v2/local/search/keyword.json?query={query}&size=15"
    r = requests.get(url, headers=headers)
    return json.loads(r.text)
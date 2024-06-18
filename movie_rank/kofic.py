import requests
import json
import pandas as pd
from datetime import datetime


api_key = ""
date = str(datetime.now().date()).replace("-", "")
url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
params ={'key' : api_key, 'targetDt' : "20240516", 'itemPerPage' : '10'}

response = requests.get(url, params=params)

movie_rank_columns = ["박스오피스", "영화", "개봉일", "누적관객수", "현재상영관수"]
movie_rank_df = pd.DataFrame(columns=movie_rank_columns)

for i, movie_info in enumerate(json.loads(response.text)["boxOfficeResult"]["dailyBoxOfficeList"]):
    movie_rank_df.loc[i] = [movie_info["rank"], movie_info["movieNm"], movie_info["openDt"], movie_info["audiCnt"], movie_info["scrnCnt"]]


print(movie_rank_df.set_index("박스오피스"), "\nKofic(영화진흥위원회) 제공")


"""
rank: 순위
movieNm: 영화명
openDt: 개봉일
audiCnt: 누적관객수
scrnCnt: 해당일자 상영한 스크린 수
"""

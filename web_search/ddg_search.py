from duckduckgo_search import DDGS


def get_url_list(query: str, limit=5) -> list[str]:
    search_result = DDGS().text(query, max_results=limit, region="kr-kr")
    url_list = [i["href"] for i in search_result]

    return url_list


"""
DDGS().new() 도 가능
"""

from langchain_community.utilities.google_search import GoogleSearchAPIWrapper


api_key = ""
cse_id = ""


def get_url_list(query: str, limit: int) -> list[str]:
    result: list[str] = []
    search = GoogleSearchAPIWrapper(
        google_api_key=api_key,
        google_cse_id=cse_id,
    )
    for web_info in search.results(query, limit):
        if not web_info.get("link", None):
            break
        result.append(web_info["link"])

    return result

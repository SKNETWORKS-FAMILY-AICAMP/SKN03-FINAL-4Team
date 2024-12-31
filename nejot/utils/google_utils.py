from googleapiclient.discovery import build

def google_search(query, num, google_api_key, google_cse_id):
    service = build("customsearch", "v1", developerKey=google_api_key)
    res = service.cse().list(q=query, cx=google_cse_id, num=num).execute()
    items = res.get("items", [])
    return items
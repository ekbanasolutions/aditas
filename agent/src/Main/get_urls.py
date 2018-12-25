from urls import path

urls = path

final_urls = {}

def all():
    for url, value in urls.items():
        if callable(value):
            final_urls[url] = value
        elif isinstance(value, dict):
            url = url[:-1]
            for u, v in value.items():
                u = url + u
                final_urls[u] = v

    return final_urls
import requests

internal_url = "http://127.0.0.1:5000/meta/"

internal_url = "http://127.0.0.1:5000/meta/scrapper"


def meta_scrapper_endpoint():
    pass


postdata = {
    'name': (None, "pytest"),
    'entries': (None, 2),
    'data': (None, '2022-01-01'),
    'errors': (None, 0)
}

r = requests.post(internal_url, files=postdata)
print(r)
r = requests.get(internal_url)
print(r.text)

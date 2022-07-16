import requests

internal_url = "http://127.0.0.1:5000/meta/scrapperdata"
internal_url2 = "http://127.0.0.1:5000/meta/scrapper"


def meta_scrapper_getendpoint():

    # Check get statement
    r = requests.get(internal_url)
    assert r.status_code == 200


def meta_scrapper_postendpoint():

    # Check get statement
    postdata = {
        'name': (None, "pytest"),
        'entries': (None, 2),
        'date': (None, '2022-01-01'),
        'errors': (None, 0)
    }

    r = requests.post(internal_url2, files=postdata)
    assert r.status_code == 204

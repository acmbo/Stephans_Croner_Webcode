import requests
import json

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


def meta_scrapper_delete_endpoint():

    # Check get statement
    postdata = {
        'id': (None, "10"),
    }

    r = requests.delete(internal_url2, files=postdata)
    assert r.status_code == 204


def keywords_to_api():

    datas = {'kw1': 1, 'kw2': 2}

    url = "http://127.0.0.1:5000/meta/keywordsmonth/"

    r = requests.post(url, json=datas)
    assert r.status_code == 204


# Postings - Week

def meta_postingsweek_getendpoint():
    url = "http://127.0.0.1:5000/meta/postingsweek/"
    # Check get statement
    r = requests.get(url)
    print(r)
    assert r.status_code == 200


def meta_postingsweek_postendpoint():
    url = "http://127.0.0.1:5000/meta/postingsweek/"
    # Check get statement
    postdata = {
        'post': (None, 1),
        'date': (None, '2022-07-15'),
    }

    r = requests.post(url, files=postdata)
    print(r)
    assert r.status_code == 204


def meta_postingsweek_delete_endpoint():

    url = "http://127.0.0.1:5000/meta/postingsweek/"
    r = requests.delete(url)
    print(r)
    assert r.status_code == 204


def meta_postingsmonth_getendpoint():
    url = "http://127.0.0.1:5000/meta/postingsmonth/"
    # Check get statement
    r = requests.get(url)
    print(r)
    assert r.status_code == 200


def meta_postingsmonth_postendpoint():
    url = "http://127.0.0.1:5000/meta/postingsmonth/"
    # Check get statement
    postdata = {
        'post': (None, 1),
        'date': (None, '2022-07-13'),
    }

    r = requests.post(url, files=postdata)
    print(r)
    assert r.status_code == 204


def meta_postingsmonth_delete_endpoint():

    url = "http://127.0.0.1:5000/meta/postingsmonth/"
    r = requests.delete(url)
    print(r)
    assert r.status_code == 204

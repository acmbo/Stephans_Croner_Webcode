import requests
import json

internal_url = "http://127.0.0.1:5000/meta/scrapperdata"
internal_url2 = "http://127.0.0.1:5000/meta/scrapper"


def meta_scrapper_getendpoint():
    internal_url = "http://127.0.0.1:5000/meta/scrapperdata"
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
    internal_url2 = "http://127.0.0.1:5000/meta/scrapper"
    # Check get statement
    postdata = {
        'id': (None, "22"),
    }

    r = requests.delete(internal_url2, files=postdata)
    print(r)
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


# Postings - Month

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


# Postings - Year

def meta_postingsyear_getendpoint():
    url = "http://127.0.0.1:5000/meta/postingsyear/"
    # Check get statement
    r = requests.get(url)
    print(r)
    assert r.status_code == 200


def meta_postingsyear_postendpoint():
    url = "http://127.0.0.1:5000/meta/postingsyear/"
    # Check get statement
    postdata = {
        'post': (None, 1),
        'date': (None, '2022-05-02'),
    }

    r = requests.post(url, files=postdata)
    print(r)
    assert r.status_code == 204


def meta_postingsyear_delete_endpoint():

    url = "http://127.0.0.1:5000/meta/postingsyear/"
    r = requests.delete(url)
    print(r)
    assert r.status_code == 204


# ---------------------- Graphendpoints --------------------------

# Daily

def graphedges_get_endpoint_daily():
    url = "http://127.0.0.1:5000/themegraph/themeGraphDaily/"
    r = requests.get(url)
    print(r)
    print(r.json())
    assert r.status_code == 200


def graphedges_post_endpoint_daily():
    url = "http://127.0.0.1:5000/themegraph/themeGraphDaily/"

    # Check get statement
    postdata = [
        {"source": "Test1", "target": "Test2", "value": 1, "urls": ""},
        {"source": "Test1", "target": "Test2", "value": 1, "urls": ""},
        {"source": "Test1", "target": "Test2", "value": 1, "urls": ""},
        {"source": "Test1", "target": "Test2", "value": 1, "urls": ""},
        {"source": "Test1", "target": "Test2", "value": 1, "urls": ""},
        {"source": "Test1", "target": "Test2", "value": 1, "urls": ""},
        {"source": "Test1", "target": "Test2", "value": 1, "urls": ""},
        {"source": "Test1", "target": "Test2", "value": 1, "urls": ""},
    ]

    r = requests.post(url, json=postdata)
    print(r)
    assert r.status_code == 204


def graphedges_delete_endpoint_daily():
    url = "http://127.0.0.1:5000/themegraph/themeGraphDaily/"
    r = requests.delete(url)
    print(r)
    assert r.status_code == 204


# Weekly


def graphedges_get_endpoint_week():
    url = "http://127.0.0.1:5000/themegraph/themeGraphWeekly/"
    r = requests.get(url)
    print(r)
    print(r.json())
    assert r.status_code == 200


def graphedges_post_endpoint_week():
    url = "http://127.0.0.1:5000/themegraph/themeGraphWeekly/"

    # Check get statement
    postdata = [
        {"source": "Test1", "target": "Test2", "value": 1, "urls": ""},
        {"source": "Test1", "target": "Test2", "value": 1, "urls": ""},
        {"source": "Test1", "target": "Test2", "value": 1, "urls": ""},
        {"source": "Test1", "target": "Test2", "value": 1, "urls": ""},
        {"source": "Test1", "target": "Test2", "value": 1, "urls": ""},
        {"source": "Test1", "target": "Test2", "value": 1, "urls": ""},
        {"source": "Test1", "target": "Test2", "value": 1, "urls": ""},
        {"source": "Test1", "target": "Test2", "value": 1, "urls": ""},
    ]

    r = requests.post(url, json=postdata)
    print(r)
    assert r.status_code == 204


def graphedges_delete_endpoint_week():
    url = "http://127.0.0.1:5000/themegraph/themeGraphWeekly/"
    r = requests.delete(url)
    print(r)
    assert r.status_code == 204


# Monthly


def graphedges_get_endpoint_month():
    url = "http://127.0.0.1:5000/themegraph/themeGraphMonthly/"
    r = requests.get(url)
    print(r)
    print(r.json())
    assert r.status_code == 200


def graphedges_post_endpoint_month():
    url = "http://127.0.0.1:5000/themegraph/themeGraphMonthly/"

    # Check get statement
    postdata = [
        {"source": "Test1", "target": "Test2", "value": 1, "urls": ""},
        {"source": "Test1", "target": "Test2", "value": 1, "urls": ""},
        {"source": "Test1", "target": "Test2", "value": 1, "urls": ""},
        {"source": "Test1", "target": "Test2", "value": 1, "urls": ""},
        {"source": "Test1", "target": "Test2", "value": 1, "urls": ""},
        {"source": "Test1", "target": "Test2", "value": 1, "urls": ""},
        {"source": "Test1", "target": "Test2", "value": 1, "urls": ""},
        {"source": "Test1", "target": "Test2", "value": 1, "urls": ""},
    ]

    r = requests.post(url, json=postdata)
    print(r)
    assert r.status_code == 204


def graphedges_delete_endpoint_month():
    url = "http://127.0.0.1:5000/themegraph/themeGraphMonthly/"
    r = requests.delete(url)
    print(r)
    assert r.status_code == 204



# Testendpoint

def test_get_endpoint_():
    url = "http://127.0.0.1:5000/themegraph/testjson/"
    url = "http://stephanscorner.de/themegraph/testjson"
    r = requests.get(url)
    print(r)
    print(r.json())
    """
    data = r.json()
    import datetime
    new_data=[]
    
    for i in range(len(data["autor"])):
        tempdict = {'autor':data["autor"][str(i)],
                    'date': datetime.datetime.strptime(data["date"][str(i)],"%d.%M.%Y").isoformat(),
                    'h4article':data["h4article"][str(i)],
                    'meistgelesen':data["meistgelesen"][str(i)],
                    'themen':data["themen"][str(i)],
                    'themenseiten': data["themenseiten"][str(i)],
                    'count':1}
        new_data.append(tempdict)
    """
    assert r.status_code == 200
    

def test_post_endpoint():
    url = "http://127.0.0.1:5000/themegraph/testjson/"

    # Check get statement
    postdata = [
        {"source": "Test1", "target": "Test2", "value": 1, "urls": ""},
        {"source": "Test1", "target": "Test2", "value": 1, "urls": ""},
        {"source": "Test1", "target": "Test2", "value": 1, "urls": ""},
        {"source": "Test1", "target": "Test2", "value": 1, "urls": ""},
        {"source": "Test1", "target": "Test2", "value": 1, "urls": ""},
        {"source": "Test1", "target": "Test2", "value": 1, "urls": ""},
        {"source": "Test1", "target": "Test2", "value": 1, "urls": ""},
        {"source": "Test1", "target": "Test2", "value": 1, "urls": ""},
    ]

    r = requests.post(url, json=postdata)
    print(r)
    assert r.status_code == 204


def test_delete_endpoint():
    url = "http://127.0.0.1:5000/themegraph/testjson/"
    r = requests.delete(url)
    print(r)
    assert r.status_code == 204
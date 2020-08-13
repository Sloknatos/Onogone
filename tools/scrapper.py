import bs4
from urllib.request import Request, urlopen
from urllib import parse
from files.env import ajax_hash, request_url
import json
import hashlib


comment_result = {}


def transform_url(url):
    # Get the JVC url and transform it to have the comments page
    url_splitted = url.split("/")
    wanted_segment = [0, 1, 2, 3, 4]
    url_comment = ""
    for i in wanted_segment:
        end = "/" if i != 4 else ""
        segment = url_splitted[i] if i != 3 else "commentaires"
        url_comment += segment + end
    return url_comment


def get_pages(url):
    # Get the number of pages
    req = Request(url)
    response = urlopen(req)
    soup = bs4.BeautifulSoup(response, 'html.parser')
    pagination = soup.find_all("div", {
        "class": "bloc-liste-num-page"
        })

    return len(pagination[0])


def scrap(url):
    url_comment = transform_url(url)
    pages = get_pages(url_comment + "-1")

    for i in range(1, pages + 1):  # For each page
        req = Request(url_comment + f'-{i}')
        resp = urlopen(req)
        comments_list = get_comment_block_from_response(resp)

        for comment_block in comments_list:  # For each comment
            id = comment_block.get('data-id')
            answers_list = get_answer_block_from_comment_id(id)
            serialize_comment_from_block(comment_block)
            for answer in answers_list:  # For each answer
                serialize_comment_from_block(answer, True)
    return comment_result


def get_answer_block_from_comment_id(comment_id):
    data = {
        "id_commentaire": comment_id,
        "ajax_hash": ajax_hash
    }
    data = parse.urlencode(data).encode()
    req = Request(request_url, data=data)
    resp = urlopen(req)
    try:
        answer_list = []
        tab_reponse = json.loads(resp.read().decode("utf-8"))['tab_reponse']
        for elem in tab_reponse:
            soup = bs4.BeautifulSoup(elem['render'], "html.parser")
            answer_list.append(soup.find("div", {
                "class": "txt-msg text-enrichi-forum"
            }))
        return answer_list
    except Exception:
        return []


def get_comment_block_from_response(response):
    soup = bs4.BeautifulSoup(response, 'html.parser')
    comments_list = soup.find_all("div", {
        "class": "bloc-message-forum commentaire-parent"
    })
    return comments_list


def get_comment_text_from_block(comment_block):
    try:
        comment_text = []
        soup = bs4.BeautifulSoup(str(comment_block), 'html.parser')
        bs4_comment_text_object = soup.find_all("div", {
            "class": "txt-msg text-enrichi-forum"
        })
        for elem in bs4_comment_text_object:
            for div in elem.find_all("blockquote", {
                "class": "blockquote-jv"
            }):
                div.decompose()

            comment_text.append(elem.p.text)
        return " ".join(comment_text)
    except Exception as err:
        print(f'Get this ERROR: {err}')
        return None


def serialize_comment_from_block(comment_block, answer=False):
    text = get_comment_text_from_block(comment_block)
    id = f'anwser {hash(text)}' if answer else comment_block.get('data-id')
    comment_result[id] = text
    return True

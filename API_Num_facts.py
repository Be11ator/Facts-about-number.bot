import requests
def text_num(types_, num):

    if types_ == "date":

        data = requests.get(f"http://numbersapi.com/{num[0]}/{num[1]}/{types_}?json")
    else:
        data = requests.get(f"http://numbersapi.com/{num}/{types_}?json")

    texts = data.json()

    return texts
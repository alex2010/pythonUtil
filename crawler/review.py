import requests
from bs4 import BeautifulSoup
import json
import random
import time
import matplotlib.pyplot as plt

def scrape_reviews(url):
    web_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Cookie': 'session-id=130-0763099-6679354; ubid-main=131-5978447-8087254; skin=noskin; session-id-time=2082787201l; av-timezone=Asia/Shanghai; i18n-prefs=USD; aws_lang=en; sp-cdn="L5Z9:AR"; lc-main=en_US; session-token="ETnDtB3CxHFfei1rZh4KmR42i5lvFSUpqfCq6OIS6QjAOxFuTsji9vGWOUNIzBInzM2dkyftz2wwp6ndlxZI9FASjue07mIyieAuXA03fAldd5tzD2t/uQ4QjOk2MHxTa++GCaOEaGOS6vnl25N3zqI7sUJdbwPT8DScZY0tOLBFjBj5Cp7bp+2Vs0TeA0dPRtEqjvjTJOIyvQr66NiJWJ6QBlw5gFPiEcAAcpbkLGQ="',
        'TE': 'Trailers'}
    response = requests.get(url=url, headers=web_header)
    soup = BeautifulSoup(response.text, 'html.parser')
    reviews = soup.find('div', {'id': 'cm_cr-review_list'}).find_all('div', {'class': 'a-section celwidget'})
    result = []
    for review in reviews:
        data = {}
        data['username'] = review.find('span', {'class': 'a-profile-name'}).text.strip()
        data['avatarUrl'] = review.find('div', {'class': 'a-profile-avatar'}).img['src']
        data['title'] = review.find('a', {'class': 'review-title'}).span.text.strip()
        title_str = review.find('a', {'class': 'a-link-normal'}).get('title')
        if title_str:
            data['rating'] = title_str.split(' ')[0]
        date_str = review.find('span', {'class': 'review-date'}).text.strip().replace('Reviewed in the ', '')
        if date_str:
            data['country'], data['date'] = date_str.split(' on ')
        material_type_str = review.find('div', {'class': 'review-format-strip'}).find('a',
                                                                                      {'class': 'a-size-mini'}).text
        data['material_type'] = material_type_str.split(': ')[1]
        data['content'] = review.find('span', {'class': 'review-text'}).text.strip()
        result.append(data)
    # print(result)
    # with open('reviews.json', 'w', encoding='utf-8') as f:
    #     json.dump(result, f, ensure_ascii=False, indent=4)
    return result


# scrape_reviews(
#     'https://www.amazon.com/Ksports-Badminton-Shuttlecocks-Pack-Tube/product-reviews/B07XG449VF/ref=cm_cr_getr_d_paging_btm_prev_1?ie=UTF8&reviewerType=all_reviews&pageNumber=1')
#

def scrape_reviews_from_urls(url_list):
    reviews = []
    for url in url_list:
        reviews.extend(scrape_reviews(url))
        time.sleep(random.randint(7, 15))

    with open('reviews.json', 'w', encoding='utf-8') as f:
        json.dump(reviews, f, ensure_ascii=False, indent=4)


scrape_url_list = []
for n in range(1, 6):
    scrape_url_list.append(
        'https://www.amazon.com/Ksports-Badminton-Shuttlecocks-Pack-Tube/product-reviews/B07XG449VF/ref=cm_cr_getr_d_paging_btm_prev_1?ie=UTF8&reviewerType=all_reviews&pageNumber=' + str(
            n))


scrape_reviews_from_urls(scrape_url_list)

def generate_pie_chart(file_path):
    # read json file
    with open(file_path, 'r') as f:
        data = json.load(f)

    # group data by rating
    rating_count = {}
    for review in data:
        rating = review['rating']
        if rating in rating_count:
            rating_count[rating] += 1
        else:
            rating_count[rating] = 1

    # generate pie chart
    labels = ['{} stars'.format(rating) for rating in rating_count]
    sizes = [rating_count[rating] for rating in rating_count]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    plt.title('Distribution of Ratings')
    plt.show()


generate_pie_chart('/Users/alexwang/Projects/pythonUtil/crawler/reviews.json')

from locust import HttpUser, task, between
import random

# list of 100 valid urls
list_of_urls = ["https://www.google.com",
                "https://www.youtube.com",
                "https://www.facebook.com",
                "https://www.baidu.com",
                "https://www.wikipedia.org",
                "https://www.yahoo.com",
                "https://www.amazon.com",
                "https://www.qq.com",
                "https://www.google.co.in",
                "https://www.twitter.com",
                "https://www.live.com",
                "https://www.taobao.com",
                "https://www.bing.com",
                "https://www.instagram.com",
                "https://www.weibo.com",
                "https://www.sina.com.cn",
                "https://www.linkedin.com",
                "https://www.yahoo.co.jp",
                "https://www.msn.com",
                "https://www.vk.com",
                "https://www.google.de",
                "https://www.yandex.ru",
                "https://www.hao123.com",
                "https://www.google.co.uk",
                "https://www.reddit.com",
                "https://www.ebay.com",
                "https://www.google.fr",
                "https://www.t.co",
                "https://www.tmall.com",
                "https://www.google.com.br",
                "https://www.360.cn",
                "https://www.sohu.com",
                "https://www.amazon.co.jp",
                "https://www.pinterest.com",
                "https://www.netflix.com",
                "https://www.google.it",
                "https://www.google.ru",
                "https://www.microsoft.com",
                "https://www.google.es",
                "https://www.wordpress.com",
                "https://www.tumblr.com",
                "https://www.paypal.com",
                "https://www.blogspot.com",
                "https://www.imgur.com",
                "https://www.stackoverflow.com",
                "https://www.aliexpress.com",
                "https://www.naver.com",
                "https://www.ok.ru",
                "https://www.apple.com",
                "https://www.github.com",
                "https://www.chinadaily.com.cn",
                "https://www.imdb.com",
                "https://www.google.co.kr",
                "https://www.fc2.com",
                "https://www.jd.com",
                "https://www.blogger.com",
                "https://www.163.com",
                "https://www.google.ca"]

def get_url():
    return random.choice(list_of_urls)

class WebsiteUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def load_api(self):
        self.client.get(f"/api/{get_url()}", headers={"Content-Type": "application/json"})

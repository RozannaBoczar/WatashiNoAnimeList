# https://myanimelist.net/#
import scrapy

name_eng = ""
description = ""
num_episodes = 0
status = ""
premiered = ("", "")
studio = ""
source = ""
genres = []
duration = 0
score = 0
# image - obrazek


class MyAnimeListSpider(scrapy.Spider):
    name = "anime"
    start_urls = ["https://myanimelist.net/topanime.php"]

    def parse(self, response):
        for anime in response.css("tr.ranking-list"):
            print(anime.xpath(".//td[@class='title al va-t word-break']/a/@href").getall())




# https://myanimelist.net/#
import scrapy
#
# name_eng = ""
# description = ""
# num_episodes = 0
# status = ""
# premiered = ("", "")
# studio = ""
# source = ""
# genres = []
# duration = 0
# score = 0
# image - obrazek


class MyAnimeListSpider(scrapy.Spider):
    name = "MyAnimeList"

    # start_urls = ["https://myanimelist.net/topanime.php"] -> it's the same as the def start_request(), kinda shortcut

    anime_url = " "

    def start_requests(self):
        urls = ["https://myanimelist.net/topanime.php"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for anime in response.css("tr.ranking-list"):
            # print(anime.xpath(".//td[@class='title al va-t word-break']/a/@href").get())
            next_page = anime.xpath(".//td[@class='title al va-t word-break']/a/@href").get()
            if next_page is not None:
                next_page = anime.xpath(".//td[@class='title al va-t word-break']/a/@href").get()
                yield scrapy.Request(next_page, callback=self.parse_info)

    def parse_info(self, response):
        """""
        WORKING
        titles = response.xpath("//*[@id='contentWrapper']/div[1]/div/div[1]/div")
        title_eng = titles.xpath(".//h1/strong/text()").get()
        case = titles.xpath(".//p/text()").get()  # for example season 3 of anime
        num_episodes = int(
            response.xpath("//*span[text()='Episodes:']/following-sibling::text()").get())
        """""
        # have to add multiple reading bc sometimes we have more than value
        # studios = response.xpath("/html/body/div[2]/div[2]/div[3]/div[2]/table/tbody/tr/td[1]/div/div[17]/a/text()").get()
        #description = response.xpath("/html/body/div[2]/div[2]/div[3]/div[2]/table/tbody/tr/td[2]/div[1]/table/tbody/tr[1]/td/p").get()
        # #genres = response.xpath().get()

        status = response.xpath("//span[contains(@class, 'dark_text') and text() = 'Status:']/following-sibling::text()").get()
        premiered = response.xpath("//*span[contains(@class, 'dark_text') and text() = 'Premiered:']").get()
        # source = response.xpath("/html/body/div[2]/div[2]/div[3]/div[2]/table/tbody/tr/td[1]/div/div[18]/text()").get()
        # duration = response.xpath("/html/body/div[2]/div[2]/div[3]/div[2]/table/tbody/tr/td[1]/div/div[20]/text()").get()
        # score = response.xpath("/html/body/div[2]/div[2]/div[3]/div[2]/table/tbody/tr/td[1]/div/div[22]/span[2]/text()").get()
        # image = response.xpath("/html/body/div[2]/div[2]/div[3]/div[2]/table/tbody/tr/td[1]/div/div[1]/a/img/@src").get()

        # if studios is not None or description is not None:
        #     print("Studios" + studios)

        if status is not None:
            print("Status: "+ str(status))
        # if premiered is not None:
        #     print("Premiered: " + str(premiered))

        # # if premiered is not None:
        # #     print("Premiered" + premiered)
        #
        # if source is not None:
        #     print("Source: " + source)
        #
        # if duration is not None:
        #     print("Duration: " + duration)
        #
        # if score is not None:
        #     print("Score" + score)
        #
        # if image is not None:
        #     print("Image" + image)






import scrapy
from magalu.items import ProductItem
from scrapy.http.response.html import HtmlResponse
from magalu.magalu_urls import get_urls
import re
from logging import getLogger

logger = getLogger("Magalu Spider")

class MagaluSpiderSpider(scrapy.Spider):
    name = "magalu_spider"
    allowed_domains = ["magazineluiza.com.br"]

    def start_requests(self):
        urls = get_urls(self.categories)
        for url in urls:
            yield scrapy.Request(url, meta={"playwright": True})

    def parse(self, response: HtmlResponse):
        hrefs = response.css(
            '[data-testid="product-card-container"]::attr(href)'
        ).getall()

        for href in hrefs:
            yield response.follow(href, callback=self.parse_product)

    def parse_product(self, response: HtmlResponse):
        product_item = ProductItem()
        product_item["category"] = get_category(response)
        product_item["id"] = response.url
        product_item["title"] = (
            response.css('[data-testid="heading-product-title"]::text')
            .get()
            .replace("'", "")
            .replace("\\", "")
            .replace("\"", "")
        )
        product_item["reviews"] = get_reviews(response)
        product_item["free_shipping"] = "false"
        product_item["image_url"] = get_image(response)
        product_item["price"] = get_price(response)
        product_item["previous_price"] = (
            get_previous_price(response) or product_item["price"]
        )
        product_item["discount"] = round(
            (1 - (product_item["price"] / product_item["previous_price"])) * 100
        )

        yield product_item


def get_category(response: HtmlResponse) -> str:
    container = response.css('[data-testid="breadcrumb-container"]')
    container_items = container.css('[data-testid="breadcrumb-item"]')
    category = [
        item.css("::text").get()
        for item in container_items
        if item.css("::text").get() != None
    ][:-1]
    if category:
        return " ".join(category)
    return ""


def get_reviews(response: HtmlResponse) -> int:
    inner_text = response.css('[format="score-count"]::text').get()
    if inner_text:
        x = re.search(r"\((\d+)\)", inner_text)
        return int(x.group(1))
    return 0


def get_image(response: HtmlResponse) -> str:
    image_url = response.css(
        '[data-testid="image-selected-thumbnail"]::attr(src)'
    ).get()
    if image_url:
        return image_url
    return "https://raw.githubusercontent.com/guimassoqueto/mocks/main/images/404.webp"


def get_price(response: HtmlResponse) -> float:
    price_raw = response.css('[data-testid="price-value"]::text').get()
    price_value = re.search(r"[\d\.]+\,\d{2}$", price_raw).group()
    return float(price_value.replace(".", "").replace(",", "."))


def get_previous_price(response: HtmlResponse) -> float | None:
    price_raw = response.css('[data-testid="price-original"]::text').get()
    if price_raw:
        price_value = re.search(r"[\d\.]+\,\d{2}$", price_raw).group()
        return float(price_value.replace(".", "").replace(",", "."))
    return None

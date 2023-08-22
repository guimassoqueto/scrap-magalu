# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
from itemadapter import ItemAdapter

from magalu.helpers.postgres import PostgresDB
from magalu.settings import DATA_FILE, LOG_FILE


class PlaywrightMagaluPipeline:
    async def process_item(self, item, spider):
        await PostgresDB.upsert_item("items", ItemAdapter(item).asdict())
        return item


class FinishSpiderPipeline:
    def close_spider(self, spider):
        delete_files()


def delete_files() -> None:
    if os.path.exists(DATA_FILE) and os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
        os.remove(DATA_FILE)

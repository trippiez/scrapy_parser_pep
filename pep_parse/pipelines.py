import csv
import datetime as dt
from collections import Counter

from pep_parse.settings import (BASE_DIR, DATETIME_FORMAT, FILE_FORMAT,
                                SUMM_NAME)


class PepParsePipeline:
    def __init__(self):
        self.results_dir = BASE_DIR / 'results'
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.status_counter = Counter()

    def process_item(self, item, spider):
        self.status_counter[item['status']] += 1
        return item

    def close_spider(self, spider):
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)

        file_name = f'{SUMM_NAME}_{now_formatted}.{FILE_FORMAT}'
        file_path = self.results_dir / file_name

        fieldnames = ['Статус', 'Количество']
        data = [
            {'Статус': status,
             'Количество': count
             } for status, count in self.status_counter.items()]
        total_count = sum(self.status_counter.values())

        with open(file_path, 'w+', encoding='utf-8', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
            writer.writerow({'Статус': 'Total', 'Количество': total_count})

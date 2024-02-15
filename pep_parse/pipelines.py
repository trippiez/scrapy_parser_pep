import csv
import datetime as dt
from collections import Counter
from pep_parse.settings import BASE_DIR

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
now = dt.datetime.now()
now_formatted = now.strftime(DATETIME_FORMAT)
results_dir = BASE_DIR / 'results'
results_dir.mkdir(exist_ok=True)
file_name = f'status_summary_{now_formatted}.csv'
file_path = results_dir / file_name


class PepParsePipeline:

    def open_spider(self, spider):
        self.status_counter = Counter()

    def process_item(self, item, spider):
        self.status_counter[item['status']] += 1
        return item

    def close_spider(self, spider):
        DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = results_dir / file_name
        with open(
            file_path, 'w+', encoding='utf-8', newline=''
        ) as self.csvfile:
            self.fieldnames = ['Статус', 'Количество']
            self.writer = csv.DictWriter(
                self.csvfile, fieldnames=self.fieldnames)
            self.writer.writeheader()
            for status, count in self.status_counter.items():
                self.writer.writerow({'Статус': status, 'Количество': count})
            self.csvfile.write(f'Total,{sum(self.status_counter.values())}\n')

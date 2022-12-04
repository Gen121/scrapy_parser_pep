import csv
from datetime import datetime
from pathlib import Path

from pep_parse.settings import BASE_DIR, DATETIME_FORMAT


class PepParsePipeline:
    def open_spider(self, spider):
        self.statuses = {}

    def process_item(self, item, spider):
        status = item.get('status', default=None)
        if status:
            self.statuses[status] = self.statuses.get(status, 0) + 1
        return item

    def close_spider(self, spider):
        date_time = datetime.now().strftime(DATETIME_FORMAT)
        res_dir_path = BASE_DIR / 'results'
        res_dir_path.mkdir(exist_ok=True)
        file_name = f'status_summary_{date_time}.csv'
        self.file_path = Path.joinpath(res_dir_path, file_name)
        self.statuses['Total'] = sum(self.statuses.values())
        with open(self.file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Статус', 'Количество'])
            writer.writerows(self.statuses.items())

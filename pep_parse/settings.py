from pathlib import Path

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

PEP_SPIDER_URL = 'peps.python.org'

BASE_DIR = Path(__file__).resolve().parent.parent

RESULTS = 'results'
RESULTS_DIR = BASE_DIR / RESULTS

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

FILE_FORMAT = 'csv'

ROBOTSTXT_OBEY = True


ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

PEP_NAME = 'pep'
PEP_FILE_NAME = f'{PEP_NAME}_%(time)s.{FILE_FORMAT}'
SUMM_NAME = 'status_summary'

FEEDS = {
    f'{RESULTS}/{PEP_FILE_NAME}': {
        'format': FILE_FORMAT,
        'fields': ['number', 'name', 'status'],
    },
}

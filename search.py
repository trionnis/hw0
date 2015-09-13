import re
from collections import Counter

DATA_FILE = 'iowa-liquor-sample.csv'

SEARCH_FOR = [
   {
      'name': 'Single Malt Scotch',
      'pattern': re.compile('.*single malt scotch.*', re.IGNORECASE)
   }
]

results_counter = Counter()

def process_line(line):
   for q in SEARCH_FOR:
      if q['pattern'].match(line):
         results_counter.update({q['name']})

with open(DATA_FILE, 'r') as f:
   for line in f:
      process_line(line)

print results_counter.most_common()

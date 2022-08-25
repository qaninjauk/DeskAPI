import json

from collections import Counter

with open('input.json') as f:
    j = json.load(f)

    # count = Counter()

    # for item in j:
    #     for key, value in item.items():
    #         if key.startswith('id') and value:
    #             count.update([key[4:]])
    # print(count)

    c = Counter()

    for d in j:
        for k, v in d.items():
            if k.startswith('id') and v:
                c.update([k])

            items = str(c.values())

print('Number of Saved items = ' + items)
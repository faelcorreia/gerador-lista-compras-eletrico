import json


shop_list = {}

def set_or_increase(item, qnt):
    if item in shop_list:
        shop_list[item] += qnt
    else:
        shop_list[item] = qnt

with open("itens.json") as f:
    data = json.load(f)

for key in data.keys():
    room = data[key]
    for i in room:
        total_slots = len(i["slots"])
        item = ""
        if total_slots == 1:
            item = f'{i["descricao"]} 1 slot {i["cor"]}'
        elif total_slots > 1:
            item = f'{i["descricao"]} {total_slots} slot {i["cor"]}'
        elif total_slots == 0 and "furo" not in i["descricao"]:
            item = f'{i["descricao"]} cega {i["cor"]}'
        else:
            item = f'{i["descricao"]} {i["cor"]}'
        set_or_increase(item, i["quantidade"])
        for slot in i["slots"]:
            item = f'{slot} {i["cor"]}'
            set_or_increase(item, 1)

sorted_dict = dict(sorted(shop_list.items()))
for item in sorted_dict.keys():
    print(f'{item} - {sorted_dict[item]}')
        
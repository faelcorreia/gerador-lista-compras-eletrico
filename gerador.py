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
        placa = ""
        if total_slots == 0:
            placa = f'placa {i["placa"]} cega ({i["cor"]})'
        elif total_slots == 1:
            placa = f'placa {i["placa"]} 1 seção ({i["cor"]})'
        elif total_slots == 2:
            placa = f'placa {i["placa"]} {total_slots} seções separadas ({i["cor"]})'
        elif total_slots == 3:
            placa = f'placa {i["placa"]} {total_slots} seções ({i["cor"]})'
        else:
            placa = f'placa {i["placa"]} ({i["cor"]})'
        set_or_increase(placa, i["quantidade"])
        set_or_increase(f'suporte placa {i["placa"]}', i["quantidade"])
        for slot in i["slots"]:
            item = f'{slot} ({i["cor"]})'
            set_or_increase(item, i["quantidade"])

sorted_dict = dict(sorted(shop_list.items()))
for item in sorted_dict.keys():
    print(f'- {item} - {sorted_dict[item]}')
        
import json

# Load the nested JSON data
with open('thai_zipcode_raw.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

flat_data = {'th_data':[]}
for province in data:
    for amphure in province['amphure']:
        for tambon in amphure['tambon']:
            flat_data['th_data'].append({
                'zip_code': tambon['zip_code'],
                'province_th': province['name_th'],
                'province_en': province['name_en'],
                'amphures_th': amphure['name_th'],
                'amphures_en': amphure['name_en'],
                'tombon_th': tambon['name_th'],
                'tombon_en': tambon['name_en']
            })

# Save the flattened data to a new JSON file
with open('thailand_province_flat.json', 'w', encoding='utf-8') as f:
    json.dump(flat_data, f, ensure_ascii=False, indent=4)

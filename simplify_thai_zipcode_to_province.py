import json

# Load the nested JSON data
with open('thai_zipcode_raw.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

flat_data = {'th_data':[]}
zip_codes = set()  # Use a set to keep track of unique zip codes

for province in data:
    for amphure in province['amphure']:
        for tambon in amphure['tambon']:
            zip_code = tambon['zip_code']
            if zip_code not in zip_codes:
                flat_data['th_data'].append({
                    'zip_code': zip_code,
                    'province_th': province['name_th'],
                    'province_en': province['name_en'],
                })
                zip_codes.add(zip_code)

# Save the flattened data with unique zip codes to a new JSON file
with open('thailand_province_zipcodes.json', 'w', encoding='utf-8') as f:
    json.dump(flat_data, f, ensure_ascii=False, indent=4)

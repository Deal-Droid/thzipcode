# Thai Zipcode Data Transformer

A simple tool to transform nested Thai province and zipcode data into flat JSON format for easier database integration.

## Data Source

Raw data is sourced from [kongvut/thai-province-data](https://github.com/kongvut/thai-province-data)

## Features

- Transforms nested Thai administrative data into flat JSON format
- Two output options:
  1. Complete data including province, amphure (district), and tambon (sub-district)
  2. Simplified version with unique zipcodes mapped to provinces only

## Output Formats

### Complete Format (thai_zipcode_flat.json)
```json
{
    "th_data": [
        {
            "zip_code": "10200",
            "province_th": "กรุงเทพมหานคร",
            "province_en": "Bangkok",
            "amphures_th": "พระนคร",
            "amphures_en": "Phra Nakhon",
            "tombon_th": "พระบรมมหาราชวัง",
            "tombon_en": "Phra Borom Maha Ratchawang"
        },
        ...
    ]
}
```

### Simplified Format (thai_zipcode_to_province.json)
```json
{
    "th_data": [
        {
            "zip_code": "10200",
            "province_th": "กรุงเทพมหานคร",
            "province_en": "Bangkok"
        },
        ...
    ]
}
```

## Usage

The project uses Make commands for execution:

```bash
# Generate complete flat data
make general

# Generate simplified province-only data
make province
```

## Requirements

- Python 3.x
- UV (Python package manager)

## License

This project inherits its license from the original data source. Please refer to [kongvut/thai-province-data](https://github.com/kongvut/thai-province-data) for licensing information.
```

This README provides:
1. A brief description of what the tool does
2. Credit to the original data source
3. Examples of the output formats
4. Usage instructions
5. Requirements
6. License information

You might want to customize it further by adding:
- Installation instructions if needed
- More detailed examples
- Contributing guidelines
- Any specific requirements or dependencies
- Contact information
- Additional documentation links

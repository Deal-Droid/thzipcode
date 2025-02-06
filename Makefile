.PHONY=general
general:
	uv run python simplify_thai_zipcode_flat.py

.PHONY=province
province:
	uv run python simplify_thai_zipcode_to_province.py

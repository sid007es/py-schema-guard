# py-schema-guard
A lightweight, zero-dependency Python CLI utility designed to validate CSV/JSON data pipelines against relational schemas and generate mock synthetic datasets for local integration testing.

## Key Features
- **Schema Enforcement:** Fast tabular checks for missing fields and type drift.
- **Synthetic Data Generation:** Generates schema-compliant dummy data without exposing production values.
- **Zero-PII Architecture:** Completely local; processes no external network calls or private datasets.

## Development Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest
```

## License
MIT License
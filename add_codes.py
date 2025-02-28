name: Add Codes to Supabase
on: [push]
jobs:
  add-codes:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install supabase
      - name: Run script
        run: |
          python add_codes.py

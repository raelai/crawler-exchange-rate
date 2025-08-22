 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a//dev/null b/README.md
index 0000000000000000000000000000000000000000..52478eab2b5f2b0359c7eb8b591acf19e3122ff7 100644
--- a//dev/null
+++ b/README.md
@@ -0,0 +1,32 @@
+# Exchange Rate Crawler
+
+This project provides a simple script for downloading daily exchange rate data
+from the [Taiwan Customs Administration](https://portal.sw.nat.gov.tw/APGQO/GC331#).
+The data is saved to a CSV file and can optionally be exported to an Excel file.
+
+## Requirements
+
+Install the required packages:
+
+```bash
+pip install -r requirements.txt
+```
+
+The script uses Selenium with Chrome in headless mode. Make sure a compatible
+Chrome/Chromium browser is installed in your environment.
+
+## Usage
+
+Run the crawler from the repository root:
+
+```bash
+python crawler_rate.py --csv output.csv --xlsx output.xlsx
+```
+
+The `--xlsx` argument is optional; when provided, an Excel file will be created
+alongside the CSV output.
+
+## Notes
+
+- Network access is required to download the exchange rate page.
+- The script automatically closes the browser after scraping the data.
 
EOF
)

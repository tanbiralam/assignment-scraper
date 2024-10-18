Here’s the updated `README.md` file that includes the `requirements.txt` section.

````markdown
# Web Scraping Vegetables Data

This project utilizes Selenium and BeautifulSoup to scrape data from the Otipy website's vegetable category. The script extracts information about various vegetable products, including their names, prices, and quantities, and saves the data in a JSON file.

## Features

- Automated web scraping using Selenium.
- Parses HTML content with BeautifulSoup.
- Dynamically loads more products by scrolling down the page.
- Extracts product details such as:
  - Product Name
  - Standard Price
  - Selling Price
  - MRP (Final Price)
  - Quantity
- Saves scraped data to a `products.json` file.

## Prerequisites

To run this project, ensure you have the following installed:

- Python 3.x
- Chrome WebDriver (compatible with your Chrome version)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/tanbiralam/assignment-scraper
   ```
````

2. Navigate to the project directory:

   ```bash
   cd assignment-scraper
   ```

3. Install required Python packages:

   Create a `requirements.txt` file with the following content:

   ```plaintext
   requests
   beautifulsoup4
   pandas
   selenium
   webdriver-manager
   ```

   Then run:

   ```bash
   pip install -r requirements.txt
   ```

4. Download ChromeDriver from [ChromeDriver downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in the `chromedriver` directory.

## Usage

1. Open the script file (`main.py`) in your preferred code editor.
2. Update the `chrome_driver_path` variable to point to the location of your ChromeDriver if necessary.
3. Run the script:

   ```bash
   python main.py
   ```

4. After running, the scraped product data will be saved to `products.json`.

## Example Output

The output in `products.json` will be in the following format:

```json
[
    {
        "Name": "Hydroponic Lettuce - Butterhead",
        "Standard Price": "57.4/Pack",
        "Selling Price": "67.4",
        "MRP": "57.4",
        "Quantity": "1 Pack"
    },
    ...
]
```

```

### Key Changes:
- Added a section for `requirements.txt`, including the required packages.
- Updated installation instructions to reflect using the `requirements.txt` file.

Feel free to modify any parts as needed! If you have any more requests, just let me know.
```

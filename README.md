# Telegram-Backup-Link-Scraper
This script will extract link from Telegram chat backup 

## HTML Link Scraper

This Python script allows you to scrape links from HTML files and save them to different text files based on your preferences. It uses the BeautifulSoup library to parse HTML content and extract links.

### Features

- Scrape links from multiple HTML files in a specified folder.
- Filter out links starting with '#' or 'mailto:'.
- Option to save all links, Telegra.ph links, or links without Telegra.ph to separate text files.
- User-friendly command-line interface for selecting options.
- Outputs detailed information about the scraping process.

### Usage

1. Place your HTML files in the 'input' folder.
2. Run the script and follow the on-screen instructions.
3. Select an option to save the desired links to separate text files.
4. The output files will be saved in the script directory.

### Requirements

- Python 3.x
- BeautifulSoup library (bs4)
- colorama library

### License

This project is licensed under the [MIT License](LICENSE).



## HTML Link Scraper - Usage Tutorial

This tutorial will guide you through the steps to use the HTML Link Scraper script to scrape links from HTML files.

### Step 1: Setup

1. Make sure you have Python 3.x installed on your system. If not, you can download it from the official Python website (https://www.python.org).

2. Clone or download the HTML Link Scraper repository from GitHub to your local machine.

3. Install the required dependencies by running the following command in your command-line interface:

   ```
   pip install beautifulsoup4 colorama PySimpleGUI
   ```

### Step 2: Prepare HTML Files

1. Place your HTML files in the `input` folder of the downloaded repository. You can either copy your HTML files directly into the folder or create subfolders within the `input` folder and place your HTML files there.

### Step 3: Run the Script

1. Open your command-line interface and navigate to the directory where you have the HTML Link Scraper script.

2. Run the script by executing the following command:

   ```
   python Telegram-Backup-Link-Scraper.py
   ```

### Step 4: Select Options

1. The script will display the following options on the command-line interface:

   ```
   Select an option:
   1. Save all links to 'all_links.txt'
   2. Save Telegra.ph links to 'telegra_ph_links.txt'
   3. Save links without Telegra.ph to 'link_no_telegraph.txt'
   4. Save all links, Telegra.ph links, and links without Telegra.ph to separate files
   5. Exit
   Enter the option number:
   ```

2. Enter the option number corresponding to your desired action and press Enter.

3. Depending on your selected option, the script will process the HTML files and save the extracted links to separate text files.

### Step 5: Check the Output

1. Once the script finishes processing, it will display a success message indicating the location of the output files.

2. Navigate to the script directory and locate the output files based on your selected options. The output files will be named as follows:

   - `all_links.txt`: Contains all the extracted links.
   - `telegra_ph_links.txt`: Contains only the links that start with 'https://telegra.ph/'.
   - `link_no_telegraph.txt`: Contains the links without 'https://telegra.ph/'.

### Step 6: Repeat or Exit

1. After the script completes, you can choose to run the script again with different options if needed.

2. To exit the script, select option number `5` and press Enter.

That's it! You have successfully used the HTML Link Scraper script to scrape links from HTML files. You can repeat the process for different HTML files or customize the script according to your requirements.

Note: Make sure to review and comply with the license terms mentioned in the repository before using the script.

If you have any further questions or issues, please feel free to ask!



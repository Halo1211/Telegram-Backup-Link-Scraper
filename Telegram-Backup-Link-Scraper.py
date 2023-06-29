import os
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from colorama import Fore, Style

# Function to scrape links from HTML files
def scrape_links_from_html(html_file):
    # Read the contents of the HTML file
    html_contents = html_file.read()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_contents, 'html.parser')

    # Find all the <a> tags
    a_tags = soup.find_all('a')

    # Initialize an empty list to store the links
    links = []

    # Extract the href attribute from each link
    for a_tag in a_tags:
        href = a_tag.get('href')
        if href and not href.startswith('#') and not href.startswith('mailto:'):
            parsed_url = urlparse(href)
            if parsed_url.scheme and parsed_url.netloc:
                links.append(href)

    return links

# Function to display options and get user input
def get_user_option():
    print("Select an option:")
    print("1. Save all links to 'all_links.txt'")
    print("2. Save Telegra.ph links to 'telegra_ph_links.txt'")
    print("3. Save links without Telegra.ph to 'link_no_telegraph.txt'")
    print("4. Save all links, Telegra.ph links, and links without Telegra.ph to separate files")
    print("5. Exit")
    option = input("Enter the option number: ")
    return option

# Input folder path
folder_path = "input"

# Get a list of HTML files in the folder
html_files = [file for file in os.listdir(folder_path) if file.endswith('.html')]

# Initialize empty lists to store all the links
all_links = []
telegra_ph_links = []

# Scrape links from each HTML file
for html_file_name in html_files:
    # Open the HTML file
    html_file_path = os.path.join(folder_path, html_file_name)
    html_file = open(html_file_path, 'r', encoding='utf-8')

    # Scrape links from the HTML file
    links = scrape_links_from_html(html_file)

    # Add all links to the list
    all_links.extend(links)

    # Check for telegra.ph links and add them to a separate list
    telegra_ph_links.extend([link for link in links if link.startswith('https://telegra.ph/')])

    # Close the file
    html_file.close()

# Determine the script directory
script_directory = os.path.dirname(os.path.abspath(__file__))

# Get user input for desired output
option = get_user_option()

# Write the links to the selected output file(s)
if option == '1':
    output_file = os.path.join(script_directory, "all_links.txt")
    with open(output_file, 'w', encoding='utf-8') as file:
        for link in all_links:
            file.write(link + '\n')
    print(f"{Fore.GREEN}All links have been saved to '{output_file}'.{Style.RESET_ALL}")

elif option == '2':
    output_file = os.path.join(script_directory, "telegra_ph_links.txt")
    with open(output_file, 'w', encoding='utf-8') as file:
        for link in telegra_ph_links:
            file.write(link + '\n')
    print(f"{Fore.GREEN}Telegra.ph links have been saved to '{output_file}'.{Style.RESET_ALL}")

elif option == '3':
    no_telegra_ph_links = [link for link in all_links if link not in telegra_ph_links]
    output_file = os.path.join(script_directory, "link_no_telegraph.txt")
    with open(output_file, 'w', encoding='utf-8') as file:
        for link in no_telegra_ph_links:
            file.write(link + '\n')
    print(f"{Fore.GREEN}Links without Telegra.ph have been saved to '{output_file}'.{Style.RESET_ALL}")

elif option == '4':
    all_links_output_file = os.path.join(script_directory, "all_links.txt")
    telegra_ph_output_file = os.path.join(script_directory, "telegra_ph_links.txt")
    no_telegra_ph_output_file = os.path.join(script_directory, "link_no_telegraph.txt")

    with open(all_links_output_file, 'w', encoding='utf-8') as all_links_file:
        for link in all_links:
            all_links_file.write(link + '\n')
    print(f"{Fore.GREEN}All links have been saved to '{all_links_output_file}'.{Style.RESET_ALL}")

    with open(telegra_ph_output_file, 'w', encoding='utf-8') as telegra_ph_file:
        for link in telegra_ph_links:
            telegra_ph_file.write(link + '\n')
    print(f"{Fore.GREEN}Telegra.ph links have been saved to '{telegra_ph_output_file}'.{Style.RESET_ALL}")

    no_telegra_ph_links = [link for link in all_links if link not in telegra_ph_links]
    with open(no_telegra_ph_output_file, 'w', encoding='utf-8') as no_telegra_ph_file:
        for link in no_telegra_ph_links:
            no_telegra_ph_file.write(link + '\n')
    print(f"{Fore.GREEN}Links without Telegra.ph have been saved to '{no_telegra_ph_output_file}'.{Style.RESET_ALL}")

elif option == '5':
    print("Exiting...")

else:
    print("Invalid option. Exiting...")

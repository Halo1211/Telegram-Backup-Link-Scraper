import os
import sys
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from colorama import Fore, Style
import PySimpleGUI as sg

def scrape_links_from_html(html_file):
    html_contents = html_file.read()
    soup = BeautifulSoup(html_contents, 'html.parser')
    a_tags = soup.find_all('a')
    links = []
    for a_tag in a_tags:
        href = a_tag.get('href')
        if href and not href.startswith('#') and not href.startswith('mailto:'):
            parsed_url = urlparse(href)
            if parsed_url.scheme and parsed_url.netloc:
                links.append(href)
    return links

def save_links_to_file(links, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for link in links:
            file.write(link + '\n')

def get_user_option():
    layout = [
        [sg.Text('Select an option:')],
        [sg.Radio("Save all links to 'all_links.txt'", "option", default=True, key='option1')],
        [sg.Radio("Save Telegra.ph links to 'telegra_ph_links.txt'", "option", key='option2')],
        [sg.Radio("Save links without Telegra.ph to 'link_no_telegraph.txt'", "option", key='option3')],
        [sg.Radio("Save all links, Telegra.ph links, and links without Telegra.ph to separate files", "option", key='option4')],
        [sg.Button('OK')]
    ]

    window = sg.Window('Options', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            sys.exit(0)

        if event == 'OK':
            if values['option1']:
                return 1
            elif values['option2']:
                return 2
            elif values['option3']:
                return 3
            elif values['option4']:
                return 4

    window.close()

folder_path = "input"
html_files = [file for file in os.listdir(folder_path) if file.endswith('.html')]
all_links = []
telegra_ph_links = []

for html_file_name in html_files:
    html_file_path = os.path.join(folder_path, html_file_name)
    html_file = open(html_file_path, 'r', encoding='utf-8')
    links = scrape_links_from_html(html_file)
    all_links.extend(links)
    telegra_ph_links.extend([link for link in links if link.startswith('https://telegra.ph/')])
    html_file.close()

user_option = get_user_option()

if user_option == 1:
    save_links_to_file(all_links, "all_links.txt")
    print("All links have been saved to 'all_links.txt'.")
elif user_option == 2:
    save_links_to_file(telegra_ph_links, "telegra_ph_links.txt")
    print("Telegra.ph links have been saved to 'telegra_ph_links.txt'.")
elif user_option == 3:
    no_telegra_ph_links = [link for link in all_links if link not in telegra_ph_links]
    save_links_to_file(no_telegra_ph_links, "link_no_telegraph.txt")
    print("Links without Telegra.ph have been saved to 'link_no_telegraph.txt'.")
elif user_option == 4:
    save_links_to_file(all_links, "all_links.txt")
    save_links_to_file(telegra_ph_links, "telegra_ph_links.txt")
    no_telegra_ph_links = [link for link in all_links if link not in telegra_ph_links]
    save_links_to_file(no_telegra_ph_links, "link_no_telegraph.txt")
    print("All links, Telegra.ph links, and links without Telegra.ph have been saved to separate files.")

sg.popup('Process completed.', title='Finished')

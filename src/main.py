import requests
from bs4 import BeautifulSoup
import json
import os

# Base URL of the website to scrape
base_url = 'https://example-blog.com/'

# Function to scrape a single article
def scrape_article(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract article details
    title = soup.find('h1').get_text()
    author = soup.find('span', class_='author').get_text()
    date = soup.find('time').get_text()
    content = soup.find('div', class_='entry-content').get_text()

    return {
        'title': title,
        'author': author,
        'date': date,
        'content': content
    }

# Function to scrape multiple articles
def scrape_articles(start_page, num_pages):
    articles = []
    for i in range(start_page, start_page + num_pages):
        url = f'{base_url}page/{i}/'
        print(f'Scraping page {i}: {url}')
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Error fetching the URL: {e}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        for article in soup.find_all('article'):
            article_url = article.find('a')['href']
            article_data = scrape_article(article_url)
            if article_data:
                articles.append(article_data)

    return articles

# Main function to run the scraper
def main():
    start_page = 1
    num_pages = 5  # Number of pages to scrape
    articles = scrape_articles(start_page, num_pages)

    # Ensure the data directory exists
    output_dir = '../data'
    os.makedirs(output_dir, exist_ok=True)

    # Save the data to a JSON file
    output_file = os.path.join(output_dir, 'articles.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(articles, f, ensure_ascii=False, indent=4)

    print(f'Scraping complete. Data saved to {output_file}')

if __name__ == '__main__':
    main()
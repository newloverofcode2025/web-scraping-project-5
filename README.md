# web-scraping-project-5
 A web scraper that extracts data from a website with a more complex structure, such as a blog or news site. We'll scrape articles, including titles, authors, publication dates, and content, and save this data to a JSON file. This project will also introduce you to handling more complex HTML structures and extracting data from multiple pages.

## Project Structure
web-scraping-project-5/
├── src/
│   └── main.py
├── data/
│   └── articles.json
└── README.md

## Dependencies
- Python
- requests
- beautifulsoup4

## Setup
1. Clone the repository.
2. Install the required libraries using `pip install requests beautifulsoup4`.
3. Run the script using `python src/main.py`.

## Usage
- The script scrapes article details from the specified blog and saves them to `data/articles.json`.

## Notes
- Replace the base URL in `main.py` with the blog you want to scrape.
- Ensure you have permission to scrape the website and comply with its `robots.txt` file.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
Commit and Push Changes:
Open GitHub Desktop.
Make sure your repository is selected.
Click on "Changes" to see the files you've added.
Write a commit message (e.g., "Initial commit with blog article scraping project").
Click "Commit to main".
Click "Push origin" to push your changes to GitHub.
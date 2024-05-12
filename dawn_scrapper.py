import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
import pandas as pd
import time

# Function to extract articles from a main page and follow specified links
def extract_articles(url):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    
    articles = []

    try:
        # Request the main page content with the custom header
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Ensure the request was successful

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all anchor tags with the specified class
        internal_links = soup.find_all('a', {'class': 'story__link'})

        # Loop through all found links
        for anchor in internal_links:
            # Get the link from the anchor tag
            article_href = anchor.get('href', '')

            # Convert relative URLs to absolute URLs
            if not article_href.startswith("https"):
                article_url = requests.compat.urljoin(url, article_href)
            else:
                article_url = article_href

            try:
                # Add a delay to avoid overloading the server or triggering rate limits
                time.sleep(1)

                # Fetch the full article content with the custom header
                article_response = requests.get(article_url, headers=headers)
                article_response.raise_for_status()  # This can raise HTTPError if status code is 4xx or 5xx

                # Parse the detailed article content
                article_soup = BeautifulSoup(article_response.content, 'html.parser')

                # Find the <article> tag to extract content
                article_tag = article_soup.find('article')

                if article_tag:
                    # Extract the title from an <h2> within the <article>
                    title_div = article_tag.find('h2', {'class': 'story__title'})
                    print(title_div)
                    article_title = title_div.text.strip() if title_div else 'No Title'
                    print(article_title)

                    # Extract all text from <p> tags within the same <article>
                    description_parts = []
                    story_content = article_tag.find('div', {'class': 'story__content'})
                    for paragraph in story_content.find_all('p'):
                        description_parts.append(paragraph.text.strip())
                    
                    article_description = " ".join(description_parts)  # Join all parts to form a single description

                    # Add the extracted data to the articles list
                    articles.append({
                        'Title': article_title,
                        'Description': article_description,
                        'Source': article_url,
                    })

            except HTTPError as http_err:
                # If a 403 error occurs, log it and continue
                print(f"HTTP error for {article_url}: {http_err}")

            except Exception as err:
                # Log any other errors and continue
                print(f"An error occurred with {article_url}: {err}")

    except HTTPError as http_err:
        # Log HTTP errors from the main page request
        print(f"HTTP error occurred for main page: {http_err}")

    except Exception as err:
        # Log other exceptions for the main page request
        print(f"An error occurred for the main page: {err}")

    return articles


# URL of the main news page to scrape (replace with a valid URL)
main_page_url = 'https://www.dawn.com/'  # Example URL for scraping

# Extract articles by following internal links
articles = extract_articles(main_page_url)

# Create a DataFrame to store the extracted articles
df = pd.DataFrame(articles)

# Save the DataFrame to a CSV file
df.to_csv('dawn_scrapper.csv', index=False)

# Display the DataFrame
print(df)

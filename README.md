# X_Scraper

X_Scraper is a Python module designed to scrape Twitter posts and images. It allows you to extract data from Twitter posts and download images with ease.

## Features

- **X_Image**: Scrape images from a given Twitter post.
- **X_Tweet**: Extract tweet text, metadata, and more from a Twitter post.

## Installation

You can install X_Scraper via pip:

```bash
pip install X_Scraper --upgrade(I messed up an initial version)


from X_Scraper import X_Image 
link = "https://x.com/ManagingBarca/status/1828366272951631892" 

image = X_Image(link)

image.get_X_Image()


from X_Scraper import X_Tweet

post = X_Tweet("https://x.com/AniNewsAndFacts/status/1828370987580104747/quotes")

post_description = post.get_X_Tweet()

print(f"Author @{post_description['Author']}")
print(f"Post @ {post_description['Post']}")

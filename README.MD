# CIBERSEC NEWS

> Cybersecurity news aggregator

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

## Index

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)

---

## Description

CIBERSEC NEWS is a cybersecurity news aggregator that collects information from multiple sites, filters by date, and generates reports in XLS format. It is designed to be **fast, efficient, and easy to use from the console**.

>This program was developed to automate the process of extracting cybersecurity news for the Cybersecurity Master's program.

---

## Features

- Extracts news from multiple RSS sources.  
- Filters news by a minimum publication date.  
- Generates XLS reports with a news summary.  
- Visual progress bar using `tqdm`.  
- Implements concurrency for faster news extraction.

---

## Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/[yourusername]/cibersec-news.git
cd cibersec-news
pip install -r requirements.txt
```

---

## Configuration

You can add new RSS sources for news extraction. To do this, edit the FeedJSON.json file located at:

```
/feed_json/feeds.json
```
Each entry in this file represents an RSS channel that the application processes to extract news and generate the XLS report.

**Example entry**
```json

{
        
    "site":"https://dominio.com/rss"
}
```
>**Important:**
> - Keep the established JSON structure or adapt the code to your needs.
> - Ensure that the URL is a **valid RSS feed**.
> - Save your changes and run the application again from the command line.
>- If a source does not provide news for the requested date, it will not be included in the report.
---

## Usage

Run the program from the console:

```bash
# Option A
# Option without param. By default get today to extract news
python .\cybersec_news.py 

# Option B 
# Option with dateStart param. DATE FORMAT --> DD/MM/YYYY
python cybersec_news.py --dateStart 20/10/2025 

```
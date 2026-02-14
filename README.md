# El País Opinion Scraper & Cross-Browser Analyzer

A robust Python-based automation tool that scrapes the latest opinion articles from El País, translates headers into English, and performs text analysis. This project demonstrates high-level proficiency in **Selenium**, **API Integration**, and **Parallel Cloud Testing** via BrowserStack.

## Features
- **Web Scraping:** Extracts the first 5 articles (titles and content) from the El País Opinion section.
- **Image Processing:** Automatically downloads and saves article cover images locally.
- **Translation:** Integrates with Google Translate (via `deep-translator`) to convert Spanish headers to English.
- **Word Analysis:** Analyzes translated headers to identify and count frequently repeated words.

## Tech Stack
- **Language:** Python 3.x
- **Automation Framework:** Selenium WebDriver
- **Cloud Testing:** BrowserStack
- **Translation API:** Deep Translator (Google Backend)
- **Concurrency:** Python Threading module
- **Environment Management:** Python-Dotenv

## Prerequisites
- Python installed on your machine.
- A BrowserStack account (Username and Access Key).

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/El-Pais-Web-Scraper.git](https://github.com/YOUR_USERNAME/El-Pais-Web-Scraper.git)
   cd El-Pais-Web-Scraper
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
3. **Configure Environment Variables:**
   - Create a .env file in the root directory and add your BrowserStack credentials:
   ```bash
   BS_USERNAME=your_username
   BS_ACCESS_KEY=your_access_key

## Usage

- To run the scraper locally:
  ```bash
  python scraper.py
- To run cross-browser tests on BrowserStack:
  ```bash
  python browserstack_run.py

#!/usr/bin/env python3
"""
scrape.py — URL/website content scraper
Uses newspaper3k for articles, firecrawl-py for complex/JS-heavy pages.

Usage:
  python3 tools/scrape.py <url>                    # auto-pick best method
  python3 tools/scrape.py <url> --method newspaper # force newspaper3k
  python3 tools/scrape.py <url> --method firecrawl # force firecrawl (needs API key)
  python3 tools/scrape.py <url> --output markdown  # output format (markdown|text|json)

Env:
  FIRECRAWL_API_KEY — required for firecrawl method (get free key at firecrawl.dev)
"""

import sys
import os
import argparse
import json

def scrape_newspaper(url):
    from newspaper import Article
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    return {
        "url": url,
        "method": "newspaper3k",
        "title": article.title,
        "authors": article.authors,
        "publish_date": str(article.publish_date) if article.publish_date else None,
        "text": article.text,
        "summary": article.summary,
        "keywords": article.keywords,
        "top_image": article.top_image,
    }

def scrape_firecrawl(url, output_format="markdown"):
    from firecrawl import FirecrawlApp
    api_key = os.environ.get("FIRECRAWL_API_KEY")
    if not api_key:
        raise ValueError("FIRECRAWL_API_KEY env var not set. Get a free key at https://firecrawl.dev")
    app = FirecrawlApp(api_key=api_key)
    result = app.scrape_url(url, formats=[output_format])
    return {
        "url": url,
        "method": "firecrawl",
        "markdown": result.markdown if hasattr(result, 'markdown') else str(result),
        "metadata": result.metadata if hasattr(result, 'metadata') else {},
    }

def auto_scrape(url, output_format="markdown"):
    """Try newspaper first (free/local), fall back to firecrawl if needed."""
    try:
        result = scrape_newspaper(url)
        if result["text"] and len(result["text"]) > 100:
            return result
        raise ValueError("Not enough content extracted")
    except Exception as e:
        print(f"[newspaper3k failed: {e}] Trying firecrawl...", file=sys.stderr)
        return scrape_firecrawl(url, output_format)

def main():
    parser = argparse.ArgumentParser(description="Scrape URL content for AI use")
    parser.add_argument("url", help="URL to scrape")
    parser.add_argument("--method", choices=["auto", "newspaper", "firecrawl"], default="auto")
    parser.add_argument("--output", choices=["markdown", "text", "json"], default="text")
    args = parser.parse_args()

    if args.method == "newspaper":
        result = scrape_newspaper(args.url)
    elif args.method == "firecrawl":
        result = scrape_firecrawl(args.url, args.output)
    else:
        result = auto_scrape(args.url, args.output)

    if args.output == "json":
        print(json.dumps(result, indent=2, default=str))
    elif args.output == "markdown" and "markdown" in result:
        print(result["markdown"])
    else:
        if result.get("title"):
            print(f"# {result['title']}\n")
        if result.get("authors"):
            print(f"Authors: {', '.join(result['authors'])}\n")
        if result.get("publish_date"):
            print(f"Published: {result['publish_date']}\n")
        if result.get("summary"):
            print(f"**Summary:** {result['summary']}\n")
        print(result.get("text", result.get("markdown", "No content")))

if __name__ == "__main__":
    main()

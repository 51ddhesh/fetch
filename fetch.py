#!/usr/bin/env python3
import argparse
import cloudscraper
from bs4 import BeautifulSoup
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('contest_id')
    parser.add_argument('problem_id')
    parser.add_argument('--mode', default='contest')
    args = parser.parse_args()

    # Construct URL
    base = "https://codeforces.com"
    if args.mode == 'contest':
        url = f"{base}/contest/{args.contest_id}/problem/{args.problem_id}"
    else:
        url = f"{base}/problemset/problem/{args.contest_id}/{args.problem_id}"

    print(f"Fetching {args.contest_id}{args.problem_id}...")

    # Fetch
    scraper = cloudscraper.create_scraper()
    try:
        resp = scraper.get(url)
        resp.raise_for_status()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Parse
    soup = BeautifulSoup(resp.text, 'html.parser')
    sample_test = soup.find('div', class_='sample-test')
    
    if not sample_test:
        print("No samples found.")
        sys.exit(1)

    inputs = sample_test.find_all('div', class_='input')
    outputs = sample_test.find_all('div', class_='output')

    # Helper to extract text preserving newlines
    def extract_cf_text(tag):
        pre = tag.find('pre')
        if not pre: return ""
        
        # Method 1: Check for div lines (New CF format)
        lines = pre.find_all('div')
        if lines:
            return '\n'.join(line.get_text().strip() for line in lines)
            
        # Method 2: Check for <br> (Old CF format)
        for br in pre.find_all('br'):
            br.replace_with('\n')
        return pre.get_text().strip()

    # Save
    for i, (inp, out) in enumerate(zip(inputs, outputs)):
        in_text = extract_cf_text(inp) + '\n'
        out_text = extract_cf_text(out) + '\n'

        # Determine filenames
        if i == 0:
            f_in, f_exp = "in.txt", "expected.txt"
        else:
            f_in, f_exp = f"in{i+1}.txt", f"expected{i+1}.txt"

        with open(f_in, 'w') as f: f.write(in_text)
        with open(f_exp, 'w') as f: f.write(out_text)
        
        print(f"Saved {f_in}")

if __name__ == "__main__":
    main()

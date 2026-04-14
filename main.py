#!/usr/bin/env python3
import sys
import os
import requests
import json


#API_URL = "https://is.gd/create.php"
#INPUT_FILENAME =  "urls.txt"
API_URL = os.environ.get("IS_GD_API_URL", "https://is.gd/create.php")
INPUT_FILENAME = os.environ.get("INPUT_FILENAME", "urls.txt")

#caching memory
url_cache = {}

def shorten_url(original_url):
    if original_url in url_cache:
       # print(f"-> Usando caché para: {original_url}", file=sys.stderr)
        return url_cache[original_url]

    try:
        params = {
            "format" : "json",
            "url" : original_url,
        }
        response = requests.get(API_URL, params=params)

        try:
            data = response.json()
        except json.JSONDecodeError:
            print(f"Error: the answer from is.gd for {original_url} is not a valid JSON", file=sys.stderr)
            return None
        if response.status_code == 200 and "shorturl" in data:
            short_url = data["shorturl"]
            url_cache[original_url] = short_url
            return short_url
        
        elif "errormessage" in data:
            error_code = data.get("errorcode", "unknown")
            error_msg = data.get("errormessage", "Error unknown")
            print(f"Error: API is.gd (code {error_code}) para {original_url}: {error_msg}", file=sys.stderr)
            if error_code == 3:
                print("-> rate limit exceeded, please wait one minute at least.", file=sys.stderr)
                
                
            return None
        else:
            
            print(f"Error HTTP {response.status_code} try to shorten {original_url}", file=sys.stderr)
            return None
    except requests.RequestException as e:
        print(f"Error: conection with is.gd to obtain {original_url}: {e}, file=sys.stderr")



def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_filepath = os.path.join(script_dir, INPUT_FILENAME)

    try:
        with open(input_filepath, "r", encoding='utf-8') as f:
            original_urls = [line.strip() for line in f if line.strip()]
            
    except FileNotFoundError:
        print(f"Error: input file not found '{input_filepath}'.", file=sys.stderr)
        sys.exit(1) 
    except Exception as e:
        print(f"Error: during the file reading: {e}", file=sys.stderr)
        sys.exit(1)

    for url in original_urls:
        short_url = shorten_url(url)
        if short_url:
            print(f"{short_url},{url}")
        else:
            print(f"Error:, {url}")


#print(shorten_url("https://www.rei.com/c/mountain-bike-helmets"))
#print(shorten_url("https://maps.google.co.uk/maps?f=q&source=s_q&hl=en&geocode=&q=louth&sll=53.800651,-4.064941&sspn=33.219383,38.803711&ie=UTF8&hq=&hnear=Louth,+United+Kingdom&ll=53.370272,-0.004034&spn=0.064883,0.075788&z=14"))
if __name__ == "__main__":
    main()
# main_file.py

import argparse
import random
from functions.search_jobs import search_job
from functions.search_products import search_product

def generate_random_job_search_phrase():
    job_search_phrases = ["Essay writing", "Personal statement", "Admission or application essay", "Ghost writing"]
    return random.choice(job_search_phrases)

def generate_random_product_search_phrase():
    product_search_phrases = ["Cooking Oil", "Smartphone", "Laptop", "Fitness Tracker"]
    return random.choice(product_search_phrases)

def print_jobs(query):
    job_search_results = search_job(query)
    for job in job_search_results:
        print(job)

def print_products(query):
    products_search_results = search_product(query)
    for product in products_search_results:
        print(product)

def main():
    parser = argparse.ArgumentParser(description="Search for jobs or products.")
    parser.add_argument('--jobs', action='store_true', help='Print job search results')
    parser.add_argument('--products', action='store_true', help='Print product search results')
    parser.add_argument('--query', type=str, help='Search query string')

    args = parser.parse_args()

    if args.query:
        query = args.query
    elif args.jobs:
        print("No search query provided for jobs. Generating a random job search phrase.")
        query = generate_random_job_search_phrase()
        print(f"Random job search phrase: \n{query}\n")
    elif args.products:
        print("No search query provided for products. Generating a random product search phrase.")
        query = generate_random_product_search_phrase()
        print(f"Random product search phrase: \n {query} \n")
    else:
        print("No search query provided. Generating a random search phrase.")
        query = generate_random_job_search_phrase() if random.choice([True, False]) else generate_random_product_search_phrase()
        print(f"Random search phrase: \n {query} \n")

    if args.jobs:
        print(f"\nPrinting job search results for: {query}")
        print_jobs(query)
    elif args.products:
        print(f"\nPrinting product search results for: {query}")
        print_products(query)
    else:
        print(f"\nPrinting product search results for: {query}")
        print_products(query)
        

if __name__ == "__main__":
    main()
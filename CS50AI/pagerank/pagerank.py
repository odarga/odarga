import os
from random import choice
import re
import sys
from numpy import random
from collections import Counter

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    # Next page probability distribution dictionary
    next_page_probability = {}
    # Calculating probability and writing it to dictionary for each page
    # If there is no outgoing links from current page
    if not corpus[page]:
        for webpage in corpus:
            next_page_probability[webpage] = 1 / len(corpus)
    # If there are outgoing links from current page
    else:
        for webpage in corpus:
            probability = (1 - damping_factor) / len(corpus)
            if webpage in corpus[page]:
                probability += damping_factor / len(corpus[page])
            next_page_probability[webpage] = probability
    # Returning the next page probability distribution dictionary
    return next_page_probability


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # Selecting a random page for first sample
    page = choice(list(corpus.keys()))
    # Writing first page to page array
    samples = [page]
    # n samples
    for i in range(1, n):
        # Getting next page probability distribution
        probability_distribution = transition_model(corpus, page, damping_factor)
        page_list = []
        probability_list = []
        for webpage in probability_distribution:
            page_list.append(webpage)
            probability_list.append(probability_distribution[webpage])
        # Random choice for next sample according to probability distribution
        next_page = random.choice(page_list, p = probability_list, size = 1)
        page = next_page[0]
        page_list.clear()
        probability_list.clear()
        samples.append(page)
    # Samples probability distribution dictionary
    samples_probability_distribution = {}
    for webpage in corpus:
            # Filling samples probability distribution dictionary
            samples_probability_distribution[webpage] = Counter(samples)[webpage] / n
    # Returning samples probability distribution dictionary
    return samples_probability_distribution


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # Iteration probability distribution dictionary
    iterations_probability_distribution = {}
    # Assigning same probability for each web page
    for webpage in corpus:
        iterations_probability_distribution[webpage] = 1 / len(corpus)
    changes = {}
    # Iterations
    while True:
        # Calculating new probability for every webpage
        for webpage in corpus:
            start = iterations_probability_distribution[webpage]
            iterations_probability_distribution[webpage] = (1 - damping_factor) / len(corpus)
            for other in corpus:
                if other != webpage and not corpus[other]:
                    iterations_probability_distribution[webpage] += damping_factor * iterations_probability_distribution[other] / len(corpus)
                elif other != webpage and webpage in corpus[other]:
                    iterations_probability_distribution[webpage] += damping_factor * iterations_probability_distribution[other] / len(corpus[other])
            end = iterations_probability_distribution[webpage]
            # Noting change
            changes[webpage] = abs(end - start)
        i = 0
        # Checking if all changes under 0.001
        for webpage in corpus:
            if changes[webpage] <= 0.001:
                i += 1
        if i == len(corpus):
            break
    # Returning iteration probability distribution dictionary
    return iterations_probability_distribution


if __name__ == "__main__":
    main()



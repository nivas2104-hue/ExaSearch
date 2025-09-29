from exa_py import Exa

exa = Exa('e88fa023-5f48-4869-bbcf-1d599f8ab8a5')
query = input('Search here: ')

response = exa.search(
    query,
    num_results=5,
    type='keyword',  # treat input like a keyword search
    include_domains=['https://www.instagram.com'],  # Instagram domain
)

for result in response.results:
    print(f'Title: {result.title}')
    print(f'URL: {result.url}')
    print()
    
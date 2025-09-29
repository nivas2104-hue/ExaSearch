from exa_py import Exa

exa = Exa('e88fa023-5f48-4869-bbcf-1d599f8ab8a5')

def fetch_by_platform(query, domain, num_results=3):
    results = exa.search(
        query,
        num_results=num_results,
        include_domains=[domain]
    )
    return results.results

def find_food():
    food = input("What food do you want? ").strip()
    area = input("Which area in Bangalore? (or press enter for anywhere): ").strip()
    
    query = f"best {food} {area + ' ' if area else ''}Bangalore restaurants"
    print(f"\n🔍 Searching for {food}...")

    zomato_results = fetch_by_platform(query, "zomato.com", 3)
    swiggy_results = fetch_by_platform(query, "swiggy.com", 3)
    insta_results = fetch_by_platform(query, "instagram.com", 3)


    combined_results = []
    for i in range(3):
        if i < len(zomato_results): combined_results.append(zomato_results[i])
        if i < len(swiggy_results): combined_results.append(swiggy_results[i])
        if i < len(insta_results): combined_results.append(insta_results[i])

    print(f"\n🍽️ Found {len(combined_results)} places (mixed platforms):")
    print("=" * 50)
    
    for i, place in enumerate(combined_results, 1):
        print(f"{i}. {place.title}")
        print(f"   🔗 {place.url}")
        
        if "zomato" in place.url:
            print("   📱 Platform: Zomato")
        elif "swiggy" in place.url:
            print("   📱 Platform: Swiggy")
        elif "instagram" in place.url:
            print("   📱 Platform: Instagram")
        else:
            print("   📱 Platform: Unknown")
        
        if hasattr(place, 'snippet') and place.snippet:
            print(f"   📝 {place.snippet}")
        print("-" * 50)

while True:
    find_food()
    again = input("Search again? (y/n): ").strip().lower()
    if again in ['n', 'no']:
        print("🍽️ Happy eating in Bangalore! 🎉")
        break

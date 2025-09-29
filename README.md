
# 🍽️ Food Finder with Exa (Custom Search Engine Project)

This repository demonstrates how I used the Exa API to first build a simple custom search engine and then extended it into a more practical project — a Food Finder that aggregates restaurant results from multiple platforms.

## 📌 Project Breakdown
### 1️⃣ Custom Search Engine (Base Project)

- File: basic_search.py
  
- Runs keyword-based searches using Exa API.

- Can filter results by a specific platform (e.g., Instagram).

- Demonstrates the core idea of building a custom search engine in Python.

### 2️⃣ Food Finder (Extension Project)

- File: food_finder.py

- Built on top of the base search engine.

- Lets users search for food in Bangalore.

- Pulls results from Zomato, Swiggy, and Instagram.

- Combines them into one mixed list with:

   1. 📌 Title

   2. 🔗 URL

   3. 📱 Platform (Zomato, Swiggy, Instagram)

   4. 📝 Snippet/Description

This shows how a basic tool can be extended into a real-world use case.



### 🚀 How to Run

Clone the repository:

``` bash  
git clone https://github.com/yourusername/food-finder-exa.git 

cd food-finder-exa
```
### Requirements

- Python 3.8+
- exa-py library  

Install using:  

```bash
pip install exa-py
```

Run the basic search engine:
``` bash
python basic.py
```

Run the food finder:
``` bash
python foodfinder.py
```

### 🛠️ Tech Stack

- Python

- Exa API (exa-py)

### 🔮 Future Improvements

- Add ⭐ ratings or scoring logic (if API data allows).

- Build a simple Flask/Django web app frontend.

- Deploy online so others can try it.

### 📖 Learning Outcome

This project shows how to:

- Work with APIs in Python.

- Create a custom search engine.

- Extend a base script into a practical application.
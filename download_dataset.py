import os
import requests
import time
import random

os.makedirs("dataset", exist_ok=True)

# 7 categories 
# 1. Eyes Closed
# 2. Blurry Photos
# 3. Smiled
# 4. Solo Portraits
# 5. Group Photos
# 6. Photos with No Human
# 7. Animals

# Mapping categories to search terms for LoremFlickr
categories = {
    "eyes_closed": "sleeping,face,closed_eyes",
    "blurry": "motion_blur,out_of_focus,blur",
    "smiled": "smile,happy,laughing,face",
    "solo": "portrait,face,single,person",
    "group": "group,people,friends,team",
    "no_human": "landscape,nature,city,food",
    "animals": "dog,cat,wildlife,pet,animal"
}

count = 0
images_per_category = 5  

print(f"Downloading {len(categories) * images_per_category} images from LoremFlickr...")

for tag, query in categories.items():
    print(f"Processing category: {tag}")
    
    for i in range(images_per_category):
        try:

            url = f"https://loremflickr.com/400/400/{query}?lock={count}"
            
            response = requests.get(url, timeout=10, allow_redirects=True)
            
            if response.status_code == 200:
                filename = f"dataset/img_{count}.jpg"
                with open(filename, "wb") as f:
                    f.write(response.content)
                print(f"  Downloaded {tag} ({i+1}/{images_per_category}): {filename}")
                count += 1
            else:
                print(f"  Failed to download for {tag}: Status {response.status_code}")
            
            # adding sleep time, to avooid blocking by the server 
            # thinking this is a bot
            time.sleep(1)
            
        except Exception as e:
            print(f"  Error downloading {tag}: {e}")

print(f"\n Dataset created successfully inside dataset/ with {count} images.")

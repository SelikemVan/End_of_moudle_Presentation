print("Welcome to Seli's virtual shopping mall!")


def create_product(name, price, description):
    product = {
        "name": name,
        "price": price,
        "description": description
    }
    return product


# Function to display product information
def display_product(product):
    price_formatted = "${}".format(product['price'])
    print("{} - {}".format(product['name'], price_formatted))
    print(product['description'])
    print()


# Create products in the Electronics category
electronics = [
    {"name": "Smartphone", "price": 699.99, "description": "A high-end smartphone with advanced features."},
    {"name": "Laptop", "price": 1099.99, "description": "Powerful laptop for both work and entertainment."},
    {"name": "Headphones", "price": 149.99, "description": "Noise-canceling headphones for immersive audio."},
    {"name": "Tablet", "price": 399.99, "description": "Compact tablet for easy on-the-go use."},
    {"name": "Camera", "price": 599.99, "description": "Professional-grade camera for stunning photos."},
    {"name": "Smart Watch", "price": 249.99, "description": "Stay connected with this feature-packed smartwatch."},
    {"name": "Gaming Console", "price": 499.99, "description": "Next-gen gaming console for immersive experiences."},
    {"name": "Wireless Speaker", "price": 79.99, "description": "Portable wireless speaker with high-quality sound."},
    {"name": "Monitor", "price": 299.99, "description": "High-resolution monitor for improved productivity."},
    {"name": "VR Headset", "price": 349.99, "description": "Virtual reality headset for immersive entertainment."},
    {"name": "Robot Vacuum", "price": 199.99, "description": "Efficient robot vacuum for automated cleaning."},
    {"name": "Fitness Tracker", "price": 89.99, "description": "Track your fitness goals with this smart tracker."},
    {"name": "Bluetooth Earbuds", "price": 129.99, "description": "Wireless earbuds with crystal-clear audio."},
    {"name": "Drone", "price": 299.99, "description": "Capture stunning aerial shots with this drone."},
    {"name": "Smart Thermostat", "price": 149.99, "description": "Energy-saving smart thermostat for your home."}
]

# Create products in the Clothing category
clothing = [
    {"name": "T-Shirt", "price": 19.99, "description": "Comfortable cotton t-shirt for everyday wear."},
    {"name": "Jeans", "price": 49.99, "description": "Classic denim jeans for a stylish look."},
    {"name": "Sweater", "price": 39.99, "description": "Warm and cozy sweater for colder days."},
    {"name": "Sneakers", "price": 79.99, "description": "Stylish sneakers for casual outings."},
    {"name": "Dress Shirt", "price": 49.99, "description": "Formal dress shirt for special occasions."},
    {"name": "Skirt", "price": 29.99, "description": "Elegant skirt for a sophisticated look."},
    {"name": "Jacket", "price": 89.99, "description": "Warm and stylish jacket for colder weather."},
    {"name": "Sweater", "price": 59.99, "description": "Cozy sweater to keep you comfortable."},
    {"name": "Athletic Shorts", "price": 24.99, "description": "Breathable shorts for your workout sessions."},
    {"name": "Dress", "price": 69.99, "description": "Chic dress for formal events and parties."},
    {"name": "Hoodie", "price": 39.99, "description": "Casual hoodie for a relaxed look."},
    {"name": "Blouse", "price": 34.99, "description": "Lightweight blouse for a stylish ensemble."},
    {"name": "Pants", "price": 49.99, "description": "Versatile pants suitable for various occasions."},
    {"name": "Hat", "price": 19.99, "description": "Stylish hat to complete your outfit."},
    {"name": "Gloves", "price": 14.99, "description": "Warm gloves for chilly days."},
    {"name": "Swimsuit", "price": 29.99, "description": "Fashionable swimsuit for a day at the beach."}
]

home_decor = [
    {"name": "Throw Pillow", "price": 19.99, "description": "Decorative throw pillow for your couch."},
    {"name": "Wall Art", "price": 49.99, "description": "Beautiful artwork to adorn your walls."},
    {"name": "Candle Holder", "price": 29.99, "description": "Elegant candle holder for ambient lighting."},
    {"name": "Table Lamp", "price": 39.99, "description": "Stylish table lamp to brighten up your space."},
    {"name": "Rug", "price": 89.99, "description": "Soft and cozy rug to add warmth to your room."},
    {"name": "Vase", "price": 24.99, "description": "Artistic vase for displaying flowers or decorative items."},
    {"name": "Clock", "price": 34.99, "description": "Functional and decorative wall clock."},
    {"name": "Picture Frame", "price": 14.99, "description": "Frame your cherished memories with this picture frame."},
    {"name": "Curtains", "price": 49.99, "description": "Elegant curtains to enhance your windows."},
    {"name": "Mirror", "price": 59.99, "description": "Stylish mirror to open up your space."},
    {"name": "Bookshelf", "price": 79.99, "description": "Versatile bookshelf for organizing your books and items."},
    {"name": "Plant Stand", "price": 29.99, "description": "Sturdy plant stand for showcasing your indoor plants."},
    {"name": "Cushion Cover", "price": 12.99, "description": "Cover for your cushions, available in various designs."},
    {"name": "Coasters", "price": 9.99, "description": "Set of coasters to protect your surfaces in style."},
    {"name": "Decorative Bowl", "price": 19.99, "description": "Artistic bowl for holding small items."}
]

furniture = [
    {"name": "Sofa", "price": 499.99, "description": "Comfortable sofa for your living room."},
    {"name": "Dining Table", "price": 299.99, "description": "Sturdy dining table for family gatherings."},
    {"name": "Bed Frame", "price": 399.99, "description": "Elegant bed frame for a restful sleep."},
    {"name": "Coffee Table", "price": 149.99, "description": "Stylish coffee table to complement your seating area."},
    {"name": "Bookshelf", "price": 199.99, "description": "Spacious bookshelf for storing your books and decor."},
    {"name": "Wardrobe", "price": 349.99, "description": "Spacious wardrobe for organizing your clothes."},
    {"name": "Desk", "price": 229.99, "description": "Functional desk for productive work sessions."},
    {"name": "Dresser", "price": 279.99, "description": "Dresser with ample storage for your belongings."},
    {"name": "Nightstand", "price": 89.99, "description": "Convenient nightstand for your bedside essentials."},
    {"name": "Recliner Chair", "price": 299.99, "description": "Plush recliner chair for ultimate relaxation."},
    {"name": "Sectional Sofa", "price":  899.99, "description": "Modular sectional sofa for versatile seating."},
    {"name": "Bar Stool", "price": 49.99, "description": "Sleek bar stool for your kitchen counter."},
    {"name": "Chest of Drawers", "price": 199.99, "description": "Chest of drawers for additional storage space."},
    {"name": "Console Table", "price": 159.99, "description": "Elegant console table for your hallway."},
    {"name": "TV Stand", "price": 179.99, "description": "Sturdy TV stand for your entertainment center."}
]

# Display products in the Electronics category
print("Electronics:")
for product in electronics:
    display_product(product)

# Display products in the Clothing category
print("Clothing:")
for product in clothing:
    display_product(product)

print("home_decor")
for product in home_decor:
    display_product(product)

print("furniture")
for product in furniture:
    display_product(product)

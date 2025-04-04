Creating a simple trip-planner program involves taking user input for preferences and constraints, then generating a potential itinerary based on these inputs. This is a basic example, which could be expanded with more sophisticated logic or integrations with travel APIs. Here's a simple version with comments and error handling:

```python
import random

# Sample data for destinations, activities, and restaurants
destinations = {
    "New York": {
        "activities": ["Statue of Liberty", "Broadway Show", "Central Park"],
        "restaurants": ["Joe's Pizza", "Shake Shack", "Balthazar"]
    },
    "Paris": {
        "activities": ["Eiffel Tower", "Louvre Museum", "Seine River Cruise"],
        "restaurants": ["Le Meurice", "Cafe de Flore", "L'Astrance"]
    },
    "Tokyo": {
        "activities": ["Shinjuku Gyoen", "Senso-ji Temple", "Akihabara"],
        "restaurants": ["Sushi Saito", "Ichiran Ramen", "Gonpachi"]
    }
}

def get_user_preferences():
    """Get travel preferences from the user."""
    try:
        name = input("Hi, what's your name? ")
        budget = float(input("What is your budget for the trip (in USD)? "))
        duration = int(input("How many days do you plan to travel? "))
        preferred_destination = input("Which city would you like to visit (New York, Paris, Tokyo)? ")
        if preferred_destination not in destinations:
            raise ValueError("Destination not available. Please choose from New York, Paris, or Tokyo.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None
    return {
        "name": name,
        "budget": budget,
        "duration": duration,
        "destination": preferred_destination
    }

def plan_trip(preferences):
    """Generate a travel itinerary based on user preferences."""
    destination = preferences['destination']

    if destination not in destinations:
        print(f"Sorry, {destination} is not available.")
        return None
    
    itinerary = {
        "destination": destination,
        "activities": [],
        "restaurants": []
    }

    # Randomly select activities and restaurants
    available_activities = destinations[destination]["activities"]
    available_restaurants = destinations[destination]["restaurants"]

    num_activities = min(len(available_activities), preferences['duration'])
    num_restaurants = min(len(available_restaurants), preferences['duration'])

    try:
        itinerary["activities"] = random.sample(available_activities, num_activities)
        itinerary["restaurants"] = random.sample(available_restaurants, num_restaurants)
    except ValueError as e:
        print(f"Error in generating itinerary: {e}")
        return None

    return itinerary

def display_itinerary(itinerary, preferences):
    """Display the itinerary to the user."""
    if not itinerary:
        print("No itinerary available.")
        return
    
    print(f"\nHello {preferences['name']}! Here is your trip itinerary to {itinerary['destination']}:\n")
    print("Activities:")
    for activity in itinerary["activities"]:
        print(f"- {activity}")

    print("\nRestaurants:")
    for restaurant in itinerary["restaurants"]:
        print(f"- {restaurant}")

def main():
    """Main function to run the trip planner."""
    preferences = get_user_preferences()
    if not preferences:
        return

    itinerary = plan_trip(preferences)
    display_itinerary(itinerary, preferences)

if __name__ == "__main__":
    main()
```

### Explanation:
1. **Data Structure**: The program uses a dictionary to store data about available destinations, along with possible activities and restaurants in those destinations.

2. **User Input**: The `get_user_preferences` function collects data from the user, including the traveler's name, budget, trip duration, and preferred destination.

3. **Trip Planning**: Based on the user's preferences, the `plan_trip` function generates a random itinerary by selecting activities and restaurants. It uses Python's `random.sample` to ensure unique picks.

4. **Error Handling**: The program includes error handling for invalid inputs and other potential issues, such as attempts to select more activities than available.

5. **Display**: The `display_itinerary` function neatly outputs the generated itinerary to the user.

This basic template can be adapted and extended to include more sophisticated features and error handling, such as integrating with live APIs for up-to-date information about flights, hotels, and local events.
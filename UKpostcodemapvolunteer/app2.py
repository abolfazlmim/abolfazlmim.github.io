from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import folium

def get_coordinates(postcode):
    """Get latitude and longitude for a given postcode."""
    geolocator = Nominatim(user_agent="postcode_distance_calculator")
    location = geolocator.geocode(postcode)
    if location:
        return (location.latitude, location.longitude)
    else:
        raise ValueError(f"Could not find coordinates for postcode: {postcode}")

def find_nearest_volunteers(request_postcode, volunteer_postcodes, max_results=5):
    """Find the nearest volunteers to the requester's postcode."""
    request_coords = get_coordinates(request_postcode)
    distances = []

    for postcode in volunteer_postcodes:
        try:
            volunteer_coords = get_coordinates(postcode)
            distance = geodesic(request_coords, volunteer_coords).miles
            distances.append((postcode, distance, volunteer_coords))
        except ValueError as e:
            print(e)

    # Sort by distance (closest first)
    distances.sort(key=lambda x: x[1])

    # Limit to the top results
    return request_coords, distances[:max_results]

def create_map(request_coords, sorted_distances):
    """Create a map with the requester and volunteer postcodes marked."""
    # Initialize the map centered at the requester's location
    m = folium.Map(location=request_coords, zoom_start=10)

    # Add a marker for the requester
    folium.Marker(
        location=request_coords,
        popup="Requester Location",
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)

    # Add markers for each volunteer
    for postcode, distance, coords in sorted_distances:
        folium.Marker(
            location=coords,
            popup=f"{postcode}: {distance:.2f} miles",
            icon=folium.Icon(color="blue")
        ).add_to(m)

    return m

def main():
    volunteer_postcodes = [
        "BD15 7QU", "BD8 9BN", "BD2 1FT", "BD2 1QG"
    ]  # Example volunteer postcodes

    request_postcode = input("Enter the requester's postcode: ").strip()

    print("Finding the nearest volunteers...")
    try:
        request_coords, sorted_distances = find_nearest_volunteers(request_postcode, volunteer_postcodes)

        print("\nNearest Volunteers:")
        for postcode, distance, _ in sorted_distances:
            print(f"{postcode}: {distance:.2f} miles")

        # Create the map
        print("\nGenerating the map...")
        help_map = create_map(request_coords, sorted_distances)

        # Save the map to an HTML file
        help_map.save("nearest_volunteers_map.html")
        print("Map saved as 'nearest_volunteers_map.html'")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

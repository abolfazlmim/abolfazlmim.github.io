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

def calculate_distances(office_postcode, volunteer_postcodes):
    """Calculate distances from the office postcode to each volunteer postcode."""
    office_coords = get_coordinates(office_postcode)
    distances = []

    for postcode in volunteer_postcodes:
        try:
            volunteer_coords = get_coordinates(postcode)
            distance = geodesic(office_coords, volunteer_coords).miles
            distances.append((postcode, distance, volunteer_coords))
        except ValueError as e:
            print(e)

    # Sort by distance (closest first)
    distances.sort(key=lambda x: x[1])
    return office_coords, distances

def create_map(office_coords, sorted_distances):
    """Create a map with the office and volunteer postcodes marked."""
    # Initialize the map centered at the office location
    m = folium.Map(location=office_coords, zoom_start=10)

    # Add a marker for the office
    folium.Marker(
        location=office_coords,
        popup="Office Location",
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
    office_postcode = "BD9 6RJ"  # Example office postcode - Duckworth Ln, Bradford BD9 6RJ
    volunteer_postcodes = [
        "BD15 7QU", "BD8 9BN", "BD2 1FT", "BD2 1QG"
    ]  # Example volunteer postcodes

    print(f"Office Postcode Bradford Royal Infirmy: {office_postcode}")
    print("Calculating distances...")
    
    office_coords, sorted_distances = calculate_distances(office_postcode, volunteer_postcodes)

    print("\nVolunteers sorted by distance:")
    for postcode, distance, _ in sorted_distances:
        print(f"{postcode}: {distance:.2f} miles")

    # Create the map
    print("\nGenerating the map...")
    volunteer_map = create_map(office_coords, sorted_distances)

    # Save the map to an HTML file
    volunteer_map.save("volunteer_map.html")
    print("Map saved as 'volunteer_map.html'")

if __name__ == "__main__":
    main()

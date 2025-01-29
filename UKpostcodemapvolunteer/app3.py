from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import folium
from folium.plugins import MarkerCluster

def get_coordinates(postcode):
    """Get latitude and longitude for a given postcode."""
    geolocator = Nominatim(user_agent="postcode_distance_calculator")
    location = geolocator.geocode(postcode)
    if location:
        return (location.latitude, location.longitude)
    else:
        raise ValueError(f"Could not find coordinates for postcode: {postcode}")

def calculate_all_distances(request_postcode, volunteer_postcodes):
    """Calculate distances from the request postcode to each volunteer postcode."""
    request_coords = get_coordinates(request_postcode)
    distances = []

    for postcode in volunteer_postcodes:
        try:
            volunteer_coords = get_coordinates(postcode)
            distance = geodesic(request_coords, volunteer_coords).miles
            distances.append((postcode, distance, volunteer_coords))
        except ValueError as e:
            print(e)

    # Sort by distance
    distances.sort(key=lambda x: x[1])
    return request_coords, distances

def get_marker_color(distance):
    """Return a marker color based on distance ranges."""
    if distance <= 2:
        return "green"
    elif distance <= 7:
        return "orange"
    else:
        return "red"

def create_map(request_coords, distances):
    """Create a map with the requester and all volunteer postcodes marked."""
    # Initialize the map centered at the requester's location
    m = folium.Map(location=request_coords, zoom_start=10)

    # Add a marker for the requester
    folium.Marker(
        location=request_coords,
        popup="Requester Location for Help ",
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)

    # Initialize marker clustering
    marker_cluster = MarkerCluster().add_to(m)

    # Add markers for all volunteers with color-coded distances
    for postcode, distance, coords in distances:
        color = get_marker_color(distance)
        folium.Marker(
            location=coords,
            popup=f"{postcode}: {distance:.2f} miles from main Location ",
            icon=folium.Icon(color=color)
        ).add_to(marker_cluster)

    return m

def main():
    volunteer_postcodes = [
        "BD15 7QU", "BD8 9BN", "BD2 1FT", "BD2 1QG"
    ]  # Example volunteer postcodes

    request_postcode = input("Enter the requester's postcode: ").strip()

    print("Calculating distances to all volunteers...")
    try:
        request_coords, distances = calculate_all_distances(request_postcode, volunteer_postcodes)

        print("\nAll Volunteers:")
        for postcode, distance, _ in distances:
            print(f"{postcode}: {distance:.2f} miles")

        # Create the map
        print("\nGenerating the map...")
        volunteer_map = create_map(request_coords, distances)

        # Save the map to an HTML file
        volunteer_map.save("all_volunteers_map.html")
        print("Map saved as 'all_volunteers_map.html'")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

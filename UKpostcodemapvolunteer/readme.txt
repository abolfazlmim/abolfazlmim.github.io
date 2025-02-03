Problem & Solution: Volunteer Locator for Request Assistance
Problem Statement
Organizations that rely on volunteers often need to quickly identify the nearest available volunteer when a request for assistance is received. Manually checking distances between postcodes can be inefficient and time-consuming. The challenge is to:

✅ Find the closest volunteers based on the requester’s postcode.
✅ Display this information visually on a map for quick decision-making.
✅ Provide an interactive, user-friendly interface to input postcodes and get results instantly.
✅ Show a sortable table of distances for easy reference.

Solution
We developed a web-based application using JavaScript, HTML, and Leaflet.js that allows users to:

1️⃣ Input a requester's postcode and a list of volunteer postcodes.
2️⃣ Automatically retrieve GPS coordinates using the Nominatim API.
3️⃣ Calculate distances between the requester and each volunteer.
4️⃣ Sort volunteers by distance (closest at the top).
5️⃣ Show all locations on an interactive map, with:

Requester in red
Volunteers in green, orange, or red (color-coded based on distance).
6️⃣ Display a table above the map listing volunteers and their exact distances.
How It Works
💡 Geocoding: Converts postcodes to GPS coordinates using the Nominatim API.
💡 Haversine Formula: Computes distances between locations.
💡 Leaflet.js Map: Dynamically plots all locations and updates with new searches.
💡 User Interaction: Simple input fields for postcodes, a "Generate Map" button, and a clear results table.

Impact & Benefits
🚀 Fast decision-making – Easily find the nearest volunteer in seconds.
📍 Real-time visualization – No need for manual distance calculations.
🎨 User-friendly UI – Simple inputs, interactive maps, and color-coded results.

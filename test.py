import requests

def print_grid_from_url(url):
    # Step 1: Fetch the content from the URL
    response = requests.get(url)
    response.raise_for_status()
    text = response.text
    
    # Step 2: Parse the data
    lines = text.splitlines()
    coordinates = []
    
    # Find the table section and extract rows
    in_table = False
    for line in lines:
        if "x-coordinate" in line:
            in_table = True
            continue
        if in_table:
            if not line.strip():
                break  # Exit table section
            row = line.split()
            if len(row) == 3:  # Expecting [x, character, y]
                x, char, y = row
                coordinates.append((int(x), char, int(y)))
    
    # Step 3: Determine grid size
    if not coordinates:
        print("No coordinates found in the document.")
        return
    
    max_x = max(coord[0] for coord in coordinates)
    max_y = max(coord[2] for coord in coordinates)
    
    # Create an empty grid
    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    
    # Fill the grid with characters
    for x, char, y in coordinates:
        grid[y][x] = char
    
    # Step 4: Print the grid
    for row in grid:
        print("".join(row))

# Example usage
url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
print_grid_from_url(url)

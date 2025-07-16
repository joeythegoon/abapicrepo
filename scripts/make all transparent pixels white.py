from PIL import Image
import os
from collections import deque

def remove_edge_white_background(folder_path, tolerance=10):
    def is_white(pixel):
        r, g, b, a = pixel
        return (
            abs(r - 255) <= tolerance and
            abs(g - 255) <= tolerance and
            abs(b - 255) <= tolerance
        )

    def flood_fill_transparency(image, tolerance):
        pixels = image.load()
        width, height = image.size
        visited = set()
        queue = deque()

        # Start from all four corners
        corners = [(0, 0), (width - 1, 0), (0, height - 1), (width - 1, height - 1)]
        for x, y in corners:
            queue.append((x, y))
            visited.add((x, y))

        while queue:
            x, y = queue.popleft()
            if not (0 <= x < width and 0 <= y < height):
                continue
            if not is_white(pixels[x, y]):
                continue

            pixels[x, y] = (255, 255, 255, 0)  # Make pixel transparent

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if (nx, ny) not in visited and 0 <= nx < width and 0 <= ny < height:
                    queue.append((nx, ny))
                    visited.add((nx, ny))

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.tiff', '.webp')):
            path = os.path.join(folder_path, filename)
            image = Image.open(path).convert('RGBA')
            flood_fill_transparency(image, tolerance)
            image.save(path)
            print(f"Processed (edge white removed): {filename}")

# Example usage
folder = r"C:\Users\vent1\OneDrive\Desktop\New folder (3)\Battlers\Transfers"
remove_edge_white_background(folder, tolerance=10)

import os
import requests
from urllib.parse import urlparse

def fetch_image(url):
    """
    Fetches an image from the given URL and saves it to the Fetched_Images directory.

    Parameters
    ----------
    url : str
        The URL of the image to fetch

    Returns
    -------
    None
    """

    try:
        # Send HTTP GET request to fetch the image
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Extract the image filename from the URL or use a default name
            filename = urlparse(url).path.split("/")[-1] or "downloaded_image.jpg"

            # Create the Fetched_Images directory if it doesn't exist
            os.makedirs("Fetched_Images", exist_ok=True)

            # Create the file path
            file_path = os.path.join("Fetched_Images", filename)

            # Save the image to the specified directory in binary mode
            with open(file_path, "wb") as file:
                file.write(response.content)

            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {file_path}")
            print("\nConnection strengthened. Community enriched.")
        else:
            print(f"Error: Unable to fetch the image. HTTP Status Code: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error: An error occurred while trying to fetch the image. Details: {e}")

def main():
    """
    Runs the Ubuntu Image Fetcher script.

    This function prompts the user for the URL of the image to fetch, 
    calls the fetch_image function to download the image, and prints out 
    a success message if the image is successfully fetched.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Prompt the user for the image URL
    image_url = input("Please enter the image URL: ")
    
    # Call the fetch_image function
    fetch_image(image_url)

if __name__ == "__main__":
    main()

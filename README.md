Ubuntu Image Fetcher
====================

The **Ubuntu Image Fetcher** is a Python tool that fetches images from the web, saves them locally, and organizes them for later use, following the principles of **Ubuntu** — community, respect, and sharing.
Features

--------

* Downloads images from any URL

* Creates a `Fetched_Images` directory automatically

* Handles errors gracefully

Requirements
------------

* Python 3.x

* `requests` library

Installation
------------

1. Clone the repo:
   git clone https://github.com/edmondweb/Ubuntu-Requests.git
   cd ubuntu-image-fetcher

2. Install dependencies:
   pip install requests
   
   Usage
   -----
   
   Run the script and enter the image URL when prompted:
   
   python image_fetcher.py
   
   **Example**
   
   Please enter the image URL: https://www.pexels.com/photo/water-falls-1009136/
   ✓ Successfully fetched: water-falls-1009136.jpg
   ✓ Image saved to Fetched_Images/water-falls-1009136.jpg

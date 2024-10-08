# Inspector Image

## Objective

The **Inspector Image** project aims to analyze images passively by extracting hidden information, including PGP keys and geolocation data. The project utilizes concepts from image recognition, steganography, and metadata analysis.

## Features

- Extract PGP keys hidden within the image.
- Retrieve geolocation data (latitude and longitude) from image metadata.

## Prerequisites

- Python 3.x
  
## Installation

1. Clone this repository:

   ```bash
   git clone https://01.kood.tech/git/mkuzmina/inspector-image.git
   cd inspector-image
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Extract Geolocation

To extract the latitude and longitude from an image:

```bash
python3 image.py -map image.jpeg
```

**Example Output:**

```bash
Lat/Lon: (13.731) / (-1.1373)
```

### Extract PGP Key

To extract the hidden PGP key from the image:

```bash
python3 image.py -steg image.jpeg
```

**Example Output:**

```bash
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: 01
...
-----END PGP PUBLIC KEY BLOCK-----
```

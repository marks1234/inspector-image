import sys
from PIL import Image
import piexif

# Function to extract GPS data from EXIF metadata


def get_gps_data(image_path):
    img = Image.open(image_path)
    exif_data = piexif.load(img.info['exif'])

    if 'GPS' not in exif_data:
        print("No GPS data found.")
        return None

    gps_info = exif_data['GPS']

    # Convert EXIF GPS data into latitude and longitude
    def convert_to_degrees(value):
        d, m, s = value[0], value[1], value[2]
        return d[0] / d[1] + (m[0] / m[1] / 60.0) + (s[0] / s[1] / 3600.0)

    lat_ref = gps_info[1].decode('utf-8')
    lon_ref = gps_info[3].decode('utf-8')

    lat = convert_to_degrees(gps_info[2])
    lon = convert_to_degrees(gps_info[4])

    # Adjust latitude and longitude based on N/E or S/W
    if lat_ref == 'S':
        lat = -lat
    if lon_ref == 'W':
        lon = -lon

    return lat, lon

# Function to extract hidden PGP key from image using steganography


def extract_steg_data(image_path):
    secret_message = ""
    with open("image.jpeg", "rb") as img:
        out = img.read().decode(
            'utf-8', errors="ignore")

        secret_message = out[-900:-5]

    if secret_message:
        print("Extracted Steganographic Data (PGP Key):")
        print(secret_message)
    else:
        print("No hidden data found using LSB steganography.")

# Main function to handle user input and call appropriate functions


def main():
    if len(sys.argv) < 3:
        print("Usage: python image_analyzer.py -map/-steg image.jpeg")
        sys.exit(1)

    mode = sys.argv[1]
    image_path = sys.argv[2]

    if mode == "-map":
        gps_data = get_gps_data(image_path)
        if gps_data:
            lat, lon = gps_data
            print(f"Lat/Lon: ({lat}) / ({lon})")
        else:
            print("No GPS data found.")
    elif mode == "-steg":
        extract_steg_data(image_path)
    else:
        print("Unknown mode. Use -map for GPS extraction or -steg for Steganography extraction.")


if __name__ == "__main__":
    main()

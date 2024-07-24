import time
import board
import terminalio
from adafruit_matrixportal.matrixportal import MatrixPortal
from adafruit_display_text import label
import displayio

BOT_TOKEN = "XXXXXXXXXX:THERESTOFYOURTOKEN"

matrixportal = MatrixPortal(status_neopixel=board.NEOPIXEL, debug=True)

# Setup display
matrixportal.display.brightness = 0.5
matrixportal.display.auto_refresh = False

# Create a text label
text_area = label.Label(terminalio.FONT, text="MatrixPortal Telegram Scroller", color=0xFF0000)
text_area.x = matrixportal.display.width
text_area.y = matrixportal.display.height // 2

# Create a Group to hold the text
text_group = displayio.Group()
text_group.append(text_area)

# Add the Group to the Display
matrixportal.display.root_group = text_group

# Connect to Wi-Fi
print("Connecting to Wi-Fi...")
matrixportal.network.connect()
print("Connected to Wi-Fi!")

# Setup the requests module using the matrixportal network
requests = matrixportal.network._wifi.requests

# Setup Telegram API
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"

# Function to get the latest message from Telegram
def get_latest_message():
    response = requests.get(TELEGRAM_API_URL)
    messages = response.json()["result"]
    if messages:
        latest_message = messages[-1]
        return latest_message["message"]["text"]
    return None

# Variables for text scrolling
scroll_speed = 0.03
scroll_direction = -1
text_x = matrixportal.display.width
font_height = terminalio.FONT.get_bounding_box()[1]

while True:
    # Scroll text
    text_x += scroll_direction
    text_area.x = text_x
    matrixportal.display.refresh()

    # Check if the text has scrolled off screen
    if text_x < -text_area.bounding_box[2]:
        text_x = matrixportal.display.width
        new_message = get_latest_message()
        if new_message:
            text_area.text = new_message

    time.sleep(scroll_speed)
MatrixPortal Telegram Scroller
==============================

Adafruit MatrixPortal M4 project to display scrolling text on an LED matrix with messages fetched from a Telegram bot, written in CircuitPython.

.. raw:: html

   <div align="center">
       <img src="https://github.com/Fr4nkFletcher/MatrixPortal_Telegram_Scroller/blob/main/demo.gif" alt="Scrolling text on LED matrix">
   </div>
  

Overview
--------

This project uses the Adafruit MatrixPortal M4 to display scrolling text on a 64x32 RGB LED matrix. The text messages are fetched from a Telegram bot, allowing for dynamic updates to the displayed message.

.. image:: https://cdn-learn.adafruit.com/assets/assets/000/111/881/original/led_matrices_Adafruit_MatrixPortal_M4_Pinout.png?1653078587
   :alt: Scrolling text on LED matrix
   :align: center

Hardware Required
-----------------

- Adafruit MatrixPortal M4
- 64x32 RGB LED Matrix (HUB75 display used in this project)
- Wi-Fi with internet access

Getting Started
---------------

Hardware Setup
~~~~~~~~~~~~~~

1. Connect the Adafruit MatrixPortal M4 to the 64x32 RGB LED matrix.
2. Power the MatrixPortal M4 using a USB-C cable connected to your computer or a power source.

Software Setup
~~~~~~~~~~~~~~

1. Install `CircuitPython <https://circuitpython.org/board/matrixportal_m4/>`_ on the MatrixPortal M4.
2. Download the required CircuitPython libraries from the `Adafruit CircuitPython Bundle <https://circuitpython.org/libraries>`_ and copy them to the ``lib`` folder on your MatrixPortal M4. (all needed libraries included in this repo)
3. Create a ``settings.toml`` file in the root of your CIRCUITPY drive with your Wi-Fi credentials:

   .. code-block:: toml

      CIRCUITPY_WIFI_SSID = "YOUR_SSID"
      CIRCUITPY_WIFI_PASSWORD = "YOUR_PASSWORD"

Setting Up Telegram
~~~~~~~~~~~~~~~

These are the steps you need to get a bot token to use in your project:

1. Install Telegram from your phone's app store (you may need to set up the account on your phone initially). Once logged in, you can install the desktop versions or use the Telegram web interface.
2. Inside Telegram, search for a user called "botfather" and open a chat.
3. Click the "/newbot" option or type that message in (exactly as shown).
4. Follow the on-screen instructions to create your bot.
5. You will receive a message with the token. Copy this token into your code.
6. Click the link at the top of the message to open the chat with the new bot. There will be a "/start" button, click that to activate the bot.

Code Deployment
~~~~~~~~~~~~~~~

1. Copy the ``code.py`` file to the root directory of your CIRCUITPY drive.

Usage
-----

1. Power on the MatrixPortal M4.
2. The device will connect to the specified Wi-Fi network.
3. The latest message from the Telegram bot will be displayed as scrolling text on the LED matrix.

License
-------

This project is licensed under the MIT License - see the `LICENSE <LICENSE>`_ file for details.

Acknowledgments
---------------

- `Adafruit <https://www.adafruit.com/>`_ for providing the hardware and libraries.
- `CircuitPython <https://circuitpython.org/>`_ community for their support and development tools.
- `Brian Lough <https://github.com/witnessmenow>`_ for inspiration from his `ScrollingLedMatrixTelegram <https://github.com/witnessmenow/ScrollingLEDMatrixTelegram>`_ repo.

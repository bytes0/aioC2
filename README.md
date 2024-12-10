
# aioc2

aioc2 is a cybersecurity project that implements a Command and Control (C2) system using aiogram, a powerful and asynchronous Telegram bot framework for Python. This project demonstrates the flexibility and potential of leveraging Telegram as a C2 communication platform for security research and ethical penetration testing purposes.

---

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Asynchronous Architecture**: Built using aiogram to ensure non-blocking, efficient communication.
- **Modular Design**: Easy to extend and customize for specific C2 needs.
- **Secure Communication**: Leverages Telegram’s encryption and bot APIs.
- **Command Handling**: Supports dynamic addition of commands.
- **Logging and Monitoring**: Tracks activities for auditing purposes.

---

## Prerequisites

- Python 3.8 or higher
- A Telegram bot token (obtainable via [BotFather](https://core.telegram.org/bots#botfather))

---

## Installation

1. **Clone the Repository**
   ```
   git clone https://github.com/yourusername/aioc2.git
   cd aioc2
   ```

2. **Set Up a Virtual Environment** (optional but recommended)
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```
   pip install -r requirements.txt
   ```

---

## Usage

1. **Configure the Bot**
   Edit the bot token with your own.

2. **Run the C2 Server**
   ```
   python main.py
   ```

3. **Interact Through Telegram**
   Use the Telegram bot to send commands and receive responses.
For now, the user can use the following commands:
```
/screenshot: This will take a screenshot.
/download [location]: This will download a file from the specified location.
```
---

## Configuration


- **TOKEN**: Your Telegram bot token. 


---

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Disclaimer

This project is intended for educational and ethical purposes only. Unauthorized use of this tool is prohibited. Use responsibly.



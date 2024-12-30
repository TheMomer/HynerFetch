# HyperFetch

A lightweight, customizable system information fetcher written in Python.

![Screenshot](screenshot.png)

## Features

- Modular system for easy functionality extension
- Customizable ASCII logos
- Cross-platform support (Linux, Windows, macOS)
- System information display:
  - OS information
  - Kernel version
  - User and hostname
  - Memory usage
  - IP addresses (local and public)
  - CPU information
  - DE and terminal information (Unix-like systems)
  - System architecture

## Installation

### Requirements
- Python 3.6 or higher
- pip (Python package installer)

### Installing

1. Clone the repository:
```bash
git clone https://github.com/yourusername/hyperfetch.git
cd hyperfetch
```

2. Run the installer with administrative privileges:

For Linux/macOS:
```bash
sudo python3 install.py
```

For Windows (Run Command Prompt as Administrator):
```cmd
python install.py
```

## Configuration

The configuration files are located in:
- Linux/macOS: `~/.hyperfetch/`
- Windows: `%USERPROFILE%\.hyperfetch\`

### Directory Structure
```
.hyperfetch/
├── logos/          # ASCII art logos
│   ├── arch.txt
│   ├── windows.txt
│   └── unknown.txt
├── modules/        # Custom modules
│   └── architecture_info.py
└── config.conf     # Main configuration file
```

### Configuration File
```ini
[HyperFetch]
logo = 
show_memory = true
show_kernel = true
show_ip = true
show_unix_info = true
show_cpu = true
```

## Creating Custom Modules

1. Create a new Python file in the `~/.hyperfetch/modules/` directory
2. Include the required function `run()` in your module
3. Use the colorama formatting for consistent output

Example module:
```python
from colorama import Fore, Style

def run():
    print(f"{Fore.GREEN}Custom Module:{Style.RESET_ALL} Hello World!")
```

## Uninstallation

For Linux/macOS:
```bash
sudo rm /usr/bin/hyperfetch
rm -rf ~/.hyperfetch
```

For Windows (Run Command Prompt as Administrator):
```cmd
del %WINDIR%\System32\hyperfetch.exe
rmdir /s /q %USERPROFILE%\.hyperfetch
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the GNU/GPL 3.0 license - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to [Neofetch](https://github.com/dylanaraps/neofetch) for inspiration
- All contributors and users of HyperFetch

## Support

If you encounter any issues or have suggestions, please create an issue in the GitHub repository.
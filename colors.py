class Colors:
    # Basic colors
    RED = "\033[31m"
    GREEN = "\033[32m"
    GREY = "\033[90m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    RESET = "\033[0m"
    
    
    @staticmethod
    def print_color_text(text, color):
        return f"{color}{text}{Colors.RESET}"
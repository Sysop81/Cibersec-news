import pyfiglet
from colors import Colors

class Display:

    PROGRAM_NAME = "CIBERSEC NEWS"
    VERSION = "1.0"
    AUTHOR = "Jose Ramon Lopez Guillen"
    GITHUB = "github.com/Sysop81"
    DESCRIPTION = "CIBERSEC NEWS - Security news aggregator"

    @staticmethod
    def show_banner():
        print(f"{Colors.GREEN}{(pyfiglet.figlet_format(Display.PROGRAM_NAME, font="cybermedium")).strip()}{Colors.RESET}")
        Display.show_description()

    @staticmethod
    def show_description():
        print(Colors.print_color_text(f"Version: {Display.VERSION}",Colors.GREEN))
        print(Colors.print_color_text(f"Author : {Display.AUTHOR}",Colors.GREY))
        print(Colors.print_color_text(f"GitHub : {Display.GITHUB}",Colors.GREY))
        print(Colors.print_color_text(f"{Display.DESCRIPTION}\n",Colors.GREY))                      

    @staticmethod    
    def show_info(text,color):
         print(Colors.print_color_text(text,color))        

    @staticmethod
    def show_news_in_console(entry):                         
        print(Colors.print_color_text(f"\tTitle: {entry["title"]}",Colors.YELLOW))
        print(Colors.print_color_text(f"\tLink: {entry["link"]}", Colors.BLUE))
        print(f"\tPublished: {entry["published"]}")
        print(Colors.print_color_text(f"\tSummary: {entry["summary"]}", Colors.GREY))
        print("\t---------------------------------------------")

    @staticmethod
    def show_news_site(site):
        print(Colors.color_text(f"\n=== {result["site"]} ===",Colors.MAGENTA))
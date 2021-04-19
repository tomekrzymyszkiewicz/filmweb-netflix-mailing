import config
import scraper
import sender

def main():
    mailing = scraper.get_films_of_month()
    loaded_config = config.load_config('config.ini')
    sender.send_mails(loaded_config[0],loaded_config[1],mailing)

main()

# if __name__ == "main":
#     main()
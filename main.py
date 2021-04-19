import config
import scraper
import sender

def main():
    mailing = scraper.get_films_of_month()
    print ("mail ok")
    loaded_config = config.load_config('config.ini')
    print ("config ok")
    sender.send_mails(loaded_config[0],loaded_config[1],mailing)
    print ("sending ok")

    
main()

# if __name__ == "main":
#     main()
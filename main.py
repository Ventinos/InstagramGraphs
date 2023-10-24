import scrapper
def main():
    dupla=scrapper.scrape()
    for (conta,seguidores) in dupla:
        print(conta,seguidores)
    

if __name__ == '__main__':
    main()

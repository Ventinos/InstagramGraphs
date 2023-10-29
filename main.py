import scrapper
def main():
    pair, bot=scrapper.scrape()
    #definindo o set maior, uniao dos seguidores das contas de partida:
    FollowersUnion = set()
    for (acc,followers) in pair:
        print(acc,followers)
        FollowersUnion=FollowersUnion.union(followers)
    #sim, a conta de nome vazio fudeu os esquema, tive que tirar
    FollowersUnion.remove('')
    graph = []
    graph.append(scrapper.scrapeFollowing(bot,FollowersUnion,10))
    bot.quit()
    print(graph)


if __name__ == '__main__':
    main()

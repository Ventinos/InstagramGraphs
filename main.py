import scrapper
def main():
    pair=scrapper.scrape()
    #definindo o set maior, uniao dos seguidores das contas de partida:
    FollowersUnion = set()
    for (acc,followers) in pair:
        print(acc,followers)
        FollowersUnion=FollowersUnion.union(followers)

    #problema aqui, quando ele tenta refazer o login, o instagram joga um popup desgracado na tela
    graph = []
    graph.append(scrapper.scrapeFollowing(FollowersUnion,10))
    print(graph)


if __name__ == '__main__':
    main()

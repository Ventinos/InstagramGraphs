import preReqs
import scrapper
import pickle


def main():
    prompt = int(input('[Required] - Load saved followers[1] or Scrape new followers[2] or Load saved graph[3](wip)'))
    if prompt == 1:
        filename = input('[Required] - Write the name of the file: ')
        bot = preReqs.generate_bot()
        file = open(filename, 'rb')
        FollowersUnion = pickle.load(file)
        print("[Info] - Followers list loaded successfully, beginning follows scraping")
    else:
        pair, bot = scrapper.scrape()
        #definindo o set maior, uniao dos seguidores das contas de partida:
        FollowersUnion = set()
        for (acc, followers) in pair:
            print(acc, followers)
            FollowersUnion = FollowersUnion.union(followers)
        FollowersUnion.remove('')
        filename = input('[Required] - Write the name of the new file: ')
        file = open(filename, 'wb')
        pickle.dump(FollowersUnion, file)
        print(f"[Info] - Collective followers list saved as {filename}")

    graph = [scrapper.scrapeFollowing(bot, FollowersUnion, 99)]
    bot.quit()
    print(graph)


if __name__ == '__main__':
    main()

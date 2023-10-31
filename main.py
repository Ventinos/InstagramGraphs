import preReqs
import scrapper
import pickle


def main():
    prompt = int(input('[Required] - Scrape new followers[1] or Load saved followers[2] or Load saved graph[3]'))
    if prompt == 2:
        filename = input('[Required] - Write the name of the file: ')
        bot = preReqs.generate_bot()
        file = open(filename, 'rb')
        FollowersUnion = pickle.load(file)
        print("[Info] - Followers list loaded successfully, beginning follows scraping")
        username, password = preReqs.load_credentials()
        preReqs.login(bot, username, password)
        graph = [scrapper.scrapeFollowing(bot, FollowersUnion, 999)]
        bot.quit()
        filename = input('[Required] - Write the name of the new graph file: ')
        file = open(filename, 'wb')
        pickle.dump(graph, file)
        print(f"[Info] - Graph saved as {filename}")
    if prompt == 1:
        pair, bot = scrapper.scrape()
        #definindo o set maior, uniao dos seguidores das contas de partida:
        FollowersUnion = set()
        for (acc, followers) in pair:
            print(acc, followers)
            FollowersUnion = FollowersUnion.union(followers)
        FollowersUnion.remove('')
        filename = input('[Required] - Write the name of the new followers file: ')
        file = open(filename, 'wb')
        pickle.dump(FollowersUnion, file)
        print(f"[Info] - Collective followers list saved as {filename}")
        graph = [scrapper.scrapeFollowing(bot, FollowersUnion, 999)]
        bot.quit()
        filename = input('[Required] - Write the name of the new graph file: ')
        file = open(filename, 'wb')
        pickle.dump(graph, file)
        print(f"[Info] - Graph saved as {filename}")
    else:
        filename = input('[Required] - Write the name of the file: ')
        file = open(filename, 'rb')
        graph = pickle.load(file)
    print(graph)


if __name__ == '__main__':
    main()

from src import preReqs
from src import scrapper
from src import serializer

def case1():
    pair, bot = scrapper.scrape()
    #definindo o set maior, uniao dos seguidores das contas de partida:
    FollowersUnion = set()
    for (acc, followers) in pair:
        print(acc, followers)
        FollowersUnion = FollowersUnion.union(followers)
    FollowersUnion.remove('')
            
    #serializacao do union:
    serializer.serializeStructure(FollowersUnion)
    print(f"[Info] - Collective followers list saved!")
            
    #montando grafo:
    graph = [scrapper.scrapeFollowing(bot, FollowersUnion, 5)]
    bot.quit()
            
    #serializacao do grafo:
    serializer.serializeStructure(graph)
    print(f"[Info] - Graph saved!")
    return FollowersUnion, graph

def case2():
    #desserializacao do union:
    FollowersUnion = serializer.deserializeStructure()
    print("[Info] - Followers list loaded successfully, beginning follows scraping")
            
    #montagem do grafo:
    prompt = preReqs.promptAcc()
    username, password = preReqs.load_credentials(prompt)
    bot = scrapper.initDriver()
    preReqs.login(bot, username, password)
    graph = [scrapper.scrapeFollowing(bot, FollowersUnion, 1500)]
    bot.quit()
            
    #serializacao do grafo:
    serializer.serializeStructure(graph)
    return FollowersUnion,graph

def case3():
    graph = serializer.deserializeStructure()
    return graph

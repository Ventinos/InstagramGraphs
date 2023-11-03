import cases

def main():
    prompt = int(input('[Required]-\nScrape new followers[1]\nLoad saved followers[2]\nLoad saved graph[3]\n'))
    graph = None
    FollowersUnion = None
    match prompt:
        case 1:
            FollowersUnion, graph = cases.case1()
        case 2:
            FollowersUnion, graph = cases.case2()
        case 3:
            graph = cases.case3()
        case _:
            print('[Info] - Invalid Option!')
    print(graph)

if __name__ == '__main__':
    main()

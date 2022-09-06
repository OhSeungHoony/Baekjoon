if __name__ == "__main__":
    n, k = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.sort()
    print(x_list[n-k])


def merge_the_tools(string, k):
    # your code goes here
    '''l = []
    for i in range(0, len(string), k):
        l.append(string[i:k+i])
    print(l)

    for item in l:
        new = ''
        for i in item:
            if i not in new:
                new += i
        print(new)'''

    for i in range(0, len(string), k):
        sub_string = string[i:k+i]
        new = ''
        for char in sub_string:
            if char not in new:
                new += char
        print(new)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

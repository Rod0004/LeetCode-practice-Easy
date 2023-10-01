'''
def rank(para1,para2):
    names = []
    scores = []

'''

if __name__ == '__main__':
    names = []
    scores = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)

        scores.sort()

    indexies = []
    second_lowest = scores[1]
    for i in range(len(scores)):
        if scores[i] == second_lowest:
            indexies.append(i)

    for i in indexies:
        print(names[i])





# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    names = list()
    scores = list()

    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)
        
    uniq_scores = set(scores)
    uniq_scores.remove(min(uniq_scores))
    second_lowest = min(uniq_scores)

    second_low_scorers = [names[i] for i, score in enumerate(scores) if score == second_lowest]
    second_low_scorers.sort()
    for name in second_low_scorers:
        print(name)
            
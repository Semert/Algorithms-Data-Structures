# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

scores = [100, 100, 50, 40, 40, 20, 10]
alice = [5, 25, 50, 120]
def climbingLeaderboard(scores, alice):
    add = []
    for i in range(len(alice)):
        if(alice[i]<scores[-1]):
            scores.append(alice[i])
            count = 1
            scoresler = scores[0]
            for l, j in enumerate(scores):

                if (scoresler > j):
                    count += 1
                    print(count, j)
                    scoresler = j
                if (j == alice[i]):
                    print(count, alice[i], "hahaha")
                    add.append(count)
        else:
            break
    def deneme(i):
        high = len(scores) - 1
        low = 0
        while low <= high:
            mid = (low + high)//2
            if(alice[i] <= scores[mid]):
                low = mid + 1
            elif(alice[i] >= scores[mid]):
                high = high - 1
        a = scores.index(scores[mid])
        print(a)
        if i != 0:
            scores.pop(scores.index(alice[i-1]))
        scores.insert(a, alice[i])
        print(scores,alice[i])
        result = []
        count = 1
        scoresler = scores[0]
        for l, j in enumerate(scores):

            if (scoresler > j):
                count += 1
                print(count, j)
                scoresler = j
            if(j == alice[i]):
                print(count,alice[i],"hahaha")
                result.append(count)
        return result[0]
    cevap = []
    cevap.extend(add)
    for i in range(1,len(alice)):
        cevap.append(deneme(i))
    print(cevap)


climbingLeaderboard(scores,alice)


# ---------------------------------
def In_rank(s):
    c=1
    a=max(s)
    rl=[]
    for i in s:
        if a<=i:
            rl.append(c)
        else:
            c+=1
            rl.append(c)
            a=i
    return rl


def binarysearch(s,value):
	lo=0
	hi=len(s)-1
	while (lo<=hi):
	    mid=int(lo+(hi-lo)/2)
		if (s[mid]==value):
			return mid
		elif ((s[mid]< value) and (value < s[mid-1])):
			return mid
		elif ((s[mid]> value) and (value >= s[mid+1])):
			return mid +1
		elif (s[mid]<value):
			hi=mid-1
		elif (s[mid]>value):
			lo=mid+1

def climbingLeaderboard(s, t):
    q=[]
    irl=In_rank(s)
    print(irl)
    for i in t:
        if (i>s[0]):
    		q.append(1)
    	elif (i<s[len(s)-1]):
    		q.append(irl[len(irl)-1]+1)
    	else:
    		q.append(irl[binarysearch(s,i)])
    return q


# ---------------------------------------------------

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    scores_with_rank = assign_rank_to_scores(scores)

    alices_rank = []
    for score in alice:
        rank = get_rank(scores_with_rank, score)
        alices_rank.append(rank)
    return alices_rank


def get_rank(scores, target):
    left, right = 0, len(scores) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if scores[mid][0] == target:
            return scores[mid][1]
        if scores[mid][0] > target:
            left = mid + 1
        else:
            right = mid - 1

    if right < 0:
        return 1

    if left >= len(scores):
        return scores[-1][1] if scores[-1][0] == target else scores[-1][1] + 1

    return scores[right][1] + 1


def assign_rank_to_scores(scores):
    rank = 1
    scores_with_rank = [(scores[0], 1)]
    for i in range(1, len(scores)):
        if scores[i] != scores[i - 1]:
            rank += 1
        scores_with_rank.append((scores[i], rank))
    return scores_with_rank
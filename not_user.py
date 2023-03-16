def solution(n, users):
    user_scores = sorted(user_scores, key=lambda x: int(x.split()[1]), reverse=True)
    
    count = 0  
    nicknames = {}  
    for i, user_score in enumerate(user_scores):
        user, score = user_score.split()
        score = int(score)
        
        if user not in nicknames.values():
            nicknames[user] = i // K + 1
            count += 1
        
        if i > 0 and i % K == 0 and score < int(user_scores[i-1].split()[1]):
            count += 1
        
        if i > 0 and i % K != 0 and score != int(user_scores[i-1].split()[1]):
            count += 1
            
    return count

def solution(people, limit):
    people.sort()
    
    boat = 0
    
    while len(people) > 0:
        boat_limit = limit
        while True:
            rescued = ride(people, boat_limit)
            
            print(boat,boat_limit, rescued, people)
            
            if rescued == 0:
                boat += 1
                break

            boat_limit -= rescued

    return boat

def ride(sorted_people, limit):
    for i in range(len(sorted_people) - 1, -1, -1):
        if sorted_people[i] <= limit:
            return sorted_people.pop(i)
        
    return 0

print(solution([70, 50, 80, 50], 100))
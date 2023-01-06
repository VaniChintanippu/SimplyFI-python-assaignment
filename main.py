def splitting_tickets(available_tickets):
    result = []
    for i in available_tickets:
        result.append(i.split('-')) # appending each splitted ticket
        
    return result    

def finding_the_route(available_tickets_list, starting_point, vacation_cities_list):
    route = ''
    landed_point = starting_point
    for i in range(len(vacation_cities_list)): # iterating length of the vacation_cities_list times
        for j in available_tickets_list:
            if j[0] == landed_point:
                route += j[0] + '-'
                landed_point = j[1]
                break
    
    return route    

vacation_cities_list = input().split(',')
starting_point = input() # taking input starting point
available_tickets = input().split(',') # taking inputs available_tickets
available_tickets_list = splitting_tickets(available_tickets) # splitting the each ticket
get_route = finding_the_route(available_tickets_list, starting_point, vacation_cities_list) # finding the route
print(get_route[:len(get_route)-1]) # removing last hyphen and printing the result

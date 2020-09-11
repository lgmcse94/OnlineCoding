import requests
def solve(year,team):
    total=0
    for ctr in range(1,10):
        for res in ['https://jsonmock.hackerrank.com/api/football_matches?year='+str(year)+'&team2='+str(team),'https://jsonmock.hackerrank.com/api/football_matches?year='+str(year)+'&team1='+str(team)]:
            response = requests.get(res+'&page='+str(ctr))
            response.raise_for_status()
            jsonResponse = response.json()
            for key, value in jsonResponse.items():
                if(key=='data'):
                    for v in value:
                        if(v['team1']==team):
                            total=total+int(v['team1goals'])
                        elif(v['team2']==team):
                            total=total+int(v['team2goals'])
    return total

print(solve('2011','Barcelona'))
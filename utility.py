import csv
import os
import sys

def clean_player_data():
    team_list = ["Liverpool", "Manchester City", "Leicester City", "Chelsea", "Manchester United", "Wolverhampton Wanderers",
                "Sheffield United", "Tottenham Hotspur", "Arsenal", "Burnley", "Crystal Palace", "Everton", "Watford",
                "Newcastle United", "Southampton", "Brighton & Hove Albion", "West Ham United", "Bournemouth", "Aston Villa",
                "Norwich City", "Ipswich Town", "Queen Park Rangers", "Leeds United", "Swindon Town", "Coventry City", "Barnsley", 
                "Birmingham City", "Blackburn Rovers", "Blackpool", "Bolton Wanderers", "Bradford City", "Cardiff City", 
                "Charlton Athletic", "Derby County", "Fulham", "Huddersfield Town", "Hull City" "Middlesbrough", "Nottingham Forest",
                "Oldham Athletic", "Portsmouth", "Reading", "Stoke City", "Sunderland", "Swansea City", "West Bromwich Albion",
                "Wigan Athletic", "AFC Wimbledon"]

    try :
        inp = open(os.path.join(sys.path[0], "data\\Player.csv"), "r", encoding="utf-8")
        out = open(os.path.join(sys.path[0], "data\\Player_Edited.csv"), "w", encoding="utf-8", newline ="")
            
        writer = csv.writer(out)
            
        #writing header for csv
        writer.writerow(["ID", "Name", "Nationality", "Overall", "Potential", "Club"])

        for row in csv.reader(inp):
            if row[9] in team_list:
                writer.writerow([row[1], row[2], row[5], row[7], row[8], row[9]])
    except IOError as err :
        print("IO Error Number", err.errno, "[", err.strerror, "]")

def clean_match_data() :
    try :
        inp = open(os.path.join(sys.path[0], "data\\EPL_Set.csv"), "r", encoding="utf-8")
        out = open(os.path.join(sys.path[0], "data\\EPL_Set_Edited.csv"), "w", encoding="utf-8", newline="")

        writer = csv.writer(out)

        for row in csv.reader(inp) :
            writer.writerow([convert_team_name(row[2]), convert_team_name(row[3]), row[4], row[5], row[6]])

    except IOError as err :
        print("IO Error Number", err.errno, "[", err.strerror, "]")
            

def convert_team_name(name) :
    if name == "Birmingham" :
        return "Birmingham City"
    elif name == "Blackburn" :
        return "Blackburn Rovers"
    elif name == "Bolton" :
        return "Bolton Wanderers"
    elif name == "Bradford" :
        return "Bradford City"
    elif name == "Brighton" :
        return "Brighton & Hove Albion"
    elif name == "Cardiff" :
        return "Cardiff City"
    elif name == "Charlton" :
        return "Charlton Athletic"
    elif name == "Coventry" :
        return "Coventry City"
    elif name == "Derby" :
        return "Derby County"
    elif name == "Huddersfield" :
        return "Huddersfield Town"
    elif name == "Hull" :
        return "Hull City"
    elif name == "Ipswich" :
        return "Ipswich Town"
    elif name == "Leeds" :
        return "Leeds United"
    elif name == "Leicester" :
        return "Leicester City"
    elif name == "Man City" :
        return "Manchester City"
    elif name == "Man United" :
        return "Manchester United"
    elif name == "Middlesboro" :
        return "Middlesbrough"
    elif name == "Newcastle" :
        return "Newcastle United"
    elif name == "Norwich" :
        return "Norwich City"
    elif name == "Nott'm Forest" :
        return "Nottingham Forest"
    elif name == "Oldham" :
        return "Oldham Athletic"
    elif name == "QPR" :
        return "Queen Park Rangers"
    elif name == "Sheffield" :
        return "Sheffield United"
    elif name == "Stoke" :
        return "Stoke City"
    elif name == "Swansea" :
        return "Swansea City"
    elif name == "Swindon" :
        return "Swindon Town"
    elif name == "Tottenham" :
        return "Tottenham Hotspur"
    elif name == "West Brom" :
        return "West Bromwich Albion"
    elif name == "West Ham" :
        return "West Ham United"
    elif name == "Wigan" :
        return "Wigan Athletic"
    elif name == "Wimbledon" :
        return "AFC Wimbledon"
    elif name == "Wolves" :
        return "Wolverhampton Wanderers"
    else :
        return name


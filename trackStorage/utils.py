

existingActivities = [
    'in_vehicle', 'on_bicycle', 'on_foot', 'running', 'still', 'tilting', 'unknown', 'walking'
]

to_ignore = {'id', 'trip_id', 'latitude', 'longitude', 'altitude', 'ptstop', 'timestamp',
             'registeredactivities', 'transporttypeusedtonextpoint',
             'registeredActivities', 'transportTypeUsedToNextPoint'
            }


existingActivitiesLen = 8


def split_activities(registeredActivities: str) -> dict:
    if '-' not in registeredActivities: registeredActivities += '-100'
    registeredActivities = registeredActivities.split()
    
    activitiesDict = dict()
    for activity in registeredActivities:
        k,v = activity.split('-')
        activitiesDict[k.lower()] = float(v)
    
    splitted = dict()
    for activity in existingActivities:
        splitted[activity] = activitiesDict.get(activity, 0.01)
    
    return splitted


def set_v_or_else_mean(v, mean):
    if -1.0001 <= v <= -0.9999: return mean
    return v


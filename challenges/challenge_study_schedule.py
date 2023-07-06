def study_schedule(permanence_period, target_time):
    counter = 0
    if target_time is None:
        return None
    for each_period in permanence_period:
        if type(each_period[0]) != int or type(each_period[1]) != int:
            return None
        if each_period[0] <= target_time <= each_period[1]:
            counter += 1
    return counter

def get_user_info(sht):  # iterate over tracking numbers
    # first cell with data is E3
    n = 4
    name_cell = 'A' + str(n)
    strava_id_cell = 'B' + str(n)
    plan_cell = 'C' + str(n)

    name = sht.acell(name_cell).value

    users = {}

    while name != '':
        strava_id = int(sht.acell(strava_id_cell).value)
        plan = int(sht.acell(plan_cell).value)
        user = {'name': name, 'plan': plan, 'value': 0, 'row_nbr': n}
        users[strava_id] = user
        n = n + 1
        name_cell = 'A' + str(n)
        strava_id_cell = 'B' + str(n)
        plan_cell = 'C' + str(n)
        name = sht.acell(name_cell).value

    return users

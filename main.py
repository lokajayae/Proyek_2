import utility as utils
import calculation as calculation
import gui as gui

utils.clean_player_data()
utils.clean_match_data()


gui.display()

home_team = "Manchester United"
away_team = "Chelsea"
date = "11/08/2019"
season = utils.get_season(date)


utils.get_image_path(home_team)
utils.generate_data_for_calculation(home_team, away_team, utils.get_year(date))

calculation.generate_all_data(home_team, season)

if calculation.laplace_estimator_is_estimator_needed() :
    calculation.do_laplace_estimator()

calculation.calculate_win_probability(home_team, away_team, season)
calculation.calculate_draw_probability(home_team, away_team, season)
calculation.calculate_lose_probability(home_team, away_team, season)

from ratemyprof_api import RateMyProfApi

uwm_rmp_sid = "1256"


def test_init_ratemyprof():
    api = RateMyProfApi(uwm_rmp_sid, testing = True)
    uni = api.scrape_professors()


test_init_ratemyprof()
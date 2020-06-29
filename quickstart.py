""" Quickstart script for InstaPy usage """

# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace


# set workspace folder at desired location (default is at your home folder)
set_workspace(path=None)

# get an InstaPy session!
session = InstaPy(username="esports_merchandising", 
        password="Esportsmkt11_inst")

with smart_run(session):
    # general settings
    session.set_dont_include(["friend1", "friend2", "friend3"])

    # activity
    session.set_user_interact(amount=2,
				 percentage=70,
                  randomize=True,
                   media='Photo')

    session.follow_likers(['elrubiuswtf' , 'grefg_official'], photos_grab_amount = 2, follow_likers_per_photo = 30, randomize=True, sleep_delay=600, interact=False)


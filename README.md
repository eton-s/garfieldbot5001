# garfieldbot5001
This is just a simple python script to update the desktop wallpaper with
recent tweets from the GarfieldBot5000 bot, which posts randomized 3-panel
garfield comics. This script only supports Windows.

Before running the garf.py script, update TOKEN to have your Twitter API
bearer token. You may need to create an account at https://developer.twitter.com/en if you have not already used Twitter API.

You can also choose to automate this using Windows Task Scheduler:
1. Clone both files in the repo to a local directory
2. Create a task in Task Scheduler
3. Add desired triggers (time interval, on startup, etc.)
4. Add an action that runs garfieldbot5001.bat

<pre>
Project Outline
LAST MODIFIED: 4/23/20
Presentation Date: 5/4/20

Sections:
    A: Our Goal / Project Writeup
    B: Project File Structure
    C: Files
    D: Code Structure & Conventions
    E: Current Goals
    F: Future Goals
    G: Using GIT
    H: How to run / Required Libraries
    I: Misc / Debugging

// Section A: Our Goal / Project Writeup
    Discover your true vibe
    By Kylei Hoffland, Gianna Lammer, Nathan Breunig, Jon Noel

    For our project, we will use the Spotify API as a music analysis tool to generate playlists and determine your most
    popular jams. Using a GUI, the user can generate playlists based on genre, artist, songs, etc. These playlists will
    contain songs never listened to by the user. In addition to this, the user will also be able to generate word clouds
    based on lyrics, top artists, songs, and more.

    Features:
        -Suggest songs based on an identified theme
        -Create word clouds in real time
        -Generate word cloud based on users most listened to artitsts and songs, as well as the lyrics to any song
        -Suggest songs with opposite themes
        
    We chose this project because the current system of music is broken. We are stuck in a jukebox of captivity.
    Every online radio recommends the same songs, including Spotify. We want to create a convenient way of discovering
    new music without pushing the user too far from their comfort zone.

    Technologies Needed:
        -Spotify API
        -Genius API
        -World Cloud Generator API
        -Python GUI Library (Kivy?)
        -Dictionary.com API

// Section B: Project File Structure
    The project file tree is seen below:

    song-alyze/
        res/
            fonts/
                AlphaMusicMan.ttf
                Marvind.ttf
        src/
            .cache-
            config.py
            main.py
            spotify.py
        .gitignore
        .gitmodules
        LICENSE
        README.md

    Other Notes: This is subject to change if we add more functionality such as implementing a GUI.

// Section C: Files/Directories and their meaning

    /song-alyze
    This is the project folder.
    
    res/
    Folder to contain various resources needed by the project.
    
        res/fonts
        Folder to contain different fonts used by wordcloud

    src/
    This folder contains all of our .py files we will be dealing with.

        src/.cache-
        This is a cache file generated by the spotipy API after we have granted it access to our Spotify account. This file is used
        as memory so we don't have to authorize every time we run the project.

        src/config.py
        This file contains the configuration information for the spotipy API to work. Specifically it contains for ID's from Spotify
        saying this project is allowed to use the API.

        src/main.py
        This is the main python file as of right now. This contains the main method of the program. This is where we can call the
        functions we write in spotify.py. This could also be where our GUI code laters on.

        src/spotify.py
        This is the file that deals with the spotipy API. Here can write all of our needed functions that deal with the API.

    .gitignore
    Inside the file are a list of files or file extensions that git should "ignore".
    These files will not be committed/pushed. This is useful for various reasons. For example, if you are using the
    pycharm IDE, it will create a directory .idea with stuff we don't care about. There is no reason git should save this file
    and put it on GitHub.com for example (so we add it in the .gitignore file). If you have any files like this that get created
    by your IDE or something, you can add them to the .gitignore. Another file that we ignore is the ".cache-" file generated
    by spotipy. This cache file contains OUR Spotify user id's (this allows us to not have to authenticate every time we use
    this program). So we ignore it since this is personal and private info that should not go on GitHub.com

    LICENSE
    Project MIT license.

    README.md
    Readme file (this file)

// Section D: Code Structure & Conventions
    -Snake case should be used for all variables and function names
    -No more global variables should be needed
    -Functions using the spotipy API should have optional parameters (see get_top_tracks as example)
    -When you want to return either a track, artist, or playlist when will use a dictionary (not a tuple anymore).
     Each dictionary should have the following fields:
        -name (name of playlist, track or artist)
        -id (spotify id)
        -type (track, playlist, or artist)
        -popularity (artists worldwide popularity ranking...not sure if this applies to tracks or playlists but add anyways)
    -Make necessary comments (parameters, returns, etc)

    IMPORTANT: Look at get_top_tracks function as example for all of these conventions

// Section E: Current Goals
   -Brainstorm new unique ways to use the API  /  Add more functionality
   -GUI (See main.py for instructions/TODO)

// Section F: Future Goals
    -See above section

// Section G: Using GIT
    Useful git reference: https://git-scm.com/docs

    *Please read the whole document before trying the commands*

    The following steps are the steps you should take EVERY time you work on this project:
        1. Pull the repository from GitHub  -- See Example A
        2. Commit changes you make to the project  -- See Example B
        3. Push the changes back to GitHub  -- See Example C

    Example A: pull
        Command: git pull <remote_name> <branch_name>
        Command we will use: git pull origin master
        Explanation: The pull command is used to "pull" the project off of GitHub.com onto your local computer.
                     This way every time you start to make changes/add to the project you know you have the latest
                     version with everyone else's changes (permitting the previous changes were correctly "pushed").
                     THIS SHOULD BE DONE EVERY TIME YOU BEGIN TO WORK ON THE PROJECT!

    Example B: commit
        Command: git commit -a -m <"commit_message">
        Command we will use: git commit -a -m "Commit Message"
        Explanation: After making changes to the project, git requires you to "commit" them before "pushing" them back to GitHub.com.
                     Committing the changes tells git which files you want to "push" next time you run the push command.
                     The "-a" flag in the command just means commit all modified files (you can commit individual files one by one
                     if necessary, but "-a" should be sufficient). The "-m" flag in the command stands for message.
                     That is why you are required to enter a string after this flag (as denoted by "Commit Message" above).
                     This should be a short (one sentence) message about the changes you made
                     (Don't worry about this too much, but you should put something there).

                     Other helpful commands to use BEFORE commit would be "git log" and "git status". "git log" will show you a list
                     of all PREVIOUS commits that have been made (and by who).
                     "git status" is VERY useful. This command should be used EVERY time BEFORE committing. After running this
                     command there will be two sections: a section titled "Changes to be committed" and "Changes not staged for commit".
                     THIS IS CRITICAL since this command will tell us which changes WILL and WILL NOT be committed (if we use the
                     "git commit..." command).
                     Let's say I made a change to "main.py". I then run "git status" and the "main.py" file shows up under
                     "Changes not staged for commit". This means if I run "git commit...", the "main.py" file will NOT be committed.
                     In this case, anything that you want to commit that is under "Changes not staged for commit", you MUST use
                     "git add <file>". So in this example I must FIRST use "git add main.py" BEFORE committing. After I run the "git add"
                     command, if I run "git status" again, you will now see that "main.py" is under "Changes to be committed".
                     Now, and ONLY now, is it ok to run "git commit -a -m 'Commit Message'".

                     Be aware, sometimes "git status" will show a file that is under "Changes to be committed" BUT ALSO under
                     "Changes not staged for commit". IN THIS CASE, YOU MUST USE "git add <file>" BEFORE COMMITTING.

                     You should only commit AFTER you are DONE working on the project for a time period. There is no need to commit
                     every time you change one line of code for example. In other words, your only commit should be right before you are
                     going to push your changes.

    Example C: push
        Command: git push <remote_name> <branch_name>
        Command we will use: git push origin master
        Explanation: The push command is used to push your local project back to GitHub.com for others to see. The push command should
                     ONLY be used after correctly committing. If you don't commit anything, then there is nothing to push.
                     You should only push ONCE, and that is when you are done working on the project for a set time period.

    Workflow:
        1. Pull the project
        2. Make changes
        3. Use "git status"
            a. If there are "Changes not staged for commit"
                i. Use "git add <file>" until there are no more files under "Changes not staged for commit"
                ii. Commit
            b. If there are "Changes to be committed" WITHOUT any "Changes not staged for commit"
                i. Commit
        4. Push the project

    OTHER NOTES:
        - If you aren't sure what you are doing or not sure what this command will do (or mess up) please ask before doing said thing.
        - When running these commands make sure your terminal is in the project directory (ex. "../song-alyze/"). Make sure you are not
          in any sub directories or elsewhere.

// Section H: How to run / Required Libraries
    Required Libraries for this project are listed below.
        1. spotipy - Install from pip using "pip install spotipy"
        2. matplotlib - Install from pip using "pip install spotipy"
        3. wordcloud - Install from pip using "pip install wordcloud"
            If your wordcloud didn't install from pip, this seems to be a bug on Windows 10. 
            Follow the below steps thanks to @iturki from https://github.com/amueller/word_cloud/issues/134
            
            1. Download the .whl file compatible with your Python version and your windows distribution (32bit or 64bit)
            from here (https://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud), cd to the file path
            2. Run this command python -m pip install <filename>
        
    The main method is located in src/main.py, so this is the file you should run in the terminal if you choose to run it that way.

// Section I: Misc / Debugging
    JSON formatter: https://jsonformatter.curiousconcept.com/, useful for visualizing spotify API response
</pre>
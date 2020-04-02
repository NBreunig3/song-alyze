<pre>
    Project Outline
LAST MODIFIED: 4/2/20
Next Project Update Date: 4/3

Sections:
    A: Our Goal / Project Writeup
    B: Project File Structure
    C: Files
    D: Code Structure & Conventions
    E: Current Goals
    F: Future Goals
    G: Using GIT
    H: Git Submodules
    I: How to run
    J: Misc / Debugging

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
        -We chose this project because the current system of music is broken. We are stuck in a jukebox of captivity.
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
        libs/
            spotipy/
            word_cloud/
            matplotlib/
            __init__.py
        src/
            .cache-
            config.py
            main.py
            spotify.py
        .gitignore
        .gitmodules
        LICENSE
        README.md

    Other Notes: This is subject to change if we add more functionality such as using another API or using GUI.

// Section C: Files/Directories and their meaning

    /song-alyze
    This is the project folder.

    libs/
    This folder is to store the libraries (API's) we are going to use in this project. If the folders (libraries) are empty
    go to Section H: Git Submodules to fix. 
        
        libs/matplotlib
        This library is used to save our generated word cloud.
        
        libs/spotipy
        Spotify API 
        
        libs/word_cloud
        Word cloud generator

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

    .gitmodules
    Disregard for now but do not delete please.

    LICENSE
    Project MIT license.

    README.md
    Readme file useful for GitHub

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
    -Finish writing the needed methods in spotify.py using the spotipy API
     (Look in code for links regarding API reference points and the spotipy API reference)

// Section F: Future Goals
    -Include the Genius API and Dictionary API in src/lyric_analyzer.py
    -GUI

    Edit this document and add more if needed!

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
                     ONLY be used after correctly committing. If you don't commit anything, then there is nothing to push. A push needs
                     to be done EVERY time after you are IMMEDIATELY done working on the project. If you delay pushing your changes
                     there is a chance that your changes will get lost (since you didn't "share" your changes with the rest of us).

                     You should only push ONCE, and that is when you are done working on the project for a set time period.

    Workflow:
        1. Pull the project
        2. Make changes (in a somewhat timely fashion. More about this below)
        3. Use "git status"
            a. If there are "Changes not staged for commit"
                i. Use "git add <file>" until there are no more files under "Changes not staged for commit"
                ii. Commit
            b. If there are "Changes to be committed" WITHOUT any "Changes not staged for commit"
                i. Commit
        4. Push the project

    OTHER NOTES:
        - If you aren't sure what you are doing or not sure what this command will do (or mess up) please ask before doing said thing.
        - This isn't a perfect system since it is possible to lose changes if we all work on this at once for example. This shouldn't
          be a huge problem but is possible. For example, lets say Person A and Person B begin working on the project at similar times.
          They both pull the project around the same time (no problem), they then make their changes over the next hour or so. Person A
          finish's his/her changes in 30 min. He/She correctly commits and pushes their changes. (I have no idea when to use "their" or
          "he/she" so I just choose at random it seems) Then Person B finishes his/her changes in 60 mins. Person B also correctly
          commits and pushes their changes. But since Person B pushed WITHOUT Person A's changes, Person A's changes were erased. This
          is obviously problematic. (This why there are things called "branches" in git to account for this sort of problem, but it is
          more complicated and frankly we don't need to use them for this project) We could maybe combat this by just using communication
          to see if anyone is currently working on the project. If so, we can just tell that person to push their changes and then others
          can pull. Again, this shouldn't be a huge issue, but you should be aware it can happen and keep your eye out for it. I will
          try and keep backups of the prev versions (git does this already I think).
        - It is important to keep your "work sessions" relatively short for the above reason. Do not start working on the project (pull)
          and not be done (push) for hours. This allows too much time for another person to also begin working on it (pulling without
          your current modifications), and then there is potential code loss.
        - When running these commands make sure your terminal is in the project directory (ex. "../song-alyze/"). Make sure you are not
          in any sub directories or elsewhere.
          
// Section H: Git Submodules
    For this project we are using other Python libraries such as "spotipy" and "word_cloud". In order to include these in our own
    local project we use another feature of Git called submodules. This allows us to have the library in our local directory while
    being connected to its corresponding GitHub repository. This makes it easy to update the libraries if they make changes on
    their end. If your libs/<library_name> folder is blank that means you need to run one of the following commands below. 
    
    Command to download library (this only needs to be done once): git submodule update
    Command to update library (most likely won't use but allows us to directly update the lib from their GitHub repository):
        git submodule update
        
    Note: Notice two commands above are the same. All the command does is fetch new/missing files from the online repo to our
          local project repo. 

// Section I: How to run
    The main method is located in src/main.py, so this is the file you should run in the terminal if you choose to run it that way.
    NOTE: When running from the terminal vs in pycharm the import statements may or may not through errors. I am currently
          researching the issue. If you are using pycharm the local imports (imported files we created) should be using the
          "from src..." prefix. If you are running from the terminal then you should omit that prefix and just have "import spotify".

// Section J: Misc / Debugging
    Getting errors about imports or libraries missing or misbehaving? See Section H. 
</pre>
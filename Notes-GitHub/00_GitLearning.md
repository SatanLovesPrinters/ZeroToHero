
<summary>
Note; Git has it's own software that needs to be installed. 
Git to GitProvider / Cloud
File Explorer > Cloud > Git
Git Share Methods
	- Share Code via GitProvider (GitHub / Go PUBLIC or Private
File to Git Provider to File Recipient 
	- File & File Recipient create a mutual pool
	- Working on the same file at same time: 
		○ Normally two files can merge into one w/ built in code.
	- Reported features can appear for Open Source assistance
GitProvider Features
	- Branch: Direct copy from the repo to allow multi-use on a file.
		○ You can clone a repo but branches cannot be part of more than one repo.
	- Branching allows multiple copies to go in tandem at the same time.
	- If multiple users & multiple places are working on a document at the same time:
		○ More issues are likely to occur. 
</summary>

### Note:
<summary>

	- Git has it's own software that needs to be installed. 
	- Git to GitProvider / Cloud
Essential Baseline of "what is GIT":
	File Explorer > Cloud > Git
Git Share Methods
	- Share Code via GitProvider (GitHub / Go PUBLIC or Private
File to Git Provider to File Recipient 
	- File & File Recipient create a mutual pool
	- Working on the same file at same time: 
		○ Normally two files can merge into one w/ built in code.
	- "Report" / flag features can appear for Open Source assistance to improve communication
	- See branching for multiple people working on the same source. Decreases likelihood of changes not being tracked. 
GitProvider Features
	- Branch: Direct copy from the repo to allow multi-use on a file.
		○ You can clone a repo but branches cannot be part of more than one repo.
	- Branching allows multiple copies to go in tandem at the same time.
	- Think of OneDrive & how sync issues occur for users who work on the document locally while users stay on the live / real-time web version.
</summary>

<summary>

Course	Git Essential Training
Topic	Github / Gitproviders 
Chapter_1	How Does Git Work?
Chapter_1_Notes	- Source provider (i.e. Coder) uploads via GitProvider Application
	- See notes: Branching / Sharing Options via Public+Private Links
	- Providers such as GitHub
	- Install Locally:
	        • Example:
Remote Repository @ https://github.com/GitRepo
Local PC = Local repository location (.git)
Staging Area > Local Staging File Structure (C:\Scripts\GitRepo\)
From Local PC CLI - Run something such as:  
	        • Git Pull
	        • Git Push 
	        • Git Add .path
	        • Git = Distributed Version Control 
	        • OneDrive/DropBox = Centralized Version Control
	                ○ If I change a file on my PC then the server updates
	                ○ If something happens to the server, then I go back to my last file copy.
	        • In Distributed Version - The files are centrally located to everybody, therefore everybody has access & if the GitProvider goes down, then all with access still have local versions of all copies. 
	                ○ QUESTION: HOW DO YOU SECURE PERMISSIONS? 
	        • No one understands everything about Git
	                
	
Chapter_2_Summary	Git Pull adds the file to a local repo & directly to the local folder
* The files must be staged & committed before being pushed.
Git Push only sends changes to the remote repository that are in the Local Repository as well.
- Even without internet you can still go back to earlier versions, make snapshots as you go, and revert to changes made earlier in the script
	Corrupting the Main Repo: 
- "Because Git is distributed, the file in users' repositories will be unaffected by any changes to the file in the main repository unless users attempt to retrieve the corrupted file" 
- So if a user corrupts the Main Repo > Revert to a previous version & then advise people to retrieve the new copy.
- Git add = Stage the changes 
- Git commit = Send staged to local repo (+commit message)
	- Git push = Push committed changes to remote repository.  

Chapter_2	Install & Configure Git
Chapter_2_Notes	• Install Git (win/linux/mac): https://git-scm.com/download/win 
	        • Set to VSCode & Install VSCode Extensions > GitHistory,GitLens,GitGraph
	• Configure Git:
	        • Gitconfig
	        • Global Config : C:\Users\User.gitconfig
	        • Local = .git/config
	                ○ Default editor / branch / aliases
	        • From Terminal:
	                ○ Git config --list
	                ○ Git config --global user.name "my Name"
	                ○ Git config --global user.email "myName@email.com"
	        
Chapter_3	Push Your Code w/ Git
Chapter_3_Notes	• Setup Remote Repository
	        • GitHub/GitBuckets/
	        • Git init creates local repository
	        • Git remote add defines the remote repository & then connects the two

Chapter_4	Make Changes to Files
Chapter_4_Notes	Git status
	Git push
	Always use git status to see how the repository is doing
	        - Creating a change is like creating a new file
	
	Git diff shows what has been changed local vs remote
	Git diff --cached before you make a commit
	VS Studio Code
	        - Source Control = Shows WORKING TREE
	        - Git log --grep='expression'
	        - Git show [checksum]
	        - Git log -p 
	        - Git log --graph
	Afted deleting you can git add. / git commit -m 'Removed example' / git push 
	        - Can still be tracked on previous commits 
	Renaming Note: Git won't understand at first it is a new file. After committing the change, it will merge.
	        - Git mv .\example.txt example-renamed.txt (Rename)
	Folders:
	        - Git ignores empty folders
	                ○ .gitkeep (Important to structure, but no data to keep)
	Revert to Previous Commit / Undoing Commits:
	        - If : git add .
	                ○ Let's revert? Git status
	                        § Git restore --staged <file…>
	                        § Git restore --staged .
	                ○ Go further back / delete these chages?
	                ○ Git restore .
	        - Git log 
	        - Git checkout (paste commit unique ID from git log) 
	        - Git checkout main (return statement)
	Revert to the Previous Version:
	        - Git log --oneline (prints out in one line)
	        - Git revert [commit ID to revert to]
	        - History is always added. Git revert adds a new source line for 'git commit reverted'
	
	Create file called importantfile.md
	        - Create folder
	        - Add file into folder
	        - Git init > make repository 
	        - Git commit -m 'initial commmit'
	        - Git add .
	        - Git commit -m 'add line'
	        - Git add . 
	        - Git log --oneline
Chapter_5	Important Concepts
Chapter_5_Notes	.gitignore 
	        - Filelog1.txt in some repository
	        - If you add filelog1.txt to the .gitignore file then git will continue to sync past this
	        - Logfiles/*.md ignores all .md in the directory but you can drill down on this
	Git Branches
	        - Branch = copy of code 
	        - Main branch keeps copy of everything
	        - Then once the main branch is merged with the branch
	                ○ Create pool request
	                ○ Merge
	                ○ Delete old branch & have it merge into the file structure of main
	Git messages
	        - Present tense "fixes [task]" 
	        - ~50 char
	        - Create meaningful messages. 
	        - Git commit -m 
	                ○ Opens text editor / VS Studio Code
	                ○ Message can be multiple lines.
	Merge Conflicts:
	        - Forgetting to 
	
	
	
Course_Summary	

Creating Branch =
	
	Git branch main.GitLearning
	Git checkout main.GitLearning or Git switch main.GitLearning
	Git status (confirms which branch you are in) / the HEAD will point here.
	        • Renaming = git branch -m [new name]
	        • Publish / upload what you have locally to the remote server (PUBLIC = SHARE TO THE REMOTE SERVER)
	
	Local branch 'develop' - local pc 
	Remote branch 'origin/develop' - tracking
	Git branch --track [pathTo] [pathFrom]
	 - git branch --track main main.PowerShell
	
	REMINDER: You must publish the local branch to make it present on the 
	
	Git checkout --track [pathFrom] [pathTo]
	        - Brings Remote to Local (Branch : Branch) 

	Git push -u (Public)
	Git checkout --track
	 then you can just git pull (download from remote) & git push (upload to remote)

	After working on a branch - to DELETE LOCAL;
	        - Git branch -v
	Git branch -d -f main.PowerShell
	-- To Delete REMOTE 
	Git push origin --delete main.PowerShell
	
	
	-- MERGING --
	        1. Switch to branch receiving changes
	        2. Run merge 
	Git switch main 
	Git merge main.PowerShell

Diffing:	Ø Red Triangle shows diffs in VS Code
        - Git Diff	        • Top right has a side-by-side show changes view
	Ø Source Control Panel
	        • Clicking on a file that has changed will give you the diff view
	Ø Select for Compare
	Ø Also: View Timeline in VS Code
VS Code Logs - Output Log	
Looking to up your game?	Copilot = Suggestion based VS Code for git
Fork a repository & then drift through the logs for a revert point.	Git log --pretty=oneline
Git log --pretty=format:"%H - %an - %ar : %s"
https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History
	
</summary>

# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

**less:** More effective to view files than opening in text editor
<br>**find:** Find specific filenames in a directory
<br>**apropos / man:** Ways to get help on a command
<br>**pushd/popd:** Move around directories quickly
<br>**awk:** Find and replace text and sort databases
<br>**grep:** Select a specific string inside a file or terminal output
<br>**env:** Keep track of important environment variables
<br>**pipes (|, <. <<)**: Do things with the output from a file, such as sending it to a textfile or <br>search for a string within an output.
<br>**ps:** Display all running processes
<br>**sudo:** Run command as super user.

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls # List non-hidden files in directory`
<br>`ls -a    # List all files (show hidden)`
<br>`ls -l    # List files in long format`
<br>`ls -lh   # Long format, readable file sizes (K, M, G)`
<br>`ls -lah  # Long, all files, readable file sizes`
<br>`ls -t    # Sort by modification time`  
`ls -Glp      # Long format, show file-type indicator, colorized output`

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

`ls -d    # Directories only`
<br>`ls -L    # Display symbolic links`
<br>`ls -r    # Display files in reverse order`
<br>`ls -R    # Display directories`
<br>`ls -m    # Display as comma separated list`

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

***xargs* can take an input and reads spaces, tabs, newlines, and EOF strings and manipulate the output accordingly.**

**For example, ```cat example.txt | xargs -n 5``` will read the text file 'example.txt' and only return 5 arguments per line in the Terminal.**



                                         ASSINGMENT - 9



1. To what does a relative path refer?
ANS:-The relative path is the path of a file with respect to your current working directory (PWD).




2. What does an absolute path start with your operating system?
ANS:-An absolute path contains the full set of directories from the root of the file system up to your target file or directory. 
     An absolute path start with the root folder, such as / or C:.




3. What do the functions os.getcwd() and os.chdir() do?
ANS:-getcwd stands for "get current working directory". os.getcwd() returns the absolute path of the working directory where Python is currently running as a string str . 
     chdir stabds of "change directory". os.chdir() method in Python used to change the current working directory to specified path. 
     It takes only a single argument as new directory path.




4. What are the . and .. folders?
ANS:-The . is the current directory, while .. signifies the parent directory.




5. In C:\bacon\eggs\spam.txt, which part is the dir name, and which part is the base name?
ANS:-The basename is the final rightmost segment of the file path . In the above path base name is spam.txt. os.path.basename() can be used to extract base name from the path. 
     dir name is th folder name in which file exists. In the above path dir name is C:\bacon\eggs . os.path.dirname() can be used to extract dir name form path.




6. What are the three “mode” arguments that can be passed to the open() function?
ANS:-mode arguments that can be passed to open () function are: 'r' Open a file for reading. (default) 'w' Open a file for writing. 
     Creates a new file if it does not exist or truncates the file if it exists. 'a' Open for appending at the end of the file without truncating it. 
     Creates a new file if it does not exist. '+' Open a file for updating (reading and writing).




7. What happens if an existing file is opened in write mode?
ANS:-when a existing file is opened in write mode, contens which were previously present will be overwritten by new content passed.




8. How do you tell the difference between read() and readlines()?
ANS:-read() reads the entire contents of the file into a string. readline() just reads file till the next line.




9. What data structure does a shelf value resemble?
ANS:-A shelf value resembles a dictionary value; it has keys and values, along with keys() and values() methods that work similarly to the dictionary methods of the same names.
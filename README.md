# lldb_rush

###### Introduction
A debugger (or debugueur, from English debuger) is a software that helps a developer to analyze bugs in a program. For this, it allows you to run the program step by step, to display the value of the variables at any time, to set up breakpoints on conditions or on lines of the program ...
This is the application to the computer programming of the troubleshooting process.

###### Objectives 
The simple purpose of this rush is to make you discover methods that can be used by a debugger in order to detect bugs on your programs in general.
Once this rush has finished using LLDB specifically will no longer have any secrets for you.

###### Mandatory part
For this project you will need to create three different folders containing in each of the files requested for each exercise.

## Iv.1 Part I-Configuration
First you need to make a file of the name of .lldbinit config.
This config file will have to have a specific configuration to lldb launch. This file will then be put in a folder by the name of "00-init" present in the root of your deposit. The requested configuration:
• Syntax intel.
• Change the prompt by the login of the leader of the group.
• Automatic launching a script afficant a banner.

Here is a sample session with the valid configuration script:



## lv.2 Part 2-Use
You're going to have to start using lldb really! To do this you will have to compile by the simple command '‘clang++ -Wall -g source.cpp -o example' This small program coded in C++:

Once the compilation is finished you will have to try to run this program without it bug. For this you must use LLDB and write the following command sequence:


Once you get to this point you should now just make sure that the program works properly with the least possible action. You will have to list then the list of commands (no shortcut) typed in a file named "commands" which will then be presented in your second folder create "01-usage" at the root of your render deposit.

The number of orders will affect your final rating.

Here's an example of valid rendered file:



## lv.3 Part III-Script
You now know how to use lldb correctly we will be able to personaliseer this program by adding our own scripts! So now you have to create a small script (in Python) whose purpose will be to simply display the program name attached to LLDB but reverse! We will finally add a small ft to the beginning of this name.
The script file will be named "reverse.py" and will be inside the last folder located at the root of your render deposit named "02-Script". Here is an example of a possible use:


## Bonus part
As a bonus, there will be only three available.
• The first will be to add color during the banner display containing the login of the group leader of your rush.
• The second will be to automate the launch of commands in a configuration file readable by Lldb.
• The latter will create other "useful" functions in lldb.


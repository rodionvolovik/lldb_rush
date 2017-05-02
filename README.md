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

![Exmaple](https://lh3.googleusercontent.com/07WjxW6AggNosWfBStBt83wfa2zPbRTXj3OfCCRHv4YDuxYDBwOIsCmN_jlKi9qycTYs4bnAmPUEBemcIwTxBbFyVo3uaOPSfKidT1IilxaAPIzcZ3paKLK5EXvrVHnuD0Ff2WIb)

## lv.2 Part 2-Use
You're going to have to start using lldb really! To do this you will have to compile by the simple command '‘clang++ -Wall -g source.cpp -o example' This small program coded in C++:

![Exmaple++](https://lh6.googleusercontent.com/9-k9Sg9_whXC-PljkBnaZRhoKe3wLCbvU90ryy66wx1Svx34uvp4v4AUcPa8kG5KCdbb0zUwFN1AbJvvYxOvq4mIGGYPdAhPbKWSulFpKUwXo8feCG-hqq2AGAbFcOiHcQEPlW6F)

Once the compilation is finished you will have to try to run this program without it bug. For this you must use LLDB and write the following command sequence:

![Exmaple1](https://lh4.googleusercontent.com/Pumx6lYs2S-ZXuTpJG2a3SoJ4LYGP33xxyJTGilaU_74aM5fr0-50ZjKJncDrggfNUCz1YJC5TR_1fXQoDhXXAlCESpwTY6hHcVMqaR9i0cYr_vOjkpbsyaeBqvAfqtfSRtBsd6q)

Once you get to this point you should now just make sure that the program works properly with the least possible action. You will have to list then the list of commands (no shortcut) typed in a file named "commands" which will then be presented in your second folder create "01-usage" at the root of your render deposit.

The number of orders will affect your final rating.

Here's an example of valid rendered file:

![Exmaple3](https://lh6.googleusercontent.com/wds-lTXCP_VpdJnmv3jPWpR4xYnmKXlbre76X8wX1eB3992qIQWPJJJ6xqmdDRkys53MCIGv-9wX5AJbjP7TM8jyC458NvkROwlql-S4ADob6m1Z3oELtTrVN2iEUM0x0v9Hkg5k)

## lv.3 Part III-Script
You now know how to use lldb correctly we will be able to personaliseer this program by adding our own scripts! So now you have to create a small script (in Python) whose purpose will be to simply display the program name attached to LLDB but reverse! We will finally add a small ft to the beginning of this name.
The script file will be named "reverse.py" and will be inside the last folder located at the root of your render deposit named "02-Script". Here is an example of a possible use:

![Exmaple4](https://lh3.googleusercontent.com/PMJm4zPXHo_YOPDRQ207NsOXwoLAnHXBcgVjjFvHuMoxtSONY2leLl1BWEuC1lGLuL6-Lo_G4iJVRt5QZVf_iBZiBlsTJpCwk_mwnzxjA9y5ggsFcuGIrX4ZGwhRVPx_xJ0IP9Lh)

## Bonus part
As a bonus, there will be only three available.
• The first will be to add color during the banner display containing the login of the group leader of your rush.
• The second will be to automate the launch of commands in a configuration file readable by Lldb.
• The latter will create other "useful" functions in lldb.


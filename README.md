# Project-4-App-Backend


Project Overview

|  Day | Deliverable | Status
|---|---| ---|
|Day 1| Project Description | complete
|Day 1| Wireframes / Priority Matrix / Timeline `backend` and `frontend`| complete
|Day 2| Working RestAPI | inomplete
|Day 3| Core Application Structure (HTML, CSS, etc.) | incomplete
|Day 4| MVP & Bug Fixes | incomplete
|Day 5| Final Touches and Present | Incomplete

Project Description:

My project is an updated insult library(Bitter). The app will give you insults to save and use whenever you need. You can add your own special insults and even delete insults you dont think are good. The idea is more of a twitter like network to add and save and share insults. User is able to follow like and rate other users. 





Time/Priority Matrix:


MVP 

Frontend connected to Backend

Generate insults randomly

Login function for user/users

Sign up for user/users

Input for user to add own insults

One model for safe/childish insults

One model for not safe/adult insults

One model for Sign in and Authentication




PostMVP

A button for insult library to have adult insults. 



#### MVP
| Component | Priority | Estimated Time | Time Invetsted | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
| Frontend/Backend connection | H | 8hr | -hr | -hr|
| Show a thread of insults from different users| H | 8hr | -hr | -hr|
| Login/Sign up for users | H | 5hr | 6hr | 6hr|
| Text field Input for users to add own insults | H | 5hr | -hr | -hr|
| Users being able to edit insults after posting insult | H | 8hr | -hr | -hr|
| - | H | 8hr | -hr | -hr|





#### PostMVP
| Component | Priority | Estimated Time | Time Invetsted | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
| Adult insult version | L | 6hr | -hr | -hr|
| Asking for age to apply agre restrictions | L | 6hr | -hr | -hr|



Additional Libraries
N/A



Code Snippet
Use this section to include a brief code snippet of functionality that you are proud of an a brief description


Issues and Resolutions
Use this section to list of all major issues encountered and their resolution.


raise ImproperlyConfigured(
django.core.exceptions.ImproperlyConfigured: Cannot import 'authentication'. Check that 'apps.authentication.apps.AuthenticationConfig.name' is
correct.

This was an error I kept getting and my issues was that I tried to speed run through making the 
whole authentication the Suresh way and I couldn't even figure out where the issue was even with 
everyone in my group helping me. Anyway the resolution was starting over so it's 9/15/2020 right now 
and I just copied Alex's authentication and refactored that and my server can run right now. 


You are trying to add a non-nullable field 'image_url' to user without a default; we can't do that 
(the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py

This was just weird to get and I was unsure how to answer the first time. 


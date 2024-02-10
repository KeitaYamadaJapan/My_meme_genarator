# Meme_Generator
The final project in Udacity's Intermediate Python Nanodegree program. 

In this project, we were tasked with creating a program that superimposes quotes over images to create randomized memes. The quotes were stored in four different file types. Our goal was to properly ingest the content of these files into blank models of our own design. quotes for this project were a combination of starter code from the following link:https://learn.udacity.com/nanodegrees/nd303/parts/cd0011/lessons/56d3e4a6-21ff-4a9b-aff5-7b6327d05a8f/concepts/039d38e8-8f36-4cc0-b86e-96002a7bd0b5
, ideas that I brainstormed referenced sample code provided by lecture of this project.
And at this time, menter introduced me one classmate solution.https://github.com/conjohnson712/Meme_Generator
This solution is very helpful for me.Because this solution are created with essence of lecture.I apreciate.

I used data from this link.
Cherry-picked entries from the following link: [DogCaptions](https://getchip.com/dog-captions/#Short_Dog_Captions_for_Instagram). He replaced the starter image files with a collection of his own dog nfortunately lost his battle with Leukemia in 2016. This project serves as a loving memorial to showcase the comedic, snarky, and loving nature that Moose brought to the life of anyone who met him for over a decade. 

This project was a chance to showcase the skills presented to us in the **'Large Codebases with Libraries'** Course, including: 

- Object-Oriented thinking in Python, including abstract classes, class methods, and static methods.
- DRY (don't repeat yourself) principles of class and method design
- working with modules and packages in Python.
- Working with Flask Apps, CLI, and Web Interfaces
- Keeping code and docstrings PEP-8 compliant


## Overview
![Example](https://github.com/conjohnson712/Meme_Generator/blob/main/static/70.jpg?raw=true)
At the highest level of functionality, this project must complete the following requirements (taken directly from project instructions): 
- Interact with a variety of complex filetypes. This emulates the kind of data you'll encounter in a data engineering role. 
- Load quotes from a variety of filetypes (PDF, Word Docs, CSVs, Text files). 
- Load, manipulate, and save images/ 
- Accept dynamic user input through a command-line tool and a web service. This emulates the kind of work you'll encounter as a full stack developer.


## Setup Instructions
I developed my code on Ubuntu 22.04.2 LTS desktop, running Python 3.10.12. 

I set up with steps as bellow.

sudo apt-get install python3-venv -y
python3.10 -m venv venv
source venv/bin/activate
pip3 install pandas
pip3 install Pillow
pip3 install -U setuptools
pip3 install python-docx 
pip3 install flask -U
pip3 install requests
pip3 freeze > requirements.txt

""""
It is needed to install pdftotext to local computer.
https://www.xpdfreader.com/download.html
I downloaded the Xpdf command line tools xpdf-tools-linux-4.05.tar.gz
We can un tar.gz and place xpdf-tools-linux-4.05 to any holder.
Then add bin directory to my PATH
In case of linux,
Using command line
$ nano ~/.bashrc
At end of bashrc, write next code.
export PATH="$PATH:<DOWNLOAD_LOCATION>/xpdf-tools-linux-4.05/bin64"
Then ctrl + x, push y and Enter
$ source ~/.bashrc
""""

Then I will take next two steps.

rm -rf venv/
zip -r My_meme_generator My_meme_generator

## Run project

Please take next steps.

cd src
python3.10 -m venv venv2
source venv2/bin/activate
pip3 install -r requirements.txt

Please try

1 $ python3 meme.py

2 $ python3 app.py

3 $ export FLASK_APP=app.py
    flask run --host 0.0.0.0 --port 3000 --reload




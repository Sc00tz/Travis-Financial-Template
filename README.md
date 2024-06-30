# Travis-Financial-Template
Python script for QFX/OFX to CSV conversion, and description of Google Sheets setup

The link to the template is here: https://docs.google.com/spreadsheets/d/1HV9SobLd09zyiJF5ya7TRvN2_7r7YyTN0Hd4lpBQkWk/edit?usp=sharing
Just copy it to your own google drive and try it out

# Description
Due to never finding a good financial tool that I liked, was easy to use, and had the features I wanted, I started searching for something better. I found a template for Google Sheets that was okay, but lacking some things. It did give me enough of a base to work from and I created this.

# QFX converter
Banks usually offer a CSV download of your transactions, but they vary greatly. They also usually don't include a transaction ID that makes it easy for finding duplicate entries. I prefer to download them in QFX format and convert them to CSV. There are a number of tools out there that do this, but they all had to seem to have issues with the QFX my bank would export. Since it's just XML, I used some basic XML to CSV conversion ideas and came up with what is in this repo.

# Template Information
I included the template configuration as a text file. I wasn't sure how to do it any other way. I figured this would be useful to see exactly what's going on with an explination.

# Features
- Auto highlights the current month on the budget sheet to easily find the current month.
- Automatic generation of the categories drop down for the transactions based on the subcategories in the budget sheet.
- Automatic highlighting of duplicate entries based on transaction ID.
- "Piggy Bank" sheet for helping keep track of savings goals
- Reports sheet that shows current account balances, cashflow, budget breakdown, and category pie chart (not 100% complete yet)

# Future Ideas
- More automation, including automatic catagory selection based on transaction description



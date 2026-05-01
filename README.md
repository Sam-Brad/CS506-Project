# CS506-Project

## Proposal

### Project Description:
  When creating a product based around modulability, its important that diversity of these modules be apparent.  In the popular card game Magic: The Gathering, there are five colours that a card can be a combination of.  These colours correspond to tactics, with certain effects being more common with certain colours.  Since deck building is such an important part of Magic, its important that an equal number of cards belong to each colour and that the common theme of each colour be preserved.  As the game expands with each new release of cards, this becomes even more important.

### Project Goal:
  This project's goal is to construct a model that can accuratley predict the colour identity of Magic: The Gathering cards.  By inputting a new card's traits, the model should be able to predict and visualize to user's how well it fits into the established data of previous cards.

### Data Collection:
  The full dataset of all Magic cards can be found online.  This website (https://mtgjson.com/getting-started/) offers data files in multiple formats containing all the cards ever made.  For this project, I downloaded the csv file.

### Data Visualization:
  By processing certain features of previous cards, the model will show correlation between certain effects and colour identities.  Other visualizations will include correlation between total cost versus colour identity, as well as heatmaps checking the validation of the model.

## Running the code

### Makefile
  The makefile in this repository contains all the commands needed to install dependencies and run the code.  Use "make install" to install all of the dependencies listed in the requirements.txt file.  Use "make run" to run the code in code.ipynb, which will put the output in the output directory for viewing.

# CS506-Project
github repo:
https://github.com/Sam-Brad/CS506-Project.git

## Final Report
https://youtu.be/TBWAWLVEdZ8

## Proposal

### Project Description:
  When creating a product based around modulability, its important that diversity of these modules be apparent.  In the popular card game Magic: The Gathering, there are five colours that a card can be a combination of.  These colours correspond to tactics, with certain effects being more common with certain colours.  Since deck building is such an important part of Magic, its important that an equal number of cards belong to each colour and that the common theme of each colour be preserved.  As the game expands with each new release of cards, this becomes even more important.

### Project Goal:
  This project's goal is to construct a model that can accurately predict the colour identity of Magic: The Gathering cards.  By inputting a new card's traits, the model should be able to predict and visualize to user's how well it fits into the established data of previous cards.

### Data Collection:
  The full dataset of all Magic cards can be found online.  This website (https://mtgjson.com/getting-started/) offers data files in multiple formats containing all the cards ever made.  For this project, I downloaded the csv file.

### Data Visualization:
  By processing certain features of previous cards, the model will show correlation between certain effects and colour identities.  Other visualizations will include correlation between total cost versus colour identity, as well as heatmaps checking the validation of the model.  Check the file code.ipynb for data visualizations.

## Running the code

### Makefile
  The makefile in this repository contains all the commands needed to install dependencies and run the code.  Use "make install" to install all of the dependencies listed in the requirements.txt file.  Use "make run" to run the code in code.ipynb, which will put the output in the output directory for viewing.

## Extra Information

### Reading a Card
  Cards from Magic: The Gathering have many traits, but here I will explain exactly which features I used in this project.

  Mana value: This represents how much and which kind of mana a cards costs.  For example, a card costing two colorless and two black mana would be {2}{B}{B}.  IMPORTANT, this model predicts colour identity which is based on mana value, however this input is cleaned to remove what colour of mana is within each section.

  Mana cost: This represents the total amount of mana a cards costs, regardless of mana type.  For example, a card costing two colorless and two black mana would have a mana cost of 4.

  Colour identity: This represents the colour combination that the card belongs to.  This is dictated by what colours of mana appear in the cards mana value.  For example, a card costing two colorless and two black mana would have a colour identity of black.

  Text: A series of words that describe effects, abilities, and keywords that can alter how that card is played.

  Type: This represents what category of rules this card follows.  For example, creture cards are placed on the battlefield during your turn and can attack oppoenents, whereas instants can be played at any point and take effect immediately.

  Types: This represents flavour of what factions this cards belong to.  For example, creatures can have types such as "pirate", "dragon", or "goblin", which can make them targets of certain cards.




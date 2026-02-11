# CS506-Project
Proposal

Project Description:
  For many products the usage of the product can depend on the ratings it receives from users, and vice versa.  For this project I wish to create a model that can predict a video games player count based on the recent ratings the game has accrued.  For this instance, I will be using the online cooperative game Helldivers 2.  Since the game is continuously changing with a real time war simulation, new challenges and mechanics are added every update.  These changes motivate players to leave reviews and ratings to communicate to the developers what they liked and did not like.  Usually when an update is fun and enjoyable, old players pick the game up again.  This could mean that there is correlation between the recent ratings of the game and the recent player count on the game.  Since the game is two years old, there are many major updates with lots of data to collect about exploring how this trend could be modeled.
  The timeline for this two month project is planned as such:
  
      Two weeks for data collection
  
      One week for data cleaning
      
      First check-in (March)
      
      One week for feature extraction
      
      Two weeks for data visualization
      
      Second check-in (April)
      
      Two weeks for model training

Project Goal:
  This project's goal is to construct a model that can accurately predict the player count of Helldivers 2 based on the recent ratings score of Helldivers 2 on Steam.  The model should have a level of visualization that allows readers to easily interpet predictions, as well as perhaps update in real time to adjust predictions.

Data Collection:
  Both sets of data (player count and recent rating score) can be found online.
This website contains the entire history of the game's player count: https://steamdb.info/app/553850/charts/#1y .
This website contains the entire history of the game's recent rating score on steam: https://www.lorenzostanco.com/lab/steam/ratings/553850/2years/m+u+ur+uc+urc/ .
By scraping data from these websites, the data collections will be stored in arrays using numpy for easy computation.

Data Visualization:
  By processing the trends of player counts and recent ratings over time, this project will show correlation through linear models constructed from computations based on processed data.  The model will display the correlation of player count vs. recent ratings on the y axis, with time on the x axis in increments of 2 weeks.

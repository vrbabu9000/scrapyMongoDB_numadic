# Scrapy News Extraction Project
- This is an initial task given by Numadic, a Fintech Company where I had applied for an Internship.
- This project is a quick work to meet the rules stated as per the application.

## 1. About the project:
- I have used the scrapy package to scrap news articles from India Today website.
- The scraped data was backed up into the MongoDB Atlas and connected with the streamlit application.
- This was a rush work and I couldnt pay much attention to the UI.
- It works just fine. However, it is slow since I couldnt play around much with the inbuilt cache functions.
- Many tweeks could be done to speed up the process. 

## 2. Navigation:
- In this project, there are 3 windows:
##### 2.1 Home:
- This window shows the newsfeed of scraped data. You can scroll down to see the newsfeed. From the navigation bar you can navigate to the other two windows.
##### 2.2 Scraped Data:
- Scraped data stored in MongoDB is called and converted to Pandas DataFrame. The Dataframe is visible in this Window.
##### 2.3 Search Data:
- The user can search for news using keywords in the keyboard box.

## 3. Deployment:
- The application was built in streamlit and deployed using heroku.
- https://scrapynumadic.herokuapp.com/

# **python Application based on REST API**

## flask & communication with local REDIS:
  
  **GET:** http://127.0.0.1:5000/getByTime 
  - retrieve all messages that were on the REDIS and occurred between two given dates using a REST API GET request.
  - body -> row -> (JSON) | put: {"start":"2021-06-01", "end":"2021-06-01"} 
        
  - (note: msg from the same day - put in start the real date, and put in end the day after(even if it dosnt exist)) 1
      
  **GET**: http://127.0.0.1:5000/getLast
  - retrieve the last message that was on the REDIS server using a REST API GET request.
  
  **POST:** http://127.0.0.1:5000/publish
  - publish new messages to the REDIS server using a REST API POST request.
  - date is saved as key (or a score) for that msg. for example: 20210602001212 (means 02-06-2012 00:12:12) -> "hello world" 
  - body -> row -> (JSON) | put: {"content":"hello world"} 
        
docker-compose separate between the Redis server and the app. 

used Postman for tests (explaind above)

to run the project with docker and docker-compose:
1. docker build . -t project  
2. docker-compose up -d
        
      

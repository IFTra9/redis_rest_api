# **python Application based on REST API**

## flask & communication with local REDIS:
  
  **GET:** http://127.0.0.1:5000/getByTime 
  - retrieve all messages that were on the REDIS and occurred between two given dates using a REST API GET request.
  - in Postman -set body -> row -> (JSON) : {"start":"2021-06-01", "end":"2021-06-01"} 
        
  - (note: msg from the same day - set "start" as the real date, and set "end" to the day after(even if it dosnt exist))
      
  **GET**: http://127.0.0.1:5000/getLast
  - retrieve the last message that was on the REDIS server using a REST API GET request.
  
  **POST:** http://127.0.0.1:5000/publish
  - publish new messages to the REDIS server using a REST API POST request.
  - date is saved as key (or a score) for that msg. for example: 20210602001212 (means 02-06-2021 00:12:12) -> "hello world" 
  - in Postman - set in body -> row -> (JSON) : {"content":"hello world"} 
        
docker-compose separate between the Redis server and the app. 

used Postman for tests (explaind above)

to run the project with docker and docker-compose:
1. docker build . -t project  
2. docker-compose up -d
      

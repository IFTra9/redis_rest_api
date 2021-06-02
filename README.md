#Python Application based on REST API

##flask & communication with local REDIS:
  
  GET: http://127.0.0.1:5000/getByTime
        retrieve all messages that were on the REDIS and occurred between two given dates using a REST API GET request.
        ####body -> row -> (JSON) | put: {"start":"2012-06-01", "end":"2012-06-01"} 
      
  GET: http://127.0.0.1:5000/getLast
       retrieve the last message that was on the REDIS server using a REST API GET request.

  
  POST: publish new messages to the REDIS server using a REST API POST request.
        http://127.0.0.1:5000/publish
        date is saved as key (or a score) for that msg. for example: 20210602001212 (02/06/2012 00:12:12) -> "hello world" 
        ####body -> row -> (JSON) | put: {"content":"hello world"} 
        
docker-compose separate between the Redis server and the app. 

for test: 
         used Postman for test (explaind above)
        
      

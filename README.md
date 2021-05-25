# notifai_rekrutacyjne
I would really appreciate some feedback about things that could be done better (Issue/mail).
Few notes:
 - Heroku app might be a bit laggy (I have another instance running, and afaik it shares resources between them)
 - After cloning repo, I suggest putting it in virtual env, because installing e.g. SQLAlchemy v1.4.15 causes some other packages to throw errors
 - SQLAlchemy version I am using is currently "not ready for production", I hope that it will work on your machine, but in case it didn't, go to [this commit](https://github.com/Normale/notifai_rekrutacyjne/commit/2f037cb307731dbe1c7a03be4495e17b9355fa24)
 where you can find synchronous, "safe" version
## FastApi docs
Whole API is also documented on https://notifai-rekrutacyjne.herokuapp.com/docs (I suggest going there, because I am not even close to that level, when writing docs in Markdown).
There are also ways to manually test it, without the need of any external tools.
##### How to test manually:
1. Type `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoibm90aWYuYWkifQ.2LqWUgLYilJGXye0AyN1PlHlIN_Jvw6iOGSmVv1buRg` in BearerToken value, in Authorize (top-right corner)
2. Test.

## Readme docs
### Methods 
Bearer token needed for some calls: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoibm90aWYuYWkifQ.2LqWUgLYilJGXye0AyN1PlHlIN_Jvw6iOGSmVv1buRg`

------------
------------
* **URL**

  _/message_

* **Method:**
  
  `POST`
  
*  **URL Params**

   _None_

   **Required:**
 
   `Bearer Token Header`

* **Json Params**

  _{
  "text": "string"
}_

* **Success Response:**
  * **Code:** 200 <br />
    **Content:** `{
  "text": "string",
  "views": 0,
  "nr": 0
}`
 
* **Error Response:**
  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{
  "detail": "Not authenticated"
}`

  * **Code:** 422 UNPROCESSABLE ENTRY <br />
    **Content:** `{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}`

* **Sample Call:**
  ```
  curl -X 'POST' \
  'https://notifai-rekrutacyjne.herokuapp.com/message/' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoibm90aWYuYWkifQ.2LqWUgLYilJGXye0AyN1PlHlIN_Jvw6iOGSmVv1buRg' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "213"}'

------------
------------
* **URL**

  _/message_

* **Method:**
  
  `GET`
  
*  **URL Params**

   _message_nr_

* **Json Params**

  _none_

* **Success Response:**
  * **Code:** 200 <br />
    **Content:** `{
  "text": "string",
  "views": 0,
  "nr": 0
}`
 
* **Error Response:**
  * **Code:** 404 NOT FOUND <br />
    **Content:** `{
  "detail": "Message with id {message_nr} not found"
}`


  * **Code:** 422 UNPROCESSABLE ENTRY <br />
    **Content:** `{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}`

* **Sample Call:**
  ```
  curl -X 'GET' \
  'https://notifai-rekrutacyjne.herokuapp.com/message/1' \
  -H 'accept: application/json'


------------
------------
* **URL**

  _/message_

* **Method:**
  
  `PUT`
  
*  **URL Params**

   _message_nr_

   **Required:**
 
   `Bearer Token Header`

* **Json Params**
 _{
  "text": "string"
}_

* **Success Response:**
  * **Code:** 200 <br />
    **Content:** `{
  "text": "string",
  "views": 0,
  "nr": 0
}`
 
* **Error Response:**

    * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{
  "detail": "Not authenticated"
}`

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{
  "detail": "Message with id {message_nr} not found"
}`


  * **Code:** 422 UNPROCESSABLE ENTRY <br />
    **Content:** `{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}`

* **Sample Call:**
  ```x
  curl -X 'PUT' \
  'https://notifai-rekrutacyjne.herokuapp.com/message/123' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoibm90aWYuYWkifQ.2LqWUgLYilJGXye0AyN1PlHlIN_Jvw6iOGSmVv1buRg' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "321"}'
  ```


------------
------------
* **URL**

  _/message_

* **Method:**
  
  `DELETE`
  
*  **URL Params**

   _message_nr_

   **Required:**
 
   `Bearer Token Header`

* **Json Params**

  _none_

* **Success Response:**
  * **Code:** 200 <br />
    **Content:** `{
  "detail": "Message successfully deleted"}`
 
* **Error Response:**
  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{
  "detail": "Not authenticated"
}`
  * **Code:** 404 NOT FOUND <br />
    **Content:** `{
  "detail": "Message with id {message_nr} not found"
}`


  * **Code:** 422 UNPROCESSABLE ENTRY <br />
    **Content:** `{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}`

* **Sample Call:**
  ```
  curl -X 'DELETE' \
  'https://notifai-rekrutacyjne.herokuapp.com/message/1' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoibm90aWYuYWkifQ.2LqWUgLYilJGXye0AyN1PlHlIN_Jvw6iOGSmVv1buRg'
```



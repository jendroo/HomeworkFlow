# User Endpoints

### Login

- `/api/v1/user/login/`
    - `POST`: Login 
        - Request body
        ```json
            {
                "username": "marykate",
                "password": "marykate.11@live.com"
            }
        ```
        - Response
            - Status code: `202` Accepted
                - Response body
                    ```json
                        {
                            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ...",
                            "user": {
                            "id": 1,
                            "username": "kenz",
                            "first_name": "Ken",
                            "last_name": "Zoe",
                            "email": "kenz@example.com",
                            "role": "teacher"
                            }
                        }

                    ```
            - Status code: `400`: Bad Request
                - Response body
                    ```json
                        {
                            "error": "invalid_input",
                            "detail": "Invalid input for login"
                        }
                    ```
                     - Status code: `401` Unauthorized
                - Response body
                    ```json
                        {
                            "error": "invalid_credentials",
                            "detail": "Invalid login credentials"
                        }
                    ```



### Logout

- `/api/v1/user/logout/`
    - `POST`: Logout
        - **Header**
            Authorization: `Token`
        - **Response**
        - Status code: `200` OK
        ```json
        {
            "message": "Logged out successfully."
        }
        ```
            
            - Status code: `401` Unauthorized
           ```json 
        {
            "message": "Log out unsuccessful."
        }
        

### User Profile

- `/api/v1/user/profile/`
    - `GET`: user profile details
    
        **Header** : Authorization token
        - Response Body
        ```json
                {
                    "id": 1,
                    "username": "marykate",
                    "first_name": "Mary",
                    "last_name": "Kate",
                    "email": "kathy@example.com",
                    "role": "teacher"
                }
        ```


- `/api/v1/user/profile/`
    - `PUT`: update user profile details
    
        **Header** : Authorization token
        - Request Body
        ```json
                 {
                    "first_name": "Mary",
                    "last_name": "Kate",
                    "email": "kathy.new@example.com"
                }
        ```
        - Response 
        ```json
                {
                    "id": 1,
                    "username": "marykate",
                    "first_name": "Mary",
                    "last_name": "Kate",
                    "email": "kathy.new@example.com",
                    "role": "teacher"
                }
        ```

- `/api/v1/user/change-password/`
    - `PUT`: logged in user to Change password
        - Request Body
            ```json
                {
                    "old_password": "password",
                    "new_password": "newpassword" 
                }
            ```


              - Response
                - Status Code `200`:OK
            ```json
                {
                    "message": "Password changed successfully.",
                     
                }
            ```

## Classroom
### Class Model


1.  Create a New Class
- Endpoint: `api/v1/user/teacher/class`
- `POST`: create a new Class
**Header** : Authorization token (teacher)

- Request Body:
```json 
{
  "teacher_id": [
    1,
  ],
  "class_name": "7A"
        }

- Response Body:
    - Status Code : `201 Created`

```json {
        "class_id": 1,
        "teacher":[{
            "id":1,
            "first_name": "John",
            "last_name": "Smith"
        },],
        "class_name": "7A",
        }
```



2. Get a specific Class
- Endpoint: `/api/v1/teacher/class/class_id/`
- `GET`: List class
 **Header** : Authorization token
Request Parameters:
?teacher_id=1
?class_id=3

- `api/v1/user/teacher/class/class_id`
    - `GET`: view class by its id 
    


- Response Body:
    - Status Code: `200 OK`

```json
        [
     {
        "class_id": 1,
        "teacher": {
        "id": 1,
        "first_name": "John",
        "last_name": "Smith"
        },
        "class_name": "7a"
     },
]
```

3. Update a class

- Endpoints: api/v1/user/teacher/class/class_id/detail
  -`PATCH`: Update a Class
    **Header** : Authorization token
  Request Body:
```json
{ 
  "class_name": "Class name change"
}

```
- Response Body: 
  - status code: `200 Ok`

 ```json
 {
  "class_id": 1,
  "class_name": "Updated Class",
  
 }

 ```

 <!-- 4. Delete Class
 Endpoint: `api/v1/user/teacher/class/delete`
 - `DELETE`: Delete a Class
    **Header** : Authorization token

 - Request Body: 
   ```json
        {
            "class_id":1
        }     
        ``` 
- Response Body
            - Status Code : `204 No Content`
      ```json
        {
        "message": "Class deleted successfully."
        }            
        ```
        
- Response Body
            - Status Code : `404 Not Found`
      ```json
            {
            "error": "Class not found"
            } 
        ```      -->

## Lesson API

1. Create Lesson
- Endpoints: `api/v1/user/teacher/class/lesson/`

- `POST`: create a lesson.
**Header** : Authorization token (Role: Teacher)

- Request Body:
```json
{
"class_id": 2,
"subject_name": "Music",
"start_time": "08:00:00",
"end_time": "08:45:00",
"day": "Monday"
}

```
- Response Body:
    - Status Code: `201 Created`

```json
{
  "lesson_id": 1,
}


Teacher: Views all his lessons (teacher_id)
Student/Parent: Can view all lessons student is part of (class_id of student)
Seperate for parent/teacher/student

```
2. List Lessons
- `GET`: View Lessons
- Endpoint: `api/v1/user/teacher/class/lessons`

- Response Body: 
    - Status code: `200 OK`

```json
[
  {
    "lesson_id": 1,
    "class_id": 1,
    "teacher": {
      "id": 2,
    },
    "subject_name": "Music",
    "start_time": "08:00:00",
  "end_time": "08:45:00",
  "day": "Monday"
  },
  {
    "lesson_id": 1,
    "class_id": 2,
    "teacher": {
      "id": 2,
    },
    "subject_name": "Music",
    "start_time": "08:00:00",
  "end_time": "08:45:00",
  "day": "Tuesday"
  },
  {
    "lesson_id": 1,
    "class_id": 1,
    "teacher": {
      "id": 2,
    },
    "subject_name": "Music",
    "start_time": "08:00:00",
  "end_time": "08:45:00",
  "day": "Wednesday"
  },
]
```

2. List Lessons
- `GET`: View Lessons
- Endpoint: `api/v1/user/student/class/lessons`

- Response Body: 
    - Status code: `200 OK`

```json
[
  {
    "lesson_id": 1,
    "class_id": 1,
    "teacher": {
      "id": 2,
      "first_name": "John",
      "last_name": "Smith"
    },
    "subject_name": "Music",
    "start_time": "208:00:00",
  "end_time": "08:45:00Z",
  "day": "Monday"
  },
    {
    "lesson_id": 2,
    "class_id": 1,
    "teacher": {
      "id": 3,
      "first_name": "Max",
      "last_name": "Mustermann"
    },
    "subject_name": "Maths",
    "start_time": "08:45:00",
  "end_time": "09:30:00",
  "day": "Monday"
  },
   {
    "lesson_id": 2,
    "class_id": 1,
    "teacher": {
      "id": 3,
      "first_name": "Max",
      "last_name": "Mustermann"
    },
    "subject_name": "Maths",
    "start_time": "08:45:00",
  "end_time": "09:30:00",
  "day": "Tuesday"
  },
]
```

2. List Lessons
- `GET`: View Lessons
- Endpoint: `api/v1/user/parent/class/lessons`

- Response Body: 
    - Status code: `200 OK`

```json
[
  {
    "lesson_id": 1,
    "class_id": 1,
    "teacher": {
      "id": 2,
      "first_name": "John",
      "last_name": "Smith"
    },
    "subject_name": "Music",
    "start_time": "08:00:00",
  "end_time": "08:45:00",
  "day": "Monday"
  },
    {
    "lesson_id": 2,
    "class_id": 1,
    "teacher": {
      "id": 3,
      "first_name": "Max",
      "last_name": "Mustermann"
    },
    "subject_name": "Maths",
    "start_time": "08:45:00",
  "end_time": "09:30:00",
  "day": "Monday"
  },
   {
    "lesson_id": 2,
    "class_id": 1,
    "teacher": {
      "id": 3,
      "first_name": "Max",
      "last_name": "Mustermann"
    },
    "subject_name": "Maths",
    "start_time": "08:45:00",
  "end_time": "09:30:00",
  "day": "Tuesday"
  },
]
```

3. Update Lesson

- `PATCH`: update/change the Lesson.

- Endpoint: `api/v1/user/teacher/class/lesson/lesson_id/`
- Request Body:

```json
{
  "lesson_id":1,
  "start_time": "08:00:00",
  "end_time": "08:45:00",
  "day": "Monday",
}
```
- Response Body:
    - Status Code: `200 OK`

```json 
{
  "lesson_id": 1,
  "class_id": 1,
  "subject_name": "Physics",
  "start_time": "08:00:00",
  "end_time": "08:45:00",
  "day": "Monday",
  "message": "Lesson updated successfully"
}
```
4. Delete Lesson
- Endpoint: `api/v1/user/teacher/class/lesson/lesson_id/`
- `DELETE`: Delete a Class
 - Request Body: 
  -
   ```json
        {
            "lesson_id":1
        }     
        ``` 
- Response Body
            - Status Code : `204 No Content`
      ```json
        {
        "message": "Lesson deleted successfully."
        }            
        ```
        
- Response Body
            - Status Code : `404 Not Found`
      ```json
            {
            "error": "Lesson not found"
            } 
        ```     


## Notification API

1. Create Notification
- `POST`: create a Notification
- Endpoints: `api/v1/user/teacher/class/notification/`

- Request Body: 
```json

{
  "class_id": 1,
  "name": "Test Notification",
  "description": "This is a test notification.",
  "date": "2024-09-10T18:25:43.511Z"
}
```
- Repsonse Body:
    - Status Code: `201 Created`

```json
    {
  "notification_id": 1,
  "class_id": 1,
  "name": "Test Notification",
  "date": "2024-09-10T18:25:43.511Z",
  "message": "Notification created successfully"
}
```
2. List/View Notification
- `GET`: list and view notifications
- Endpoint: `api/v1/user/teacher/class/notification/`

- Request Body: `200 OK`

```json

  {
    "notification_id": 1,
    "class_id": 1,
    "name": "Test Notification",
    "description": "This is a test notification.",
    "date": "2024-09-19T18:25:43.511Z"
  }
```

3. Update Notification
`PATCH`: update/change a notification
- Endpoints:  `api/v1/user/teacher/class/notification/{id}/`

- Request Body:
  

```json
{
  "name": "Updated Notification",
  "description": "Updated test notification.",
  "date": "2024-09-19T18:25:43.511Z"
}
```

- Response Body: 
   - status Code: `200 OK`
```json
{
  "notification_id": 1,
  "class_id": 1,
  "name": "Updated Notification",
  "description": "Updated test notification.",
  "date": "2024-09-19T18:25:43.511Z",
  "message": "Notification updated successfully"
}
```
4. Delete Notification
- `DELETE`: delete a notification
- Endpoints: `api/v1/user/teacher/class/notification/{id}/`

- Response Body:
  - Status Code: `204 No Content`

```json
{
  "message": "Notification deleted successfully."
}

```
- Response Body:
  - status Code: `404 Not Found`
```json
{
  "message": "Notification not found or not authorized."
}

```


# HomeworkFlow Endpoints

## Teacher: Post Homework
- /api/v1/homework/post/
    - POST: Homework
        - Header: Authorization Token

        - Request Body:
            - Fields
                - lesson_id(int)
                    - required: true
                - due_date(date)
                    - required: true
                - description(str)
                    - required: true

            - Example
        ```json
        {
            "lesson_id":"1",
            "due_date":"2012-04-21T18:25:43-05:00",
            "description":"read chapter 1 and answer questions 1-3",
        }
        ```

        - Response:
            - Status Code `201`Created
                - Response Body
                    ```json
                        {
                            "lesson_id":"1"
                        }
                    ```
            - Status code: `400`: Bad Request
                - Response body
                    ```json
                        {
                            "error": "invalid_input",
                            "detail": "Invalid input for login"
                        }
                    ```

## Teacher: Post Feedback

- /api/v1/feedback/post/
    - POST: Weekly_Feedback
        - Header: Authorization Token

        - Request Body:
            - Fields
                - student_id(int)
                    - required: true
                - social_behaviour(choice: good/bad)
                    - required: true
                - work_ethics(choice: good/bad)
                    - required: true
                - written_feedback(str)
                    - required: true

            - Example
        ```json
        {
            "student_id":"1",
            "social_behaviour":"good",
            "work_ethics":"good",
            "written_feedback":"Student 1 showed high motivation and interest, with high participation and good ideas, keep it up!",
        }
        ```


        - Response:
            - Status Code `201`Created
                - Response Body
                    ```json
                        {
                            "student_id":"1"
                        }
                    ```

            - Status code: `400`: Bad Request
                - Response body
                    ```json
                        {
                            "error": "invalid_input",
                        }
                    ```

## Parent: Check Feedback

- /api/v1/feedback/mark/
    - PUT/PATCH: Weekly_Feedback
        - Header: Authorization Token (Parent Role)

        - Request Body:
            - Fields
                - weekly_feedback_id(int)
                    - required: true
                - parent_checked(BOOL)
                    - required: true
            

            - Example
        ```json
        {
            "weekly_feedback_id":"1",
            "parent_checked":"TRUE",
           
        }
        ```


        - Response:
            - Status Code `200`OK
                - Response Body
                    ```json
                        {
                            "weekly_feedback_id":"1"
                        }
                    ```

            - Status code: `400`: Bad Request
                - Response body
                    ```json
                        {
                            "error": "invalid_input",
                        }
                    ```



## Student/Parent: View Feedback

- Teacher can view all feedbacks, but Students & Parents only their own

- /api/v1/feedback/view/
    - GET: Weekly_Feedback
        - Request parameters
        - Header: Authorization Token

        - Response:
            - Status Code `200`OK
                - Response Body
                ```json
                    [
                    {
                        "student_id":"1",
                        "teacher_id":"2",
                        "social_behaviour":"good",
                        "work_ethics":"good",
                        "written_feedback":"Student 1 showed high motivation and interest, with high participation and good ideas, keep it up!",
                        "homework_completion":0.8,
                        "attendance_rate":0.8,
                        "date_created":"2024-04-21T18:25:43-05:00",
                        "parent_checked":"True",
                    },
                    ]
                ```

            - Status code: `401`Unauthorized
                - Response body
                    ```json
                        {
                            "error": "insufficient_rights",
                            "detail": "Insufficient Rights"
                        }
                    ```
            

## Student/Parent: View Homework

- /api/v1/homework/view/
    - GET: Weekly_Homework
        - Request parameters
        - Header: Authorization Token (Role Student/Parent)

        - Response:
            - Status Code `200`OK
                - Response Body
                ```json
                    [
                    {
                        "homework_id":"1",
                        "lesson_id":"1",
                        "due_date":"2012-04-21T18:25:43-05:00",
                        "description":"read chapter 1 and answer questions 1-3",
                        
                    },
                    ]
                ```
            


            - Status code: `401` Unauthorized
                - Response body
                    ```json
                        {
                            "error": "not authorized",
                            "detail": "User is not authorized"
                        }
                    ```

## Teacher: Post Attendance

- /api/v1/attendance/post/
    - POST: Attendance
        - Header: Authorization Token

        - Request Body:
            - Fields
                - student_id(int)
                    - required: true
                - date(date)
                    - required: true
             

            - Example
        ```json
        {
            "lesson_id":"1",
            "date":"2012-04-21T18:25:43-05:00",
            "type":"absent",
            "student_id":"1",
        }
        ```

        - Response:
            - Status Code `201`Created
                - Response Body
                    ```json
                        {
                            "student":"1",
                            "type":"absent"
                        }
                    ```
            - Status code: `400`: Bad Request
                - Response body
                    ```json
                        {
                            "error": "invalid_input",
                            
                        }
                    ```

## Teacher: Post Homework_Completion

- /api/v1/homework/completion/
    - POST: Homework_Completion
        - Header: Authorization Token

        - Request Body:
            - Fields
                - student_id(int)
                    - required: true
                - homework_id(int)
                    - required: true
             

            - Example
        ```json
        [
        {
            "homework_id":"1",
            "student_id":"1",
        },
        {
            "homework_id":"1",
            "student_id":"2",
        },
        {
            "homework_id":"1",
            "student_id":"3",
        },
        {
            "homework_id":"1",
            "student_id":"4",
        },
        ]
        ```

        - Response:
            - Status Code `201`Created
                - Response Body
                    ```json
                        {
                            "homework_id":"1",
                            
                        }
                    ```
            - Status code: `401` Unauthorized
                - Response body
                    ```json
                        {
                            "error": "Unauthorized",
                            "detail": "User not authorized"
                        }
                    ```
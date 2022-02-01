# Deliverect Challenge
This is a code challenge for deliverect selection process

## Challenge

### Tasks
- Retrieve a menu of all the items in the POS. An item can have description, a price, a quantity and an ID
- Add a new item to the menu
- Update an item by ID
- Delete an item by ID
- Create a new order. An order should contain a list of item IDs, with a quantity for each item a payment amount an order note
- Creating a successful order should return the order ID

### Project Guide
- Use any language you prefer, though we're best at reading python and its frameworks like Flask and Django
- Feel free to use any data source, but make sure to include it with the project (if you use sqlite, don't need to including anything, if you use postgres - make sure it's in a docker-compose file or a readme)
- Unit tests are highly favoured
- Provide the project in a github repo or a zip file
- The project should run out of the box, if an included README is followed

### Bonus
- An item can contain modifier groups, with each modifier group containing modifiers
## Solution
### Considerations
This project is made with docker-compose, mongodb, flask and Eve. All known technologies used by deliverect nowadays
### Using the makefile
The whole project is ready to function inside docker containers.

The makefile included in this project simplifies its use, for running the project just type

`make up`

To run the unittests

`make test`

To stop the containers without destroying them

`make stop`

To stop and destroy the containers

`make down`

To rebuild the dockerfile

`make rebuild`
### Endpoints
There are two main endpoints of this api `/items` and `/orders`.

#### retrieve items
- METHOD: GET
- URL: /items
- no body
- sample response
```json
{
    "_items": [
        {
            "_id": "61f87bf6d8f4e2847af473c9",
            "description": "Crispy Chicken Bites",
            "price": 20,
            "quantity": 6,
            "_created": "Thu, 01 Jan 1970 00:00:00 GMT",
            "_updated": "Thu, 01 Jan 1970 00:00:00 GMT",
            "_etag": "55b63325cbe0f3efba188b5811af1fd204f60a1c",
            "_links": {
                "self": {
                    "title": "Item",
                    "href": "items/61f87bf6d8f4e2847af473c9"
                }
            }
        },
        ...
    ],
    "_links": {
        "parent": {
            "title": "home",
            "href": "/"
        },
        "self": {
            "title": "items",
            "href": "items"
        },
        "next": {
            "title": "next page",
            "href": "items?page=2"
        },
        "last": {
            "title": "last page",
            "href": "items?page=3"
        }
    },
    "_meta": {
        "page": 1,
        "max_results": 25,
        "total": 53
    }
}
```
#### Get specific item
- METHOD: GET
- URL: /items/<itemID>
- no body
- sample response
```json
{
    "_id": "61f87bf6d8f4e2847af473d0",
    "description": "Chicken Cajun Club Sandwich",
    "price": 27,
    "quantity": 1,
    "_created": "Thu, 01 Jan 1970 00:00:00 GMT",
    "_updated": "Thu, 01 Jan 1970 00:00:00 GMT",
    "_etag": "1fdbffb3addbe8c458c2d43d738244afcdfa5f6a",
    "_links": {
        "self": {
            "title": "Item",
            "href": "items/61f87bf6d8f4e2847af473d0"
        },
        "parent": {
            "title": "home",
            "href": "/"
        },
        "collection": {
            "title": "items",
            "href": "items"
        }
    }
}
```
#### Create a new item
- METHOD: POST
- URL: /items
- sample body
```json
{
    "description": "test item",
    "quantity": 5,
    "price": 23.50
}
```
- sample response
```json
{
    "_updated": "Tue, 01 Feb 2022 05:55:45 GMT",
    "_created": "Tue, 01 Feb 2022 05:55:45 GMT",
    "_etag": "1cb5252b79444389ba2d3cf214c8a84f32eef87c",
    "_id": "61f8cb61730d713a4c71c927",
    "_links": {
        "self": {
            "title": "Item",
            "href": "items/61f8cb61730d713a4c71c927"
        }
    },
    "_status": "OK"
}
```
#### Update specific item
- METHOD: PATCH
- URL: /items/<itemID>
- HEADER If-Match with `_etag`
- sample body
```json
{
    "description": "tst item"
}
```
- sample response
```json
{
    "_id": "61f8cb61730d713a4c71c927",
    "_updated": "Tue, 01 Feb 2022 06:07:01 GMT",
    "_created": "Tue, 01 Feb 2022 05:55:45 GMT",
    "_etag": "00b6dc523cbd2b17f97723b158107db1a9448345",
    "_links": {
        "self": {
            "title": "Item",
            "href": "items/61f8cb61730d713a4c71c927"
        }
    },
    "_status": "OK"
}
```
#### Delete specific item
- METHOD: DELETE
- URL: /items/<itemID>
- HEADER If-Match with `_etag`
- No body
- No response status code 204
### Tests

The unittests test for the api endpoint, correct response and coherent data. Though the error codes
for requests and not existing objects are handled by the Eve framework, the 
planned tests to corroborate them were skipped.

### Tech Stack

* (flask)[https://flask.palletsprojects.com/en/2.0.x/] - Web framework
* (MongoDB)[https://www.mongodb.com/] - Non relational database
* (Eve)[https://docs.python-eve.org/en/stable/] - REST framework

#! /bin/bash

mongoimport --host mongodb --db orders --collection items --type json --file /database/items.json --jsonArray
mongoimport --host mongodb --db orders --collection orders --type json --file /database/orders.json --jsonArray


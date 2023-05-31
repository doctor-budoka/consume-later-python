# consume-later-python

An API for adding/querying a database of products for later consumption. Could be used as a wishlist of sorts too.

## Endpoints

There are three endpoints for this API: add, get and list

### Add

put takes a media type and an item JSON as input and adds the item to the db

### Get 

Get takes a media type and item name and produces the details of the item

### List

List takes a media type and returns a list of names up to the first 100.

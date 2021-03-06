<h1>Python and Flask</h1>
Built in Python and Flask, use a SQL database with PeeWee models

<h3>Model</h3>

```
class BaseModel(Model):
    class Meta:
        database = db

class Games(BaseModel):
    name = CharField()
    sales = IntegerField()
    release = CharField()
    genre = CharField()
    developer = CharField()
    publisher = CharField()
 ```   

<h3>API Snippet</h3>

```
{
"developer": "id Software",
"genre": "First-person shooter",
"id": 69,
"name": "Doom II: Hell on Earth",
"publisher": "GT Interactive",
"release": "Sep-94",
"sales": 2
},
{
"developer": "id Software",
"genre": "First-person shooter",
"id": 146,
"name": "Quake",
"publisher": "GT Interactive",
"release": "Jun-96",
"sales": 1
},


```
<h3>Routes</h3>

```
home route = '/'
games route = '/games'
games ID route = '/games/<id>'
games name route = '/games/names/<name>'
games genre route = '/games/genre/<genre>'
games developer route = '/games/developer/<developer>'
games publisher route = '/games/publisher/<publisher>'

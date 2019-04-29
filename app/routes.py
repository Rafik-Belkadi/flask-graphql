from app import app
from app.muta import Mutation
from app.schemas import Query
import graphene
from flask_graphql import GraphQLView


schema = graphene.Schema(query=Query, mutation=Mutation)

    

#Routes
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)


@app.route('/')
def index():
    return 'Hello World'

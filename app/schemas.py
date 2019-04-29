import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField,SQLAlchemyObjectType
from .models import Post as PostModel
from .models import Event as EventModel
from .models import User as UserModel

class PostAttribute:
    uuid = graphene.ID()
    title = graphene.String(description="The title of the post")
    body = graphene.String(description="The post body")
    author_id = graphene.ID()
    
class EventAttribute:
    uuid = graphene.ID()
    title = graphene.String(description="The title of the post")
    description = graphene.String(description="The post body")
    author_id = graphene.ID()


class PostObject(SQLAlchemyObjectType, PostAttribute):
    class Meta:
        model = PostModel
        interfaces = (graphene.relay.Node, )

class EventObject(SQLAlchemyObjectType, EventAttribute):
    class Meta:
        model = EventModel
        interfaces = (graphene.relay.Node, )
        
class UserObject(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (graphene.relay.Node, )



class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_posts = SQLAlchemyConnectionField(PostObject)
    all_users = SQLAlchemyConnectionField(UserObject)
    all_events= SQLAlchemyConnectionField(EventObject)
    post    = graphene.relay.Node.Field(PostObject)
    event   = graphene.relay.Node.Field(EventObject)


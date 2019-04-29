import graphene
from app.models import Post,User,Event,db
from app.schemas import PostObject,EventObject,UserObject
from app.schemas import PostAttribute
from app.utils import input_to_dictionary
from datetime import datetime

class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        body = graphene.String(required=True)
        username = graphene.String(required=True)

    post = graphene.Field(lambda: PostObject)

    def mutate(self,info,title,body,username):
        user = User.query.filter_by(username=username).first()
        post = Post(title=title, body=body)

        if user is not None:
            post.author = user

        db.session.add(post)
        db.session.commit()

        return CreatePost(post=post)

class CreateEvent(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        username = graphene.String(required=True)

    event = graphene.Field(lambda: EventObject)

    def mutate(self,info,title,description,username):
        user = User.query.filter_by(username=username).first()
        event = Event(title=title, description=description)

        if user is not None:
            event.manager = user

        db.session.add(event)
        db.session.commit()

        return CreateEvent(event=event)

class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)

    user = graphene.Field(lambda: UserObject)
    
    def mutate(self,info,username):
        user = User(username=username)

        db.session.add(user)
        db.session.commit()

        return CreateUser(user=user)

class UpdatePostInput(graphene.InputObjectType):
    """ Arguments to update a post"""
    id = graphene.ID(required=True,description="Global Id of the person")

class UpdatePost(graphene.Mutation):
    """Update a post"""
    post = graphene.Field(lambda: PostObject, description="Updates a post")

    class Arguments:
        input = UpdatePostInput(required=True)

    def mutate(self,info,input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        post = Post.query.filter_by(id=data['id'])
        post.update(data)
        db.session.commit()
        post = Post.filter_by(id=data['id']).first()

        return UpdatePost(post=post)


class Mutation(graphene.ObjectType):
    CreatePost  = CreatePost.Field()
    CreateEvent = CreateEvent.Field()
    CreateUser  = CreateUser.Field()
    UpdatePost  = UpdatePost.Field() 
    
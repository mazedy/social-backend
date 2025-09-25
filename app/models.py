from neomodel import (
    StructuredNode,
    StringProperty,
    UniqueIdProperty,
    RelationshipTo,
    RelationshipFrom,
    DateTimeProperty,
)


class Post(StructuredNode):
    uid = UniqueIdProperty()
    content = StringProperty(required=True)
    created_at = DateTimeProperty(default_now=True)


class User(StructuredNode):
    uid = UniqueIdProperty()
    username = StringProperty(unique_index=True, required=True)
    email = StringProperty(unique_index=True, required=True)

    # Relationships
    posts = RelationshipTo("Post", "CREATED")
    following = RelationshipTo("User", "FOLLOWS")
    followers = RelationshipFrom("User", "FOLLOWS")

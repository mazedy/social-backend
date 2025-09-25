from .models import User, Post
from .schemas import UserCreate, UserUpdate, PostCreate


# ---------- User CRUD ----------
def create_user(data: UserCreate):
    user = User(username=data.username, email=data.email).save()
    return user

def get_user(uid: str):
    return User.nodes.get_or_none(uid=uid)

def update_user(uid: str, data: UserUpdate):
    user = User.nodes.get_or_none(uid=uid)
    if not user:
        return None
    if data.username:
        user.username = data.username
    if data.email:
        user.email = data.email
    user.save()
    return user

def delete_user(uid: str):
    user = User.nodes.get_or_none(uid=uid)
    if not user:
        return None
    user.delete()
    return True


# ---------- Post CRUD ----------
def create_post(user_id: str, data: PostCreate):
    user = User.nodes.get_or_none(uid=user_id)
    if not user:
        return None
    post = Post(content=data.content).save()
    user.posts.connect(post)
    return post

def get_post(post_id: str):
    return Post.nodes.get_or_none(uid=post_id)

def delete_post(post_id: str):
    post = Post.nodes.get_or_none(uid=post_id)
    if not post:
        return None
    post.delete()
    return True

def get_user_posts(user_id: str):
    user = User.nodes.get_or_none(uid=user_id)
    if not user:
        return None
    return list(user.posts)


# ---------- Follow Logic ----------
def follow_user(follower_id: str, followee_id: str):
    follower = User.nodes.get_or_none(uid=follower_id)
    followee = User.nodes.get_or_none(uid=followee_id)
    if not follower or not followee:
        return None
    follower.following.connect(followee)
    return followee

def unfollow_user(follower_id: str, followee_id: str):
    follower = User.nodes.get_or_none(uid=follower_id)
    followee = User.nodes.get_or_none(uid=followee_id)
    if not follower or not followee:
        return None
    follower.following.disconnect(followee)
    return True

def get_following(user_id: str):
    user = User.nodes.get_or_none(uid=user_id)
    if not user:
        return None
    return list(user.following)

def get_followers(user_id: str):
    user = User.nodes.get_or_none(uid=user_id)
    if not user:
        return None
    return list(user.followers)

from fastapi import APIRouter, HTTPException
from typing import List
from .schemas import (
    UserCreate,
    UserUpdate,
    UserOut,
    PostCreate,
    PostOut,
    FollowOut,
)
from . import controllers

router = APIRouter()


# ---------- User Routes ----------
@router.post("/users/", response_model=UserOut)
def create_user_route(data: UserCreate):
    return controllers.create_user(data)

@router.get("/users/{uid}", response_model=UserOut)
def get_user_route(uid: str):
    user = controllers.get_user(uid)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/users/{uid}", response_model=UserOut)
def update_user_route(uid: str, data: UserUpdate):
    user = controllers.update_user(uid, data)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/users/{uid}")
def delete_user_route(uid: str):
    success = controllers.delete_user(uid)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"deleted": True}


# ---------- Post Routes ----------
@router.post("/users/{uid}/posts", response_model=PostOut)
def create_post_route(uid: str, data: PostCreate):
    post = controllers.create_post(uid, data)
    if not post:
        raise HTTPException(status_code=404, detail="User not found")
    return post

@router.get("/posts/{post_id}", response_model=PostOut)
def get_post_route(post_id: str):
    post = controllers.get_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.delete("/posts/{post_id}")
def delete_post_route(post_id: str):
    success = controllers.delete_post(post_id)
    if not success:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"deleted": True}

@router.get("/users/{uid}/posts", response_model=List[PostOut])
def get_user_posts_route(uid: str):
    posts = controllers.get_user_posts(uid)
    if posts is None:
        raise HTTPException(status_code=404, detail="User not found")
    return posts


# ---------- Follow Routes ----------
@router.post("/users/{follower_id}/follow/{followee_id}", response_model=FollowOut)
def follow_user_route(follower_id: str, followee_id: str):
    user = controllers.follow_user(follower_id, followee_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/users/{follower_id}/unfollow/{followee_id}")
def unfollow_user_route(follower_id: str, followee_id: str):
    success = controllers.unfollow_user(follower_id, followee_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"unfollowed": True}

@router.get("/users/{uid}/following", response_model=List[FollowOut])
def get_following_route(uid: str):
    users = controllers.get_following(uid)
    if users is None:
        raise HTTPException(status_code=404, detail="User not found")
    return users

@router.get("/users/{uid}/followers", response_model=List[FollowOut])
def get_followers_route(uid: str):
    users = controllers.get_followers(uid)
    if users is None:
        raise HTTPException(status_code=404, detail="User not found")
    return users

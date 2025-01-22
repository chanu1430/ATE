

def userSchema(data):
    return {
        "email":data["email"],
        "name":data["name"],
        "clicked":data["clicked"],
        "created_at":data["created_at"],
        "expired_at":data["expired_at"]
    }



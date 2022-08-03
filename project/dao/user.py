# Depricated

# from project.models import User
#
#
# class UserDAO:
#     def __init__(self, session):
#         self.session = session
#
#     def get_one(self, uid):
#         return self.session.query(User).get(uid)
#
#     def get_by_email(self, email):
#         return self.session.query(User).filter(User.email == email).first()
#
#     def get_all(self):
#         return self.session.query(User).all()
#
#     def create(self, user_data):
#         ent = User(**user_data)
#         self.session.add(ent)
#         self.session.commit()
#         return ent
#
#     def delete(self, uid):
#         user = self.get_one(uid)
#         self.session.delete(user)
#         self.session.commit()
#
#     def update(self, user_data, email):
#         user = self.get_by_email(email)
#
#         user.name = user_data.get("name")
#         user.surname = user_data.get("surname")
#         user.favorite_genre = user_data.get("favorite_genre")
#
#         self.session.add(user)
#         self.session.commit()
#
#     def update_password(self, user_data, user):
#         user.password = user_data.get("password")
#
#         self.session.add(user)
#         self.session.commit()

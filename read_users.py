from main import User, session, engine

local_session = session(bind=engine)

users = local_session.query(User).all()

# query para retornar todos os objetos
# users = local_session.query(User).all()
#for user in users:
#    print(user.user_name)

# query para retornar um unico objeto

gibby = local_session.query(User).filter(User.user_name=="jamilson").first()
print(gibby)



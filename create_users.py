from main import User, session, engine

local_session = session(bind=engine)

new_user = User(user_name="gibby", email="gibby@email.com")

local_session.add(new_user)

local_session.commit()
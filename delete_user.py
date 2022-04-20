from main import User, engine, session

local_session = session(bind=engine)


user_to_delete = local_session.query(User).filter(User.user_name == "Guibby").first()

local_session.delete(user_to_delete)

local_session.commit()

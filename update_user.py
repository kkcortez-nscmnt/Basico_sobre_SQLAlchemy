from main import session, engine, User

local_session = session(bind=engine)

user_to_update = local_session.query(User).filter(User.user_name=="gibby").first()

user_to_update.user_name = "Guibby"
user_to_update.email = "Guibby@email.com"

local_session.commit()


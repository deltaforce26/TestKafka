from db.database import session_maker


def insert_model(model):
    with session_maker() as session:
        session.add(model)
        session.commit()
        session.refresh(model)
        print(f'Inserted model: {model}')
        return model.id
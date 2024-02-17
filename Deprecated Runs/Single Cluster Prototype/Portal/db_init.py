from app import app, User, FactoryData, db

with app.app_context():
    db.create_all()

    # Add users
    user1 = User(username='factory1', password='password', factory_id=1)
    user2 = User(username='factory2', password='password', factory_id=2)
    user3 = User(username='factoryManager', password='password', factory_id=0)
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.commit()

    # Add factory data
    factory1_data = FactoryData(factory_id=1, material_in=100, product_out=50)
    factory2_data = FactoryData(factory_id=2, material_in=150, product_out=75)
    db.session.add(factory1_data)
    db.session.add(factory2_data)
    db.session.commit()
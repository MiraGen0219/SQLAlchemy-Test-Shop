from typing import List
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean, select
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker, relationship, Mapped, mapped_column

engine = create_engine('sqlite:///shop_v2.db')
Base = DeclarativeBase()
Session = sessionmaker(bind=engine)
session = Session()

# Database connection
engine = create_engine('sqlite:///shop_v2.db')
print("SQLite engine configured!")





class Base(DeclarativeBase):
    pass

class User(Base): 
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column("user_id", primary_key=True)
    name: Mapped[str] = mapped_column("username", String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    
    # RELATIONSHIP: One User to Many Orders
    orders: Mapped[List["Order"]] = relationship(
    # Cascade Delete had to be added so the entire script can run and not get caught on deltion of a user:
        back_populates = "user", 
        cascade = "all, delete-orphan")


class Product(Base):
    __tablename__ = 'products'
    
    id: Mapped[int] = mapped_column("product_id", primary_key=True)
    name: Mapped[str] = mapped_column("productname", String(200), nullable=False)
    price: Mapped[int] = mapped_column("price", Integer, nullable=False)
    
    # RELATIONSHIP: One Product to Many Orders
    orders: Mapped[List["Order"]] = relationship(back_populates="product")


class Order(Base):
    __tablename__ = 'orders' 
    
    id: Mapped[int] = mapped_column("order_id", primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.product_id"), nullable=False)
    quantity: Mapped[int] = mapped_column("quantity", Integer, nullable=False)
    
    # RELATIONSHIPS: Links back to User and Product
    user: Mapped["User"] = relationship(back_populates="orders")
    product: Mapped["Product"] = relationship(back_populates="orders")

# The drop_all before the create_all wipes the database clean before every update.
Base.metadata.drop_all(engine) 
Base.metadata.create_all(engine)
print("Database structure recreated successfully!")    
    

# Add Users:
user_a = User(name = "Jane Doe", email = "jdoe@example.com")
user_b = User(name = "Diana White", email = "dianawhite@example.com")

session.add(user_a)
session.add(user_b)
session.commit()

# Add Products:
prod_1 = Product(name = "Snuggle Blanket", price = 10)
prod_2 = Product(name = "SnappyFit Bowl", price = 8)
prod_3 = Product(name = "Wabbitat Travel Cage", price = 75)

session.add(prod_1)
session.add(prod_2)
session.add(prod_3)
session.commit()

# Create orders with different quantities:
order_1 = Order(user = user_a, product = prod_1, quantity = 1)
order_2 = Order(user = user_a, product = prod_3, quantity = 2)
order_3 = Order(user = user_b, product = prod_2, quantity = 1)

# Diana's order had to have 2 lines, because of the way of the way the tables are connected.
order_4 = Order(user = user_b, product = prod_1, quantity = 1)
order_5 = Order(user = user_b, product = prod_3, quantity = 1)

session.add_all([order_1, order_2, order_3, order_4, order_5])
session.commit()

print("Successfully added users, products, and split Diana's orders!")



# Retrieval and Update Code:
print("\n--- 1. RETRIEVING ALL USERS ---")
users = session.scalars(select(User)).all()
for u in users:
    print(f"User ID: {u.id} | Username: {u.name} | Email: {u.email}")
    
print("\n--- 2. RETRIEVING ALL PRODUCTS ---")
products = session.scalars(select(Product)).all()
for p in products: 
    print(f"Product Name: {p.name} | Price: ${p.price}")
    
print("\n--- 3. RETRIEVING ALL ORDERS WITH NAMES ---")
orders = session.scalars(select(Order)).all()
for o in orders:
    print(f"Order ID: {o.id} | Buyer: {o.user.name} | Item: {o.product.name} |Qty: {o.quantity}")
    
print("\n--- 4. UPDATING A PRODUCT'S PRICE ---")
blanket = session.get(Product, 1)
if blanket:
    print(f"Old Price for {blanket.name}: ${blanket.price}")
    blanket.price = 25
    session.commit()
    print(f"New Price for {blanket.name}: ${blanket.price} updated successfully!")
else:
    print("Product ID 1 not found")
    
print("\n--- 5. DELETING A USER BY ID ---")
user_to_delete = session.get(User, 1)
if user_to_delete:
    session.delete(user_to_delete)
    session.commit()
    print("User ID 1 has been deleted!")

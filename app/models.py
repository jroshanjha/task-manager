from sqlalchemy import Column, Integer, String,ForeignKey, DateTime
from datetime import datetime
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100), unique=True, index=True)

# class Product(Base):
#     __tablename__ = "products"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(100))
#     price = Column(Integer)
#     quantity = Column(Integer)
#     description = Column(String(100))
#     image = Column(String(100))
#     category = Column(String(100))
#     user_id = Column(Integer, ForeignKey("users.id"))

# class Order(Base):
#     __tablename__ = "orders"
#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     product_id = Column(Integer, ForeignKey("products.id"))
#     quantity = Column(Integer)
#     status = Column(String(100))
#     total = Column(Integer)
#     created_at = Column(DateTime, default=datetime.utcnow)
#     updated_at = Column(DateTime, default=datetime.utcnow)

# class Review(Base): 
#     __tablename__ = "reviews"
#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     product_id = Column(Integer, ForeignKey("products.id"))
#     rating = Column(Integer)
#     comment = Column(String(100))
#     created_at = Column(DateTime, default=datetime.utcnow)
#     updated_at = Column(DateTime, default=datetime.utcnow)

# class Cart(Base):
#     __tablename__ = "carts"
#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     product_id = Column(Integer, ForeignKey("products.id"))
#     quantity = Column(Integer)
#     created_at = Column(DateTime, default=datetime.utcnow)
#     updated_at = Column(DateTime, default=datetime.utcnow)

# class Payment(Base):
#     __tablename__ = "payments"
#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     order_id = Column(Integer, ForeignKey("orders.id"))
#     amount = Column(Integer)
#     status = Column(String(100))
#     created_at = Column(DateTime, default=datetime.utcnow)
#     updated_at = Column(DateTime, default=datetime.utcnow)

# class Shipping(Base):
#     __tablename__ = "shippings"
#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     order_id = Column(Integer, ForeignKey("orders.id"))
#     address = Column(String(100))
#     city = Column(String(100))
#     state = Column(String(100))
#     country = Column(String(100))
#     created_at = Column(DateTime, default=datetime.utcnow)
#     updated_at = Column(DateTime, default=datetime.utcnow)

# class Category(Base):
#     __tablename__ = "categories"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(100))
#     description = Column(String(100))
#     created_at = Column(DateTime, default=datetime.utcnow)
#     updated_at = Column(DateTime, default=datetime.utcnow)

# class Brand(Base):
#     __tablename__ = "brands"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(100))
#     description = Column(String(100))
#     created_at = Column(DateTime, default=datetime.utcnow)
#     updated_at = Column(DateTime, default=datetime.utcnow)

# class Color(Base):
#     __tablename__ = "colors"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(100))
#     description = Column(String(100))
#     created_at = Column(DateTime, default=datetime.utcnow)
#     updated_at = Column(DateTime, default=datetime.utcnow)

# class Size(Base):
#     __tablename__ = "sizes"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(100))
#     description = Column(String(100))
#     created_at = Column(DateTime, default=datetime.utcnow)
#     updated_at = Column(DateTime, default=datetime.utcnow)

# class Tag(Base):
#     __tablename__ = "tags"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(100))
#     description = Column(String(100))
#     created_at = Column(DateTime, default=datetime.utcnow)
#     updated_at = Column(DateTime, default=datetime.utcnow)

# class Discount(Base):
#     __tablename__ = "discounts"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(100))
#     description = Column(String(100))
#     created_at = Column(DateTime, default=datetime.utcnow)
#     updated_at = Column(DateTime, default=datetime.utcnow)

# class Coupon(Base):
#     __tablename__ = "coupons"
#     id = Column(Integer, primary_key=True, index=True)
#     code = Column(String(100))
#     discount_id = Column(Integer, ForeignKey("discounts.id"))
#     created_at = Column(DateTime, default=datetime.utcnow)
#     updated_at = Column(DateTime, default=datetime.utcnow)

# class Wishlist(Base):
#     __tablename__ = "wishlists"
#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     product_id = Column(Integer, ForeignKey("products.id"))
#     created_at = Column(DateTime, default=datetime.utcnow)
#     updated_at = Column(DateTime, default=datetime.utcnow)

# class CartItem(Base):
#     __tablename__ = "cart_items"
#     id = Column(Integer, primary_key=True, index=True)
#     cart_id = Column(Integer, ForeignKey("carts.id"))
#     product_id = Column(Integer, ForeignKey("products.id"))
#     quantity = Column(Integer)
#     created_at = Column(DateTime, default=datetime.utcnow)
#     updated_at = Column(DateTime, default=datetime.utcnow)

# class OrderItem(Base):
#     __tablename__ = "order_items"
#     id = Column(Integer, primary_key=True, index=True)
#     order_id = Column(Integer, ForeignKey("orders.id"))
#     product_id = Column(Integer, ForeignKey("products.id"))
#     quantity = Column(Integer)
#     created_at = Column(DateTime, default=datetime.utcnow)
#     updated_at = Column(DateTime, default=datetime.utcnow)

# %%
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# %%
engine = create_engine("sqlite:///:memory:", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# %%
from datetime import datetime
from sqlalchemy import (
    Table,
    Column,
    Integer,
    Numeric,
    String,
    DateTime,
    Boolean,
    ForeignKey,
)
from sqlalchemy.orm import relationship, backref, declarative_base

# %%
Base = declarative_base()


class Cookie(Base):
    __tablename__ = "cookies"

    cookie_id = Column(Integer, primary_key=True)
    cookie_name = Column(String(50), index=True)
    cookie_recipe_url = Column(String(255))
    cookie_sku = Column(String(55))
    quantity = Column(Integer)
    unit_cost = Column(Numeric(12, 2))

    def __repr__(self):
        return f"Cookie(cookie_name={self.cookie_name},cookie_recipe_url={self.cookie_recipe_url},cookie_skue={self.cookie_sku},quantity={self.quantity},unit_cost={self.unit_cost})"


# %%
class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    username = Column(String(15), nullable=False, unique=True)
    email_address = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=False)
    password = Column(String(25), nullable=False)
    create_on = Column(DateTime(), default=datetime.now)
    update_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return f"User(username={self.username},email_address={self.email_address},phone={self.phone},password={self.password})"


class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey("users.user_id"))
    user = relationship("User", backref=backref("orders", order_by=order_id))

    def __repr__(self):
        return "Order(user_id={self.user_id},shipped={self.shipped})"


class Lineitems(Base):
    __tablename__ = "line_items"
    line_item_id = Column(Integer(), primary_key=True)
    order_id = Column(Integer(), ForeignKey("orders.order_id"))
    cookie_id = Column(Integer(), ForeignKey("cookies.cookie_id"))
    quantity = Column(Integer())
    extended_cost = Column(Numeric(12, 2))
    order = relationship(
        "Order", backref=backref("line_items", order_by=line_item_id)
    )
    cookie = relationship("Cookie", uselist=False, order_by=cookie_id)

    def __repr__(self):
        return "Lineitems(order_id={self.order_id},cookie_id={self.cookie_id},quantity={self.quantity},extended_cost={self.extened_cost})"


Base.metadata.create_all(engine)

# %%
cc = Cookie(
    cookie_name="chocolate chip",
    cookie_recipe_url="http://some.aweso.me/cookie/recippe.html",
    cookie_sku="cc01",
    quantity=12,
    unit_cost=0.5,
)
session.add(cc)
session.commit()

# %%
cc.cookie_id

# %%
dcc = Cookie(
    cookie_name="dark chocolate chip",
    cookie_recipe_url="http://some.aweso.me/cookie/recipe_dark.html",
    cookie_sku="CC02",
    quantity=1,
    unit_cost=0.75,
)
mol = Cookie(
    cookie_name="molasses",
    cookie_recipe_url="http://some.aweso.me/cookie/recipe_molasses.html",
    cookie_sku="MOL01",
    quantity=1,
    unit_cost=0.80,
)
session.add(dcc)
session.add(mol)
session.flush()
print(dcc.cookie_id)
print(mol.cookie_id)

# %%
c1 = Cookie(
    cookie_name="peanut butter",
    cookie_recipe_url="http://some.aweso.me/cookie/peanut.html",
    cookie_sku="PB01",
    quantity=24,
    unit_cost=0.25,
)
c2 = Cookie(
    cookie_name="oatmeal raisin",
    cookie_recipe_url="http://some.okay.me/cookie/raisin.html",
    cookie_sku="EWW01",
    quantity=100,
    unit_cost=1.00,
)
session.bulk_save_objects([c1, c2])
session.commit()
print(c1.cookie_id)

# %%
from sqlalchemy import text

with engine.connect() as cnn:
    result = cnn.execute(text("select * from cookies"))
    print(result.fetchall())

# %%
ccs = session.query(Cookie).all()
print(ccs)

# %%
from pprint import pprint

pprint(ccs)

# %%
for cookie in session.query(Cookie):
    print(cookie)

# %%
print(session.query(Cookie.cookie_name, Cookie.quantity).first())

# %%
for cookie in session.query(Cookie).order_by(Cookie.quantity):
    print(f"{cookie.quantity:3} - {cookie.cookie_name}")

# %%
from sqlalchemy import desc

for cookie in session.query(Cookie).order_by(desc(Cookie.quantity)):
    print(f"{cookie.quantity:<15}{cookie.cookie_name}")

# %%
query = session.query(Cookie).order_by(Cookie.quantity)[:2]
print([(result.cookie_name, result.quantity) for result in query])

# %%
query = session.query(Cookie).order_by(Cookie.quantity).limit(2)
print([(result.cookie_name, result.quantity) for result in query])

# %%
from sqlalchemy import func

inv_count = session.query(func.sum(Cookie.quantity))
print(inv_count.all())

# %%
inv_count = session.query(func.sum(Cookie.quantity))
print(inv_count.count())

# %%
cnt = session.query(func.count(Cookie.cookie_name)).scalar()
print(cnt)

# %%
cnt = session.query(func.count(Cookie.cookie_name).label("inv_count")).first()
print(cnt._key_to_index)

# %%
cnt.inv_count

# %%
rec = (
    session.query(Cookie).filter(Cookie.cookie_name == "chocolate chip").first()
)
print(rec)

# %%
rec = session.query(Cookie).filter_by(cookie_name="chocolate chip").first()
print(rec)

# %%
query = session.query(Cookie).filter(Cookie.cookie_name.like("%chocolate%"))
for row in query:
    print(row.cookie_name)

from sqlalchemy import Column, Integer, String, ForeignKey, Date, SmallInteger, Float
from sqlalchemy.orm import relationship

from app.database.connection import Base


class Object(Base):
    __tablename__ = 'object'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    owner_id = Column(Integer, ForeignKey('owner.id'))
    industry_id = Column(Integer, ForeignKey('industry.id'))
    address_id = Column(Integer, ForeignKey('address.id'))
    year_construction = Column(Integer, nullable=True)
    year_purchase = Column(Integer, nullable=True)
    document_id = Column(Integer, ForeignKey('document.id'))
    contract_id = Column(Integer, ForeignKey('contract.id'))
    class_name = Column(String)
    floors_below = Column(Integer)
    floors_above = Column(Integer)
    area_total = Column(Float)
    area_rentable = Column(Float)
    parking_closed = Column(SmallInteger)
    parking_open = Column(SmallInteger)
    plot_owned = Column(Float)
    plot_rent = Column(Float)
    status_id = Column(Integer, ForeignKey('status.id'))
    create_user = Column(String)
    update_user = Column(String, nullable=True)
    create_date = Column(Date)
    update_date = Column(Date, nullable=True)

    owner = relationship('Owner', back_populates='objects')
    industry = relationship('Industry', back_populates='objects')
    address = relationship('Address', back_populates='objects')
    status = relationship('Status', back_populates='objects')
    document = relationship('Document', back_populates='objects')
    contract = relationship('Contract', back_populates='objects')


class Owner(Base):
    __tablename__ = 'owner'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    bin = Column(Integer)
    name = Column(String)
    abbreviation = Column(String)
    mp_share = Column(Integer)
    create_user = Column(String)
    update_user = Column(String, nullable=True)
    create_date = Column(Date)
    update_date = Column(Date, nullable=True)

    objects = relationship('Object', back_populates='owner')


class Industry(Base):
    __tablename__ = 'industry'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    create_user = Column(String)
    update_user = Column(String, nullable=True)
    create_date = Column(Date)
    update_date = Column(Date, nullable=True)

    objects = relationship('Object', back_populates='industry')


class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    street_id = Column(Integer, ForeignKey('street.id'))
    num = Column(String)
    sub_num = Column(String)

    objects = relationship('Object', back_populates='address')
    street = relationship('Street', back_populates='addresses')


class Street(Base):
    __tablename__ = 'street'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    locality_id = Column(Integer, ForeignKey('locality.id'))
    name = Column(String)

    addresses = relationship('Address', back_populates='street')
    locality = relationship('Locality', back_populates='streets')


class Locality(Base):
    __tablename__ = 'locality'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    country_id = Column(Integer, ForeignKey('country.id'))
    name = Column(String)

    streets = relationship('Street', back_populates='locality')
    country = relationship('Country', back_populates='localities')


class Country(Base):
    __tablename__ = 'country'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)

    localities = relationship('Locality', back_populates='country')


class Document(Base):
    __tablename__ = 'document'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    type_id = Column(Integer, ForeignKey('document_type.id'))
    number = Column(String)
    date = Column(Date)

    objects = relationship('Object', back_populates='document')
    document_type = relationship('DocumentType', back_populates='documents')


class DocumentType(Base):
    __tablename__ = 'document_type'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)

    documents = relationship('Document', back_populates='document_type')


class Contract(Base):
    __tablename__ = 'contract'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    object_cost_kzt = Column(Float)
    object_cost_usd = Column(Float)
    market_cost_kzt = Column(Float)
    date = Column(Date)

    objects = relationship('Object', back_populates='contract')


class Status(Base):
    __tablename__ = 'status'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    create_user = Column(String)
    update_user = Column(String, nullable=True)
    create_date = Column(Date)
    update_date = Column(Date, nullable=True)

    status_rules = relationship('StatusRules', back_populates='status')
    objects = relationship('Object', back_populates='status')


class StatusRules(Base):
    __tablename__ = 'status_rules'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    from_ = Column("from", String)
    to = Column(String)
    create_user = Column(String)
    update_user = Column(String, nullable=True)
    create_date = Column(Date)
    update_date = Column(Date, nullable=True)
    status_id = Column(Integer, ForeignKey('status.id'))

    status = relationship('Status', back_populates='status_rules')


from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import *

class OrderModel(Base):
    __tablename__ = "order"
    
    #Attributes
    id = Column(Integer, primary_key=True)
    type_order_id = Column(Integer, ForeignKey('type_order.id'))
    src_region_id = Column(Integer, ForeignKey('region.id'))
    dst_region_id = Column(Integer, ForeignKey('region.id'))
    unit_id = Column(Integer, ForeignKey('unit.id'))
    
    #Relationships
    type_order=relationship('TypeOrderModel',  back_populates='orders')
    src_region=relationship('RegionModel', 
        primaryjoin="OrderModel.src_region_id == RegionModel.id",
        back_populates="orders_src_region")
    dst_region=relationship('RegionModel', 
        primaryjoin="OrderModel.dst_region_id == RegionModel.id",
        back_populates="orders_dst_region")
    unit=relationship("UnitModel",  back_populates='order')
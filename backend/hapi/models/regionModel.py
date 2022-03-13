from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base

adjoining = Table(
    'adjoining', Base.metadata,
    Column('dst_region_id', Integer, ForeignKey('region.id')),
    Column('src_region_id', Integer, ForeignKey('region.id')),
    UniqueConstraint('dst_region_id', 'src_region_id', name='unique_adjoining'))

class RegionModel(Base):
    __tablename__= "region"

    #Attributes
    id = Column(Integer, primary_key=True )    
    name=Column(String(45), nullable=False)
    abreviation=Column(String(10), nullable=False)
    power_id=Column(Integer, ForeignKey('power.id'))
    hasCenter=Column(Boolean)

    
    #Relationships
    power = relationship('PowerModel', backref="regions")
    types = relationship('TypeRegionModel',secondary='typeRegionRegion',  back_populates="regions")
    dispositionsUnit=relationship('dispositionUnitModel',backref="region")   

    units_src_region = relationship('UnitModel', back_populates="src_region")
    units_cur_region = relationship('UnitModel', back_populates="cur_region")
    orders_src_region = relationship('OrderModel', back_populates="src_region")
    orders_dst_region = relationship('OrderModel', back_populates="dst_region")


    neighbours = relationship("RegionModel", secondary=adjoining, 
                           primaryjoin=id==adjoining.c.src_region_id,
                           secondaryjoin=id==adjoining.c.dst_region_id)


    def beNeigbours(self, neighbour):
        if neighbour not in self.neighbours:
            self.neighbours.append(neighbours)
            neighbour.neighbours.append(self)
from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base
from hapi.models.typeRegionRegion import typeRegionRegion

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
    map_id=Column(Integer, ForeignKey('map.id'))
   
    hasCenter=Column(Boolean, nullable=False)

    
    #Relationships
    map=relationship('MapModel', back_populates="regions")
    types = relationship('TypeRegionModel',
        secondary=typeRegionRegion,
        back_populates="regions"
    )
    disposition_unit=relationship('DispositionUnitModel', back_populates="region")   

    units_src_region = relationship('UnitModel',
        primaryjoin="UnitModel.src_region_id == RegionModel.id",
        back_populates="src_region"
    )
    units_cur_region = relationship('UnitModel',
        primaryjoin="UnitModel.cur_region_id == RegionModel.id",
        back_populates="cur_region"
    )
    orders_src_region = relationship('OrderModel',
        primaryjoin="OrderModel.src_region_id == RegionModel.id",
        back_populates="src_region")
    orders_dst_region = relationship('OrderModel', 
        primaryjoin="OrderModel.dst_region_id == RegionModel.id",
        back_populates="dst_region")


    neighbours = relationship("RegionModel", secondary="adjoining", 
                           primaryjoin=id==adjoining.c.src_region_id,
                           secondaryjoin=id==adjoining.c.dst_region_id)


    def beNeigbours(self, neighbour):
        if neighbour not in self.neighbours:
            self.neighbours.append(neighbour)
            neighbour.neighbours.append(self)
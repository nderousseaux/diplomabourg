from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base
from hapi.models.playerPower import playerPower

class PowerModel(Base):
    __tablename__= "power"

    #Attributes
    id = Column(Integer, primary_key=True )
    name=Column(String(45), unique=False, nullable=False)
    color_id=Column(Integer, ForeignKey('color.id'))
    map_id=Column(Integer, ForeignKey('map.id'))

    #Relationships
    color=relationship('ColorModel', back_populates="powers")
    map=relationship('MapModel', back_populates="powers")
    regions=relationship('RegionModel', back_populates="power")
    dispositions=relationship('DispositionModel', 
        primaryjoin="DispositionModel.power_id==PowerModel.id",
        back_populates="power")

    players=relationship("PlayerModel",
        secondary=playerPower,
        back_populates="powers"
    )
    units=relationship("UnitModel", 
        primaryjoin='foreign(UnitModel.player_power_power_id) == PowerModel.id',
        back_populates="power"
    )

    #Vérifie qu'une puissance est disponible
    def check_is_available(self, player):
        #On regarde qui à pris cette puissance dans la partie
        p = [p for p in self.players if p.game == player.game]

        #Si il y a personne ou lui même, alors la puissance est dispo
        if len(p) == 0 or p[0] == player:
            return True
        return False
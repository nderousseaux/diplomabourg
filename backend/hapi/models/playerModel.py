from email import message
from sqlalchemy import *
from sqlalchemy.orm import relationship

from hapi.models import Base
from hapi.models.playerPower import playerPower


class PlayerModel(Base):
    __tablename__="player"

    #Attributes
    id = Column(Integer, primary_key=True)
    username=Column(String(45), nullable=False)
    is_admin=Column(Boolean, nullable=False, default=False)
    game_id=Column(Integer ,ForeignKey('game.id'))
    is_ready=Column(Boolean, default=False)
    
    #Relationships
    game=relationship('GameModel', back_populates='players')
    power=relationship("PowerModel",
        secondary=playerPower,
        back_populates="players"
    )

    def orders(self):
        orders = []
        for unit in self.units:
            orders += unit.orders

        num_tour = self.game.num_tour    
        return [o for o in orders if o.num_tour == num_tour]

    def units(self):
        return [u for u in self.game.units if u.player() == self]

    def nb_center(self):
        """Renvoie le nombre de centre controlé par le joueur
        """
        return len([u for u in self.units() if u.type_unit.name == "CENTER"])

    def is_winner(self):
        """True si le joueur à gagné la partie
        """
        if self.game.state != "END":
            return None
        
        if self.nb_center() >= 18:
            return True
        
        if self.nb_center() in [p.nb_centers for p in self.game.players]:
            return True

        return False
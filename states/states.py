from aiogram.fsm.state import State, StatesGroup

class RetseptState(StatesGroup):
    mahsulot_kutish = State()

class KunlikMenyuState(StatesGroup):
    talab_kutish = State()

class HaftalikMenyuState(StatesGroup):
    talab_kutish = State()
class TayyorlashState(StatesGroup):
    ovqat_kutish = State()
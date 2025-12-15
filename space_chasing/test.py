import pytest
from character import Character, Player, Enemy, Item

# absolute import of classes to test (module is a namespace package)
import character as ch


# Mocks to avoid opening turtle windows and touching real scoreboard / randomness / time
class MockTurtle:
    def __init__(self):
        self._pos = (0, 0)
        self._heading = 0
        self._shape = None
        self._shapesize = None

    def setposition(self, x, y):
        self._pos = (x, y)

    def pos(self):
        return self._pos

    def penup(self):
        pass

    def hideturtle(self):
        pass

    def clear(self):
        pass

    def speed(self, s):
        pass

    def color(self, c):
        pass

    def ht(self):
        pass

    def forward(self, dist):
        # simple forward along +x for tests
        x, y = self._pos
        self._pos = (x + dist, y)

    def backward(self, dist):
        x, y = self._pos
        self._pos = (x - dist, y)

    def left(self, angle):
        self._heading = (self._heading + angle) % 360

    def right(self, angle):
        self._heading = (self._heading - angle) % 360

    def towards(self, _):
        return 0

    def shape(self, s):
        self._shape = s

    def goto(self, x, y):
        self._pos = (x, y)


class MockScreen:
    def __init__(self):
        self._handlers = {}

    def bye(self):
        self._bye_called = True

    def clear(self):
        self._cleared = True

    def onkeypress(self, func, key):
        self._handlers.setdefault("keypress", {})[key] = func

    def onkey(self, func, key):
        self._handlers.setdefault("key", {})[key] = func

    def listen(self):
        self._listened = True


class MockScore:
    def __init__(self, *args, **kwargs):
        self.last = None

    def insert(self, name, score):
        self.last = (name, score)


def setup_module(module):
    # Patch module-level names to use mocks
    ch.Turtle = MockTurtle
    ch.Screen = MockScreen
    ch.Score = MockScore


def test_character_type_validation():
    # valid construction should not raise
    ch.Turtle = MockTurtle
    ch.Screen = MockScreen
    Character("blue", 1, size=3, x=0, y=0)

    # invalid x type
    with pytest.raises(TypeError):
        Character("blue", 1, x="not-a-number")

    # invalid y type
    with pytest.raises(TypeError):
        Character("blue", 1, y=None)

    # invalid color type
    with pytest.raises(TypeError):
        Character(123, 1)

    # invalid speed type
    with pytest.raises(TypeError):
        Character("red", "fast")


def test_player_movement_updates_position():
    ch.Turtle = MockTurtle
    ch.Screen = MockScreen
    p = Player()
    initial_pos = p.turtle.pos()
    p.walk_forward()
    # update logical position properties from turtle
    p.x, p.y = p.turtle.pos()
    assert p.x > initial_pos[0]
    p.walk_backward()
    p.x, p.y = p.turtle.pos()
    assert p.x < initial_pos[0] + 6  # moved back from forward


def test_enemy_hit_records_score_and_sets_flag(monkeypatch):
    ch.Turtle = MockTurtle
    ch.Screen = MockScreen
    ch.Score = MockScore

    # create player and enemy
    player = Player()
    # place player at origin explicitly
    player.turtle.setposition(0, 0)
    player.x, player.y = player.turtle.pos()
    # set lifetime to 0 so score is deterministic
    player.lifetime = 0

    enemy = Enemy()
    # place enemy at same position as player to force hit
    enemy.turtle.setposition(0, 0)
    enemy.x, enemy.y = enemy.turtle.pos()

    # ensure time.time returns 5 for deterministic score
    monkeypatch.setattr(ch.time, "time", lambda: 5)

    enemy.hit(player, "alice")
    assert enemy.hit_p is True
    # Score instance stored on enemy should have recorded the insertion
    assert isinstance(enemy.score, MockScore)
    assert enemy.score.last == ("alice", 5)


def test_item_collect_activates_and_clears_list():
    ch.Turtle = MockTurtle
    ch.Screen = MockScreen

    class TestItem(Item):
        def __init__(self, shape, size):
            super().__init__(shape, size)
            self.activated = False

        def activate(self):
            self.activated = True

    player = Player()
    player.turtle.setposition(10, 10)
    player.x, player.y = player.turtle.pos()

    item = TestItem("circle", 2)
    # place item at same position as player
    item.turtle.setposition(10, 10)
    item.x, item.y = item.turtle.pos()

    items = [item]
    item.collect(player, items)
    assert item.activated is True
    assert items == []
    # after collect, turtle was moved away (goto 1000,1000 sets pos)
    assert item.turtle.pos() == (1000, 1000)

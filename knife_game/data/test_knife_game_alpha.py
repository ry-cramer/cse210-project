import pytest
import knife, constants, director

# Testing: knife.py

def test_throw(self):
    """Test Knife.throw function to verify knife is moving at
    the speed defined in constants.py"""
    k = knife.Knife()
    speed = k.throw(self)
    assert speed == constants.KNIFE_THROWN_MOVEMENT_SPEED


# Testing: director.py

def test_setup_knife_count(self):
    """Test Director.setup function to verify knife_count is
    no longer defined as None"""
    d = director.Director()
    d.setup(self)
    assert d.knife_count == 5
    
def test_setup_knife_list(self):
    """Test Director.setup function to verify knife_list is
    no longer defined as None"""
    d = director.Director()
    d.setup(self)
    assert d.knife_list != None

def test_setup_wheel_list(self):
    """Test Director.setup function to verify wheel_list is
    no longer definead as None"""
    d = director.Director()
    d.setup(self)
    assert d.knife_count != None

def test_on_key_press_enter():
    """Test Director.on_key_press to verify that pressing
    ENTER changes current_state of game to running."""
    d = director.Director()
    key = "arcade.key.ENTER"
    
    d.on_key_press(key)
    assert d.current_state == "GameState.GAME_RUNNING"

def test_on_key_press_space():
    """Test Director.on_key_press to verify that pressing
    SPACE removes 1 knife from knife_count."""
    d = director.Director()
    key = "arcade.key.SPACE"
    before_throw = d.knife_count

    d.on_key_press(key)
    after_throw = d.knife_count
    assert after_throw == before_throw - 1


# Call the main function that is part of pytest so that
# the test functions in this file will execute.
pytest.main(["-v", "--tb=no", "test_jumper.py"])
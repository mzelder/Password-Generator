import pytest
import pyperclip
from main import App

@pytest.fixture
def app():
    return App()    

def test_generator(app):
    app.pwd_length_scale.set(10)
    obj1 = app.generate()
    assert len(obj1) == 10

    app.pwd_length_scale.set(40)
    obj2 = app.generate()
    assert len(obj2) == 40

    app.destroy()

def test_updatecheckbox(app):
    app.lower.set(False)
    app.upper.set(False)
    app.numbers.set(False)
    app.symbol.set(False)
    app.update_checkbox()
    assert app.lower.get() == True

    app.destroy()

def test_copy(app):
    app.copy()
    assert pyperclip.paste() == app.pwd_entry.get()


    
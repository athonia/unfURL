import pytest
from urlshort import create_app

@pytest.fixture
def app():
    app = create_app()
    # app.config['TESTING'] = True
    yield app

    @pytest.fixture
    def client(app):
        return app.test_client()
    
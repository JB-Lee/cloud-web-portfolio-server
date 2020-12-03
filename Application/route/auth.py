from ..database import DBSessionPool
from ..model import User
from ..router import RouteContainer


class AuthRoute(RouteContainer):
    def route(self):
        @self.app.post("auth/login")
        async def login():
            pass

        @self.app.post("auth/register")
        async def register(user: User):
            with DBSessionPool.get_instance() as conn:
                with conn.cursor() as cur:
                    sql = '''
                    INSERT INTO "User" (USER_ID, PASSWORD, NAME, EMAIL) VALUES (:user_id, :password, :name, :email)
                    '''

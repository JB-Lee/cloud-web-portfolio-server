from typing import Optional

from fastapi import Response, Request, Header

from ..database import DBSessionPool
from ..model import User, Login
from ..router import RouteContainer


class AuthRoute(RouteContainer):
    def route(self):
        @self.app.post("/auth/login")
        async def login(login_model: Login, response: Response, request: Request,
                        user_agent: Optional[str] = Header(None)):
            with DBSessionPool.get_instance() as conn:
                with conn.cursor() as cur:
                    sql = '''
                    SELECT COUNT(*) 
                    FROM "User" 
                    WHERE USER_ID = RPAD(:user_id, 12) AND PASSWORD = RPAD(:user_pw, 24)
                    '''
                    cur.execute(sql, user_id=login_model.user_id, user_pw=login_model.password)
                    result = cur.fetchone()[0]

                if not result:
                    return {"login": "fail"}

                ip = request.client.host

                new_session = await self.session_manager.create_session(login_model.user_id, ip, user_agent)
                response.set_cookie(key="session_id", value=new_session.id)

                conn.commit()

                return {"login": "success"}

        @self.app.post("/auth/register")
        async def register(user: User):
            with DBSessionPool.get_instance() as conn:
                with conn.cursor() as cur:
                    sql = '''
                    INSERT INTO "User" (USER_ID, PASSWORD, NAME, EMAIL) VALUES (:user_id, :password, :name, :email)
                    '''

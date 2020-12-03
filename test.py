import asyncio


async def main():


# with DBSessionPool.get_instance() as conn:
#     with conn.cursor() as cur:
#         res = cur.callfunc("register", int, ['test', 'test', 'test', 'test'])
#         fetches = cur.execute('''SELECT * FROM "User"''').fetchall()
#         print(res)
#         print(fetches)
#     conn.commit()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

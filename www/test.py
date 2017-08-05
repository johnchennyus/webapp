import orm

from models import User, Blog, Comment
import asyncio

async def test(loop):
    await orm.create_pool(loop=loop, user = 'root', password ='password', db='awesome')
    
    u = User(name='Test7', email='test@example.com7', passwd='1234567890', image='about:blank1',test = 'haha')
    await u.save()

#    findone = User()
    tt = await u.findNumber('name,email')
    print(tt)

loop =asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()

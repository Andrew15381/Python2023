#!/usr/bin/env python3
import asyncio
import shlex
import cowsay

clients = {}

async def chat(reader, writer):
    me = "{}:{}".format(*writer.get_extra_info('peername'))
    print(me)
    clients[me] = ['', asyncio.Queue()]
    send = asyncio.create_task(reader.readline())
    receive = asyncio.create_task(clients[me][1].get())
    while not reader.at_eof():
        done, pending = await asyncio.wait([send, receive], return_when=asyncio.FIRST_COMPLETED)
        for q in done:
            if q is send:
                send = asyncio.create_task(reader.readline())
                cmd = shlex.split(q.result().decode())
                if not cmd:
                    continue
                if cmd[0] == 'who':
                    await clients[me][1].put(', '.join([c[0] for c in clients.values()]))
                elif cmd[0] == 'cows':
                    cs = [c[0] for c in clients.values()]
                    await clients[me][1].put(', '.join([c for c in cowsay.list_cows() if c not in cs]))
                elif cmd[0] == 'login':
                    if cmd[1] not in [c[0] for c in clients.values()] and cmd[1] in cowsay.list_cows():
                        clients[me][0] = cmd[1]
                        await clients[me][1].put('Succesful login')
                    else:
                        await clients[me][1].put('Failed to login')
                elif cmd[0] == 'say':
                    if cmd[1] in [c[0] for c in clients.values()] and clients[me][0]:
                        for c in clients:
                            if clients[c][0] == cmd[1]:
                                break
                        await clients[c][1].put(cmd[2])
                    else:
                        await clients[me][1].put('Login to say')
                elif cmd[0] == 'yield':
                    if clients[me][0]:
                        for out in clients.values():
                            if out is not clients[me] and out[0]:
                                await out[1].put(cmd[1])
            elif q is receive:
                receive = asyncio.create_task(clients[me][1].get())
                writer.write(f"{q.result()}\n".encode())
                await writer.drain()
    send.cancel()
    receive.cancel()
    print(me, "DONE")
    del clients[me]
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(chat, '0.0.0.0', 1337)
    async with server:
        await server.serve_forever()

asyncio.run(main())

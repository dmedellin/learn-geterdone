---
format: long
lesson: enterprise-patterns-concurrency-and-session-state/session-state
title: Session state: client, server or database?
thumb: Where does the cart live?
---

@chapter Session or record
@title text="Session State" sub="Patterns of Enterprise Application Architecture, Chapters 6 and 17" art=thumb
Your server is stateless. Good. So where does the cart live? Fowler gives three answers, and each one moves or holds a very different number of bytes.

@quote text="Session state needs to be committed to become record data." cite="Fowler, Patterns of Enterprise Application Architecture, Chapter 6"
First, a distinction. The cart is session state: data that matters only to one session, inside a business transaction. Record data is the long term data every session sees. Session state needs to be committed to become record data.

@words text="Not valid yet · isolated · not a cache"
Because it lives inside a business transaction, it has the transaction's properties. It needn't be valid while you work on it; a half filled form can break the rules until it's committed. It must be isolated. And a cache isn't session state, because losing a cache loses only speed.

@chapter Three places
@art three-places
Client Session State keeps it on the client: in the URL, a cookie, a hidden field, or a rich client's objects. Server Session State keeps it on the server, in memory or serialized somewhere durable. Database Session State breaks it into tables and fields, like record data.

@art client-round-trip
Client state crosses the wire with every request. A few fields are no burden. But in one of Fowler's applications it came to about a megabyte, as XML. And anything sent to a client can be edited by a malicious user, so it must be validated again when it comes back.

@art server-map
Server Session State, at its simplest, is a map in memory from session id to session object. It assumes enough memory, one server, and that losing a session in a crash is acceptable. Lift those, and you serialize it to a memento on a shared store.

@art pending-rows
Database Session State pulls what a request needs from the database, and saves it back. Its problem is keeping pending data out of everyone else's queries, with a session id in each row, or separate pending tables. It pays for reading and writing on every request.

@chapter The code
@code block=1 lines=1-14 label=Java focus="4@a map in memory|8-10@the first time"
Here's Server Session State at its simplest. A map in memory, from the id the browser sends to that session's cart, creating a cart the first time an id is seen. Only this server can find these carts, and a crash loses them.

@chapter Count the bytes
@math heading="a-megabyte: 100 users, 20 requests, 32-byte id" items="client, a request: 2 × 1,000,000 = 2,000,000@two million;;client, a session: 40,000,000@forty million;;server or database, on the wire: 32@thirty two;;server memory: 100 × 1,000,000 = 100,000,000@a hundred million;;database, a request: 2,000,000@through the database"
The lab counts bytes, for the book's megabyte session. Client state goes out and comes back, so two million bytes a request, and forty million a session. Server or database state carries just the id: thirty two bytes. Server memory holds a hundred million. And two million go through the database each request.

@math heading="a-small-cart: 2,000 bytes" items="client: 4,000 a request · 80,000 a session@four thousand;;id: still 32@still thirty two;;memory 200,000 · database 4,000@two hundred thousand"
Now a small cart of two thousand bytes. Client state is four thousand a request, and eighty thousand a session. The id is still thirty two. Memory holds two hundred thousand, and the database moves four thousand. Every figure but the id scales with the state.

@chapter Fowler's choice
@art cluster-affinity
A cluster raises a harder question. Server state is awkward to migrate, since often only the server holding it can find it. Pinning users to one server by IP address can tie everyone behind one proxy to one machine. Database state copes best with a crash.

@words text="Server state, memento stored remotely" sub="client state for ids and very small data"
Fowler's preference is Server Session State, with its memento stored remotely so it survives a crash. And Client Session State for ids and very small data. Whatever else you use, at least a session id lives on the client.

@chapter Where people slip
@list heading="Common slips" items="Client session state is free@The first|Server session state is simple@The second|A cache is session state@And the third"
The first slip is thinking client state is free because the server stores nothing. It sends forty million bytes in one session. The second is thinking server state is simple. Only until there are two servers. And the third is counting a cache as session state.

@chapter Try it
@words text="5,000 users · 40,000 bytes · 12 requests · 32-byte id"
Your turn. Five thousand users, forty thousand bytes of state each, twelve requests in a session, and a thirty two byte id. Work out the client bytes a request and a session, what server or database state puts on the wire, the server's memory, and the database's bytes a request.

@end text="Count the bytes yourself"
You can change the session's size and count what each choice moves, on Learn. That's learn dot get er done dot I O.

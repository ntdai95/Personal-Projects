# Belay

Belay is a Slack-style chat application. The server is Flask over SQLite and the front
end is plain JavaScript with no framework. It supports accounts with hashed passwords,
channels, threaded replies, per-channel unread counts, and links that take you to the
exact message you were sent after you log in.

## Demo

Every screenshot below is the running application in a browser at `127.0.0.1:5000`.

### Signing in

Accounts are stored with a bcrypt hash and a server-issued key. The key goes in
`localStorage` and travels in the `Authorization` header on every later request.

![Login and signup](docs/01-login.png)

### Channels and unread counts

The channel list shows how many messages have arrived in each channel since you last
read it. The count comes from the last message id you were shown, recorded per user and
per channel, so each person sees their own number. Here `general` is caught up and
`release planning` has one message waiting.

![Channel list with unread counts](docs/02-channels.png)

### Messages

Each message shows its author and how many replies it has. The reply count updates in
place while you are reading, without rebuilding the list under your cursor.

![Messages in a channel](docs/03-messages.png)

### Threads

Opening a thread shows the parent message with its replies underneath. The URL for this
view is `/channel/1/thread/1`, and it is shareable. If you send it to someone who is
logged out, they see the login form and land on this exact thread once they sign in.

![A thread with replies](docs/04-thread.png)

## How to run the program

Install Requirements:
1. Type the following command to install the required python modules: "pip install -r requirements.txt"

Run App:
1. Type the following command to start the server: "python app.py"
2. Open a web browser and type the following url: "127.0.0.1:5000"

## How it works

The server exposes a small JSON API and serves one static page. The front end decides
what to show from `window.location.pathname`, and it uses `history.pushState` to move
between views, so the back button works and every view has a real URL.

| Route | Purpose |
|---|---|
| `GET /api/user` | Log in and receive the auth key |
| `POST /api/user` | Create an account |
| `GET /api/channel` | List channels |
| `POST /api/channel` | Create a channel |
| `GET /api/channel/<id>/message` | List a channel's messages with reply counts |
| `POST /api/channel/<id>/message` | Post a message |
| `GET /api/channel/<id>/message/<id>` | Read a message and its replies |
| `POST /api/channel/<id>/message/<id>` | Reply to a message |
| `GET /api/message/unread` | Unread counts for every channel |
| `POST /api/message/unread` | Record the last message a user has seen |

Four tables sit behind it. `user` holds the account and its bcrypt hash, `channel` holds the
names, `message` holds both messages and replies (a reply carries `is_reply` and the id
it answers), and `user_channel` records the last message each user saw in each channel.

## Correctness and security review

I went back through this project with the application running and fixed the defects
below. Each one is listed with how it was found, because several of them only appear
when you use the application instead of reading it.

**Any request could authenticate as anyone.** Every query was assembled by putting the
value straight into the SQL string, so sending `Authorization: x' OR '1'='1` matched a
row and passed the authentication check on every endpoint. A request with no account at
all could post messages. All 23 statements now pass their values as parameters.

**A message could run code in another user's browser.** Message text was written into
the page with `innerHTML`, so a message containing `<img src=x onerror=...>` executed
for everyone who opened the channel. I confirmed that it fired before making the change. Text now
goes in through `textContent`, and the image-embedding feature still works because it
appends real elements instead of markup.

**Nobody could log in on their first try.** The page remembered the current URL so it
could return you there after signing in, but it did that on the login page too, so a
new visitor was sent back to the form they had just submitted. It only worked on a
second attempt. The URL is now remembered only when it points at a channel or a thread.

**Channel names and messages were stored URL-encoded.** The front end encoded text
before sending it as JSON, where no encoding is needed, so the database held
`release%20planning`. The matching decode on render hid this on screen but not from the
API or any other client. Both halves are gone and the text is stored as typed.

**The message list was rebuilt on every poll.** The guard meant to skip the rebuild
compared `messageContent.length`, and a `div` has no `length`, so the comparison was
always true. The list was cleared and recreated continuously, which made it flicker and
made the reply buttons hard to click. It now compares `children.length`.

**The page polled as fast as the network allowed.** Each polling function called itself
from inside its own callback with no delay, so the browser ran out of ephemeral ports
and reported `ERR_ADDRESS_IN_USE`. The loops now wait one second between cycles.

**The documented install did not work.** `requirements.txt` never listed Flask, which
the app imports, and pinned three packages it never uses at versions that no longer
install. Following the instructions produced `ModuleNotFoundError: No module named
'flask'`. The file now lists what the application actually imports.

**Two requests could crash or create a bad account.** Logging in without a password
raised an exception and returned a 500, and signing up with an empty username
succeeded. Both are now rejected.

## What I would do next

Sessions never expire, so an auth key is good forever once issued. Passwords are sent
as query parameters on login, which puts them in server logs, and they belong in a POST
body. Each database call opens its own connection and does not close it. None of these
block the application, and all of them would matter if it ran anywhere real.

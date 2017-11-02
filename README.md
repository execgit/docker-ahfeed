# Introduction

Dockerfile to build an [ejabberd][] container image with a basic
[AbuseHelper](https://github.com/abusesa/abusehelper) botnet for
receiving feeds and archiving them to JSON files.

Based on
[docker-ejabberd](https://github.com/rankenstein/rroemhild/ejabberd).

# Quick Start

Similarly to
[docker-ejabberd](https://github.com/rankenstein/rroemhild/ejabberd),
you can start a container with the following command:

```bash
docker run -d \
    --name "ejabberd" \
    -p 5222:5222 \
    -h 'xmpp.example.fi' \
    -e "XMPP_DOMAIN=example.fi" \
    -e "ERLANG_NODE=ejabberd" \
    -e "EJABBERD_ADMINS=admin@example.fi admin2@example.fi" \
    -e "EJABBERD_USERS=admin@example.fi:password1234 admin2@example.fi" \
    -e "TZ=Europe/Helsinki" \
    execgit/ahfeed
```

This will create an ejabberd container, where the room `feed.incoming`
is monitored, and all of the events will be archived under the
directory `/var/lib/ah2/feed/archive`.

# Persistence

For easier access and storage of the incoming feed data, you can mount
the volume at `/var/lib/ah2/feed/archive`. Incoming data is saved to
files in directory structure format `%Y/%m/%d.json`. The JSON files
are updated in real time, and old files are automatically compressed
to save space.

# Environment variables

All of the
[docker-ejabberd](https://github.com/rankenstein/rroemhild/ejabberd)
environment variables should be supported. Additional variables:

* **LOBBY**: The [AbuseHelper](https://github.com/abusesa/abusehelper) service room for the feed botnet. By default `feed`.
* **FEED_CHANNEL**: The XMPP channel to store the feed. By default `incoming`, which will result as the channel name `feed.incoming`.

# Further documentation

For further configuration and usage instructions, refer to
[docker-ejabberd](https://github.com/rankenstein/rroemhild/ejabberd).

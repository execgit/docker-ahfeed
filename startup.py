import os

from abusehelper.core.startup import Bot
from abusehelper.core.runtime import Room, Session

from credentials import xmpp_jid, xmpp_password

EJABBERD_HOME = os.environ.get('EJABBERD_HOME')
DOMAIN = os.environ.get('XMPP_DOMAIN')
LOBBY = os.environ.get('FEED_LOBBY', 'feed')
CHANNEL = os.environ.get('FEED_CHANNEL', 'incoming')

class UserBot(Bot):
    def __init__(self, name, **attrs):
        baseattrs = dict(
            module="abusehelper.core."+name,
            bot_name=name,

            xmpp_extra_ca_certs=\
            '{0}/ssl/{1}.pem'.format(EJABBERD_HOME, DOMAIN),
            xmpp_jid=xmpp_jid,
            xmpp_password=xmpp_password,
            service_room=LOBBY,
            )

        baseattrs.update(attrs)
        Bot.__init__(self, name, **baseattrs)
        
def configs():

    #load bots from abusehelper.core
    yield UserBot("runtime", config='./startup.py')
    yield UserBot("roomgraph")

    yield UserBot('archivebot', 
                  _module='abusehelper.bots.archivebot.archivebot',
                  archive_dir='archive')

    yield Room("{0}.{1}".format(LOBBY, CHANNEL)) | Session('archivebot')
